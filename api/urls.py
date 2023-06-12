from django.urls import path

from api.views import TestApiView

urlpatterns = [
    path('test', TestApiView.as_view()),
]