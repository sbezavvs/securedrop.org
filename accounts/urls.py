from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from accounts.views import DashboardView, UpdateUserForm, SecuredropEditView

urlpatterns = [
    url(r'^dashboard$', DashboardView.as_view(), name='dashboard'),
    url(r'^change_name/(?P<pk>[-\w]+)/', UpdateUserForm.as_view(), name='account_change_name'),
    url(r'^instances/add/$', SecuredropEditView.as_view(), name='securedroppage_add'),
    url(r'^instances/(?P<slug>[\w-]+)/$', SecuredropEditView.as_view(), name='securedroppage_edit'),
]
