from django.urls import path
from django.conf import settings
from tracking import views

urlpatterns = [
    path('refresh/', views.update_active_users, name='tracking-refresh-active-users'),
    path('refresh/json/', views.get_active_users, name='tracking-get-active-users'),
]

if getattr(settings, 'TRACKING_USE_GEOIP', False):
    urlpatterns += [
        path('map/', views.display_map, name='tracking-visitor-map'),
    ]
