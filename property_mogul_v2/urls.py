"""property_mogul_v2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from members import views as members_views
from home import views as home_views
from paypal.standard.ipn import urls as paypal_urls
from paypal_store import views as paypal_views
from .settings import MEDIA_ROOT
from products import views as product_views
from houses import views as house_views
from django.views.static import serve


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home_views.get_index, name='index'),
    url(r'^register/$', members_views.register, name='register'),
    url(r'^profile/$', members_views.profile, name='profile'),
    url(r'^login/$', members_views.login, name='login'),
    url(r'^logout/$', members_views.logout, name='logout'),
    url(r'^cancel_subscription/$', members_views.cancel_subscription, name='cancel_subscription'),
    url(r'^cancelled/$', members_views.cancel, name='cancel'),
    url(r'^subscriptions_webhook/$', members_views.subscriptions_webhook, name='subscriptions_webhook'),
    url(r'^a-really-hard-to-guess-url/', include(paypal_urls)),
    url(r'^paypal-return', paypal_views.paypal_return),
    url(r'^paypal-cancel', paypal_views.paypal_cancel),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),
    url(r'^products/$', product_views.all_products),
    url(r'^houses/$', house_views.all_houses),
]
