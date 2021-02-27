
from django.urls import path

from Management import views

urlpatterns = [
    #path('', views.upload, name='index'),
    path('settings/', views.settings_view, name='settings'),
    path('upload/', views.upload_view, name='upload'),
    path('transporters/', views.set_station_transporters_view, name='set_station_transporters'),
    path('transporters/stations', views.set_station_transporters_view, name='set_station_transporters'),
    path('routes/', views.RouteListView.as_view(), name='route_list'),
    path('routes/create/', views.RouteCreateView.as_view(), name='route_create'),
    path('routes/<int:pk>/', views.RouteUpdateView.as_view(), name='route_update'),
    path('routes/<int:pk>/delete/', views.RouteDeleteView.as_view(), name='route_delete'),

    path('cities/', views.city_for_station_view, name='city_for_station')

]
