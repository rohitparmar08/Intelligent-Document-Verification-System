from app.report.json_report import JSONReport
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage

from app.image_processing.image_loader import ImageLoader
from app.image_processing.image_quality import ImageQuality
from app.image_processing.blur_detector import BlurDetector
from app.image_processing.noise_detector import NoiseDetector

from app.ocr.ocr_engine import OCREngine
from app.extractor.aadhaar_extractor import AadhaarExtractor
from app.verifier.document_verifier import DocumentVerifier
from document_app.utils import download_json


def home(request):

    if request.method == "POST":

        uploaded_file = request.FILES["document"]

        fs = FileSystemStorage()

        filename = fs.save(uploaded_file.name, uploaded_file)

        image_path = fs.path(filename)

        image = ImageLoader(image_path).load_image()

        quality = ImageQuality(image)

        blur = BlurDetector(image)

        noise = NoiseDetector(image)

        ocr = OCREngine()

        text = ocr.extract_text(image_path)

        extractor = AadhaarExtractor(text)

        extracted = extractor.extract()

        verifier = DocumentVerifier(extracted)

        verification = verifier.verify()

        request.session["report"] = {
            "Document Information": extracted,
            "Verification Report": verification,
        }

        report = JSONReport(extracted, verification)

        json_report = report.generate()

        if "download" in request.POST:

          return download_json(json_report)

        return render(
            request,
            "index.html",
            {
                "uploaded": True,
                "image_url": fs.url(filename),

                "width": quality.get_dimensions()[0],
                "height": quality.get_dimensions()[1],
                "brightness": round(quality.get_brightness(), 2),

                "blur_score": round(blur.blur_score(), 2),
                "noise_score": round(noise.noise_score(), 2),

                "extracted": extracted,
                "verification": verification,

                "json_report": json_report,
            },
        )

    return render(request, "index.html")