from django.urls import path
from .views import *

urlpatterns = [
    path('', DvgBaseIndexView.as_view(), name='home'),
    path('whatwedo/', DvgBaseWhatWeDoView.as_view(), name='whatwedo'),
    path('manifesto/', DvgBaseManifestoView.as_view(), name='manifesto'),
    path('joinus/', DvgBaseJoinUsView.as_view(), name='joinus'),
    path('workshop/', DvgBaseWorkShopView.as_view(), name='workshop'),


]
