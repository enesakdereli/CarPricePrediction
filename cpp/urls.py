from . import views
from django.urls import path

app_name = 'cpp'
urlpatterns = [
    path('', views.cpp_home, name='cpp_home'),
    path('price-tracking', views.PricePredictionListView.as_view(), name='userpreference_changelist'),
    path('add/', views.PricePredictionCreateView.as_view(), name='predict_price'),
    path('<int:pk>/', views.PricePredictionUpdateView.as_view(), name='user_preference_change'),
    path('ajax/load-dropdown/', views.load_dropdown, name='ajax_load_dropdown'),
    path('ajax/get-prediction/', views.get_prediction, name='ajax_get_prediction')]
