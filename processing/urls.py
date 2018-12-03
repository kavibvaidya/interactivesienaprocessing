from django.urls import path
from . import views
from processing.views import *

app_name = "processing"

urlpatterns =[
    path('', HomePage.as_view(), name="Homepage"),
    path("processed", Processed.as_view(), name="Processed"),
    path('download', Download.as_view(), name="Download"),
]
