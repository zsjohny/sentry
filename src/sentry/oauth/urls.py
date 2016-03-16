from django.conf.urls import patterns, url
from django.contrib import admin

from .views import (
     ConsumerExchangeView
)

admin.autodiscover()

urlpatterns = patterns(
    '',
    url(
        regex=r'^consumer/exchange/',
        view=ConsumerExchangeView.as_view(),
        name='consumer-exchange'
    )

)
