from django.conf.urls import url 
from pizza import views 
from rest_framework import routers

router = routers.DefaultRouter()

urlpatterns = [ 
    url(r'^pizza/create', views.create_pizza),
    url(r'^pizza/list$', views.list_pizza),
    url(r'^pizza/edit/(?P<pk>[0-9]+)$', views.edit_pizza),
    url(r'^pizza/delete/(?P<pk>[0-9]+)$', views.delete_pizza),
]