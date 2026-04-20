from django.urls import path
from . import views
from .views import ev_tahmin

urlpatterns = [
    path('', ev_tahmin),
    ##path('predict/', views.predict),
]