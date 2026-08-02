from image_processing.image_loader import ImageLoader
from image_processing.image_quality import ImageQuality
from image_processing.blur_detector import BlurDetector
from image_processing.noise_detector import NoiseDetector

from ocr.ocr_engine import OCREngine
from extractor.aadhaar_extractor import AadhaarExtractor
from verifier.document_verifier import DocumentVerifier


IMAGE_PATH = "sample.jpeg"


def main():

    # -----------------------------
    # Image Loading
    # -----------------------------
    loader = ImageLoader(IMAGE_PATH)
    image = loader.load_image()

    # -----------------------------
    # Image Quality
    # -----------------------------
    quality = ImageQuality(image)
    blur = BlurDetector(image)
    noise = NoiseDetector(image)

    print("=" * 60)
    print("           DOCUMENT QUALITY REPORT")
    print("=" * 60)

    width, height = quality.get_dimensions()

    print(f"Image Size        : {width} x {height}")
    print(f"Brightness        : {quality.get_brightness():.2f}")
    print(f"Blur Score        : {blur.blur_score():.2f}")
    print(f"Noise Score       : {noise.noise_score():.2f}")

    print()

    print(
        f"Resolution Status : {'PASS' if not quality.is_low_resolution() else 'FAIL'}"
    )
    print(f"Blur Status       : {'PASS' if not blur.is_blurry() else 'FAIL'}")
    print(f"Noise Status      : {'PASS' if not noise.is_noisy() else 'FAIL'}")

    print()

    overall = (
        not quality.is_low_resolution()
        and not blur.is_blurry()
        and not noise.is_noisy()
    )

    print(f"Overall Status    : {'ACCEPTED' if overall else 'REJECTED'}")

    print("=" * 60)

    if not overall:
        return

    # -----------------------------
    # OCR
    # -----------------------------
    print("\nOCR RESULT")
    print("=" * 60)

    ocr = OCREngine()
    text = ocr.extract_text(IMAGE_PATH)

    for line in text:
        print(line)

    # -----------------------------
    # Information Extraction
    # -----------------------------
    extractor = AadhaarExtractor(text)

    extracted_data = extractor.extract()

    print("\n" + "=" * 60)
    print("      EXTRACTED DOCUMENT INFORMATION")
    print("=" * 60)

    for key, value in extracted_data.items():
        print(f"{key:<18}: {value}")

    # -----------------------------
    # Verification
    # -----------------------------
    verifier = DocumentVerifier(extracted_data)

    result = verifier.verify()

    print("\n" + "=" * 60)
    print("         DOCUMENT VERIFICATION REPORT")
    print("=" * 60)

    for key, value in result.items():
        print(f"{key:<20}: {value}")

    print("=" * 60)


if __name__ == "__main__":
    main()
