from django.test import TestCase

# Create your tests here.
   url(r'^new-user/$', UserRegistrationView.as_view(), name='user_registration'),
   url(r'^login/$', login, {'template_name': 'login.html'},name='login'),
   url(r'^logout/$', logout, {'next_page': '/login/'}, name='logout'),

    