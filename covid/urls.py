from django.urls import path

from covid.api.home import CovidHomeAPIView

urlpatterns = [
    path('', CovidHomeAPIView.as_view(), name='covid home'),

]
