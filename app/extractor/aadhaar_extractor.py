import re


class AadhaarExtractor:

    def __init__(self, text_lines):
        self.text_lines = text_lines

    def get_full_text(self):
        return " ".join(self.text_lines)

    def extract_aadhaar_number(self):

        text = self.get_full_text()

        pattern = r"\b\d{4}\s\d{4}\s\d{4}\b"

        match = re.search(pattern, text)

        if match:
            return match.group()

        return "Not Found"

    def extract_gender(self):

        text = self.get_full_text().lower()

        if "male" in text:
            return "Male"

        if "female" in text:
            return "Female"

        return "Not Found"

    def extract_year_of_birth(self):

        text = self.get_full_text()

        match = re.search(r"\b(19|20)\d{2}\b", text)

        if match:
            return match.group()

        return "Not Found"

    def extract_name(self):

        keywords = [
            "government",
            "india",
            "authority",
            "address",
            "male",
            "female",
            "year",
            "birth",
            "unique",
            "identification",
            "uidai",
        ]

        for line in self.text_lines:

            clean = line.strip()

            if len(clean.split()) < 2:
                continue

            lower = clean.lower()

            if any(word in lower for word in keywords):
                continue

            if re.search(r"\d", clean):
                continue

            return clean

        return "Not Found"

    def extract(self):

        return {
            "Document Type": "Aadhaar",
            "Name": self.extract_name(),
            "Gender": self.extract_gender(),
            "Year of Birth": self.extract_year_of_birth(),
            "Aadhaar Number": self.extract_aadhaar_number(),
        }
