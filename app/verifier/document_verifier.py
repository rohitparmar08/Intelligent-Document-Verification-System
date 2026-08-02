import re


class DocumentVerifier:

    def __init__(self, data):
        self.data = data

    def verify_name(self):
        name = self.data.get("Name", "")

        if name == "Not Found":
            return False

        return len(name.strip()) >= 3

    def verify_gender(self):
        gender = self.data.get("Gender", "")

        return gender in ["Male", "Female", "Other"]

    def verify_year(self):
        year = self.data.get("Year of Birth", "")

        if not str(year).isdigit():
            return False

        year = int(year)

        return 1900 <= year <= 2100

    def verify_aadhaar(self):
        aadhaar = self.data.get("Aadhaar Number", "")

        pattern = r"^\d{4}\s\d{4}\s\d{4}$"

        return bool(re.match(pattern, aadhaar))

    def confidence_score(self):

        score = 0

        if self.verify_name():
            score += 25

        if self.verify_gender():
            score += 25

        if self.verify_year():
            score += 25

        if self.verify_aadhaar():
            score += 25

        return score

    def overall_status(self):

        if self.confidence_score() >= 75:
            return "VERIFIED"

        return "NOT VERIFIED"

    def verify(self):

        return {
            "Name Valid": self.verify_name(),
            "Gender Valid": self.verify_gender(),
            "Year Valid": self.verify_year(),
            "Aadhaar Valid": self.verify_aadhaar(),
            "Confidence Score": self.confidence_score(),
            "Overall Status": self.overall_status(),
        }
