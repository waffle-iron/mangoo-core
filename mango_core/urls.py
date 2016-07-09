from django.conf.urls import url, include, patterns
from mango_core_common.views import HomePage
from django.conf import settings

urlpatterns = [
    url(r'^$', HomePage.as_view(), name="homepage"),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += patterns('',
                            url(r'^__debug__/', include(debug_toolbar.urls)),
                            )
