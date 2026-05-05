from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('registo/', views.registo_view, name='registo'),
    path('magic-link/', views.magic_link_request_view, name='magic_link_request'),
    path('magic-link/validate/', views.magic_link_validate_view, name='magic_link_validate'),
]