from django.conf.urls import url
from mango_core_common.views import HomePage

urlpatterns = [
    url(r'^$', HomePage.as_view(), name="homepage"),
]
