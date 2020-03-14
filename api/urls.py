from django.urls import path, include
from .views import GkRetrieveView, CamRetrieveView, CbRetrieveView, CdmRetrieveView, CfRetrieveView, CmRetrieveView, LbRetrieveView, LmRetrieveView, LwRetrieveView, LwbRetrieveView, RbRetrieveView, RmRetrieveView, RwRetrieveView, RwbRetrieveView, StRetrieveView

urlpatterns = [
    path('gk/<int:sofifa_id>/', GkRetrieveView.as_view()),
    path('cam/<int:sofifa_id>/', CamRetrieveView.as_view()),
    path('cb/<int:sofifa_id>/', CbRetrieveView.as_view()),
    path('cdm/<int:sofifa_id>/', CdmRetrieveView.as_view()),
    path('cf/<int:sofifa_id>/', CfRetrieveView.as_view()),
    path('cm/<int:sofifa_id>/', CmRetrieveView.as_view()),
    path('lb/<int:sofifa_id>/', LbRetrieveView.as_view()),
    path('lm/<int:sofifa_id>/', LmRetrieveView.as_view()),
    path('lw/<int:sofifa_id>/', LwRetrieveView.as_view()),
    path('lwb/<int:sofifa_id>/', LwbRetrieveView.as_view()),
    path('rb/<int:sofifa_id>/', RbRetrieveView.as_view()),
    path('rm/<int:sofifa_id>/', RmRetrieveView.as_view()),
    path('rw/<int:sofifa_id>/', RwRetrieveView.as_view()),
    path('rwb/<int:sofifa_id>/', RwbRetrieveView.as_view()),
    path('st/<int:sofifa_id>/', StRetrieveView.as_view()),

]