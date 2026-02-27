from django.urls import path
from .views import main_page, register_page, login_page, profil_page, contacts_page, about_uss_page

urlpatterns = [
    path('', main_page, name="main_page"),
    path('login/', login_page, name="login_page"),
    path('register/', register_page, name="register_page"),
    path('profil/', profil_page, name="profil_page"),
    path('contacts/', contacts_page, name="contacts_page"),
    path('about/', about_uss_page, name="about_uss_page")
]
