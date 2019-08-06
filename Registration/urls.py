from django.conf.urls import include, url
from django.contrib import admin
from signup.views import *
# from django.conf import settings
# from django.conf.urls.static import static

urlpatterns = [
    url(r'^signup/',include('signup.urls', namespace = 'signup')),
    url(r'^admin/', include(admin.site.urls)),

]
