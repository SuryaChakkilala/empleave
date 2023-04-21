from django.urls import path
from .views import home, loginPage, logoutUser, register_users, vacation_form, thanks_page

urlpatterns = [
    path('', home, name='home'),    
    path('login', loginPage, name='login'),
    path('logout', logoutUser, name='logout'),
    path('register_users', register_users, name='reg_users'),
    path('vacation_form', vacation_form, name='vacation_form'),
    path('thanks_page', thanks_page, name='thanks_page')
]
