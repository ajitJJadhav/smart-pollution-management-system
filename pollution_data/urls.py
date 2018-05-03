from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^getdata/$',views.grab,name="grab_data"),
    url(r'^showdata/$',views.showMap,name="map"),
    url(r'^showCharts/$', views.showCharts, name = "analytics"),
]
