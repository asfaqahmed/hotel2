from django.conf.urls import url
from HotelApp import views
from Authorize import views

app_name = 'Authorize'
urlpatterns = [
         url(r'^$', views.displayDash, name='displayDash'),
         url(r'^admindash$', views.displayAdminDash, name='admindash'),
         url(r'^admindash/proposals$', views.showProposals, name='showproposals'),
         url(r'^admindash/partners$', views.showPartners, name='showpartners'),
         url(r'^admindash/partners/(?P<id>[0-9]+)/remove$', views.removePartner, name='removepartner'),
         url(r'^admindash/proposals/(?P<id>[0-9]+)/accept$', views.acceptProposals, name='acceptproposal'),
]
