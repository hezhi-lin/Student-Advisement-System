from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView
from django.contrib.auth.views import login

from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^myapp/',include('myproject.myapp.urls')),
    url(r'^$', RedirectView.as_view(url='/myapp/home/', permanent=True)),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', login, {'template_name': 'admin/login.html'})
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
