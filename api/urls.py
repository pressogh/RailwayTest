from django.urls import path, include
from rest_framework import routers

from api import views

router = routers.DefaultRouter()

router.register(r"review-note", views.ReviewNoteViewSet)
router_urlpatterns = [path("", include(router.urls))]

urlpatterns = (
	router_urlpatterns
)
