from django.urls import path
from . import views
from processing.views import *

app_name = "processing"

urlpatterns =[
    path('', HomePage.as_view(), name="Homepage"),
    path('updates', Updates.as_view(), name="Updates")
]
