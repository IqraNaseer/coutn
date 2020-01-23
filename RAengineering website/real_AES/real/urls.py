from django.contrib import admin
from . import views
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('about/',views.about,name="AboutUs"),
    path('contact/',views.contact,name="ContactUs"),
    path("inquiry/", views.inquiry, name="inquirypage"),
    path("clients/", views.clients, name="clients"),
    path("overview/", views.services_ov, name="overview"),
    path("calibration/", views.calibration, name="calibration"),
    path("Verification/", views.verify, name="verify"),
    path("product/", views.product, name="product")
]
