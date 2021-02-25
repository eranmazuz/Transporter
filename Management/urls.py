from django.urls import path

from . import views

urlpatterns = [
    #path('', views.upload, name='index'),
    path('routes/', views.RouteListView.as_view(), name='route_list'),
    path('routes/<int:pk>/update', views.edit_route_view, name='edit_route'),
    path('routes/<int:pk>/delete', views.RouteDeleteView.as_view(), name='route_delete'),
    path('routes/create/', views.create_route_view, name='create_route'),
    path('a3/', views.create_route_with_stations, name='a3'),
    path('a3/<int:pk>/', views.create_route_with_stations, name='a333'),

]
