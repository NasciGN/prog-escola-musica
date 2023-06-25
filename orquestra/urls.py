from django.urls import path
from orquestra import views

app_name = 'orquestra'

urlpatterns = [
    path('listar/', views.OrquestraListView.as_view(), name='read'),
    path('criar/', views.OrquestraCreateView.as_view(), name='create'),
    path('editar/<int:pk>/', views.OrquestraUpdateView.as_view(), name='update'),
    path('excluir/<int:pk>/', views.OrquestraDeleteView.as_view(), name='delete'),
]