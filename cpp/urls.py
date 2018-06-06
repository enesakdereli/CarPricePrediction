from . import views
from django.urls import path

app_name = 'cpp'
urlpatterns = [
    path('', views.cpp_home, name='cpp_home'),
    path('predict/', views.PricePredictionCreateView.as_view(), name='predict_price'),
    path('<int:pk>/', views.PricePredictionUpdateView.as_view(), name='price_prediction_change'),
    path('ajax/load-dropdown/', views.load_dropdown, name='ajax_load_dropdown'),
    path('ajax/get-prediction/', views.get_prediction, name='ajax_get_prediction'),
    path('price-tracking/', views.PriceTrackingListView.as_view(), name='price_tracking_changelist'),
    path('price-tracking/add/', views.PriceTrackingCreateView.as_view(), name='price_tracking_add'),
]
