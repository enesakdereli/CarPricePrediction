from . import views
from django.urls import path
from django.contrib.auth.decorators import login_required
app_name = 'cpp'
urlpatterns = [
    path('', views.cpp_home, name='cpp_home'),
    path('predict/', views.PricePredictionCreateView.as_view(), name='predict_price'),
    path('ajax/load-dropdown/', views.load_dropdown, name='ajax_load_dropdown'),
    path('ajax/get-prediction/', views.get_prediction, name='ajax_get_prediction'),
    path('price-tracking/', login_required(views.PriceTrackingListView.as_view()), name='price_tracking_changelist'),
    path('price-tracking/add/', login_required(views.add_tracking), name='price_tracking_add'),
    path('price-tracking/<int:pk>/', login_required(views.PriceTrackingUpdateView.as_view()), name='price_tracking_change'),
    path('price-tracking/delete/<int:pk>', login_required(views.PriceTrackingDelete.as_view()), name='price_tracking_delete'),

]
