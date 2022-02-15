from django.urls import path
from . import views



urlpatterns=[
    path("script/",views.TestApiView.as_view())
]