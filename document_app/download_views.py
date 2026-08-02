from django.http import HttpResponse

import json


def download_json(request):

    report = request.session.get("report")

    if report is None:

        return HttpResponse("No report available.")

    response = HttpResponse(

        json.dumps(report, indent=4),

        content_type="application/json"

    )

    response["Content-Disposition"] = 'attachment; filename="verification_report.json"'

    return response