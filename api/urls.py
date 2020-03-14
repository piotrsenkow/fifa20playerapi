from django.urls import path, include
from .views import GkRetrieveView

urlpatterns = [
    path('gk/<int:sofifa_id>/', GkRetrieveView.as_view())
]