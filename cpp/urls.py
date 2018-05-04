from . import views
from django.urls import path

app_name = 'cpp'
urlpatterns = [
    path('', views.cpp_home, name='cpp_home'),
    path('price-tracking', views.UserPreferenceListView.as_view(), name='userpreference_changelist'),
    path('add/', views.UserPreferenceCreateView.as_view(), name='userpreference_add'),
    path('<int:pk>/', views.UserPreferenceUpdateView.as_view(), name='user_preference_change'),
    path('ajax/load-dropdown/', views.load_dropdown, name='ajax_load_dropdown'),
    path('price-prediction', views.UserPreferenceListView.as_view(), name='price_prediction'),

]