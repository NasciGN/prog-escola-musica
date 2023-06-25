from django.urls import path
from .views import SinfoniaListView

app_name = 'sinfonia'

urlpatterns = [
    path('', SinfoniaListView.as_view(), name='read'),
]