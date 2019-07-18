from django.urls.conf import include
from django.contrib import admin
from django.url import path


urlpatterns=[
    #inclui as URLs do app 'website'
    path('',include('website.urls',namespace='website')),

    #interface administrativa
    path('admin/', admin.site.urls),

]
