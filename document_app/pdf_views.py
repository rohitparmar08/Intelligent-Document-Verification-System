from django.http import HttpResponse

from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

import io


def download_pdf(request):

    report = request.session.get("report")

    if report is None:
        return HttpResponse("No report available.")

    buffer = io.BytesIO()

    doc = SimpleDocTemplate(buffer)

    styles = getSampleStyleSheet()

    elements = []

    elements.append(
        Paragraph(
            "<b>DOCUMENT VERIFICATION REPORT</b>",
            styles["Heading1"]
        )
    )

    elements.append(Paragraph("<br/>", styles["Normal"]))

    elements.append(
        Paragraph(
            "<b>Document Information</b>",
            styles["Heading2"]
        )
    )

    for key, value in report["Document Information"].items():

        elements.append(
            Paragraph(f"{key} : {value}", styles["Normal"])
        )

    elements.append(Paragraph("<br/>", styles["Normal"]))

    elements.append(
        Paragraph(
            "<b>Verification Report</b>",
            styles["Heading2"]
        )
    )

    for key, value in report["Verification Report"].items():

        elements.append(
            Paragraph(f"{key} : {value}", styles["Normal"])
        )

    doc.build(elements)

    pdf = buffer.getvalue()

    buffer.close()

    response = HttpResponse(
        pdf,
        content_type="application/pdf"
    )

    response["Content-Disposition"] = (
        'attachment; filename="verification_report.pdf"'
    )

    return response