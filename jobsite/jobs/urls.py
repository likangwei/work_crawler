__author__ = 'likangwei'
from django.conf.urls import url, include, patterns
import views
from rest_framework.routers import DefaultRouter

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'jobs', views.JobViewSet)
router.register(r'company', views.CompanyViewSet)

# The API URLs are now determined automatically by the router.
# Additionally, we include the login URLs for the browsable API.
urlpatterns = [
    url(r'^$', views.index),
    url(r'^rest/', include(router.urls)),
]