from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from mysite.core import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.prodt, name='home'),
    path('signup/', views.signup, name='signup'),
    path('secret/', views.secret_page, name='secret'),
    path('secret2/', views.SecretPage.as_view(), name='secret2'),
    path('accounts/', include('django.contrib.auth.urls')),
    path("product/<int:myid>", views.productView, name="product"),
    path('about/',views.about,name="About"),
    path('contact/',views.contact,name="contact"),
    path("request/", views.Request, name="wants"),
    path("order/", views.book, name="order"),
    path("detail/", views.detail, name="detail"),
    path("select/", views.select, name="select"),
    path("checkout/", views.check, name="checkout"),
    path("trend/", views.price, name="trend"),
    path("payment/",views.checoutView, name="payment"), 
    path('accounts/',include('allauth.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
