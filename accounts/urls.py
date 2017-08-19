from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView
from .views import UserRegistrationView
from django.contrib.auth.views import login, logout

urlpatterns = [
    url(r'^new-user/$', UserRegistrationView.as_view(), name='user_registration'),
    url(r'^login/$', login, {'template_name': 'login.html'},name='login'),
    url(r'^logout/$', logout, {'next_page': '/login/'}, name='logout'),

]

