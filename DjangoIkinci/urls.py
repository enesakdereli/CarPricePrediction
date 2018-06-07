from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.urls import path
from cpp import views as core_views


urlpatterns = [
    url(r'^$', core_views.home, name='home'),
    url(r'^cpp/', include('cpp.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': 'login'}, name='logout'),
    url(r'^signup/$', core_views.signup, name='signup'),
    url(r'^index/$', core_views.index),



]
