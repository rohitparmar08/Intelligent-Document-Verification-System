from django.http import HttpResponse


def download_json(json_report):

    response = HttpResponse(

        json_report,

        content_type="application/json"

    )

    response["Content-Disposition"] = 'attachment; filename="verification_report.json"'

    return response