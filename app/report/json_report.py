import json


class JSONReport:

    def __init__(self, extracted, verification):

        self.extracted = extracted

        self.verification = verification

    def generate(self):

        report = {

            "Document Information": self.extracted,

            "Verification Report": self.verification

        }

        return json.dumps(report, indent=4)