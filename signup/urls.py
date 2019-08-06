from django.conf.urls import url, include
#from django.core.urlresolvers import reverse_lazy
from django.views.generic import RedirectView
from . import views

urlpatterns=[
    url(r'signup/$',views.signup, name = 'signup'),
    url(r'login/$',views.login, name='login'),
    url(r'logout/$',views.logout, name = 'logout'),
]
