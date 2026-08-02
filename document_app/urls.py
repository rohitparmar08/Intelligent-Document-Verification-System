from django.urls import path

from . import views
from . import download_views
from . import pdf_views

urlpatterns = [

    path("", views.home, name="home"),

    path(
        "download-json/",
        download_views.download_json,
        name="download_json",
    ),

    path(
        "download-pdf/",
        pdf_views.download_pdf,
        name="download_pdf",
    ),

]