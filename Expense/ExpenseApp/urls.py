from django.conf.urls import url
from .views import *

urlpatterns =[

url(r'^$', index, name='index'),

url(r'^display_Farhan$', display_Farhan, name='display_Farhan'),
url(r'^display_Nadia$', display_Nadia, name='display_Nadia'),
url(r'^display_FarhanFamily$', display_FarhanFamily, name='display_FarhanFamily'),
url(r'^display_Ongie$', display_Ongie, name='display_Ongie'),
url(r'^display_Orange$', display_Orange, name='display_Orange'),

url(r'^add_Farhan$', add_Farhan, name='add_Farhan'),
url(r'^add_Nadia$', add_Nadia, name='add_Nadia'),
url(r'^add_FarhanFamily$', add_FarhanFamily, name='add_FarhanFamily'),
url(r'^add_Ongie$', add_Ongie, name='add_Ongie'),
url(r'^add_Orange$', add_Orange, name='add_Orange'),

url(r'^Farhan/edit_item/(?P<pk>\d+)$', edit_Farhan, name="edit_Farhan"),
url(r'^Nadia/edit_item/(?P<pk>\d+)$', edit_Nadia, name="edit_Nadia"),
url(r'^FarhanFamily/edit_item/(?P<pk>\d+)$', edit_FarhanFamily, name="edit_FarhanFamily"),
url(r'^Ongie/edit_item/(?P<pk>\d+)$', edit_Ongie, name="edit_Ongie"),
url(r'^OrangeTrust/edit_item/(?P<pk>\d+)$', edit_Orange, name="edit_Orange"),

url(r'^Farhan/delete_item/(?P<pk>\d+)$', delete_Farhan, name="delete_Farhan"),
url(r'^Nadia/delete_item/(?P<pk>\d+)$', delete_Nadia, name="delete_Nadia"),
url(r'^FarhanFamily/delete_item/(?P<pk>\d+)$', delete_FarhanFamily, name="delete_FarhanFamily"),
url(r'^Ongie/delete_item/(?P<pk>\d+)$', delete_Ongie, name="delete_Ongie"),
url(r'^Orange/delete_item/(?P<pk>\d+)$', delete_Orange, name="delete_Orange"),


]