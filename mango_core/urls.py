from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
from tastypie.api import Api

from src.views import HomePage
from src.api import AnimalResource, UserResource

animal_resource = AnimalResource()

v1_api = Api(api_name='v1')
v1_api.register(UserResource())
v1_api.register(AnimalResource())

urlpatterns = [
    url(r'^$', HomePage.as_view(), name="homepage"),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(v1_api.urls)),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns.append(
        url(r'^__debug__/', include(debug_toolbar.urls)),
    )
