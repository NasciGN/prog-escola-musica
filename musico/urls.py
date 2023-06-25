from django.urls import path
from musico import views

app_name = 'musico'

urlpatterns = [
    path('listar/', views.MusicoListView.as_view(), name='read'),
    path('criar/', views.MusicoCreateView.as_view(), name='create'),
    path('editar/<int:pk>/', views.MusicoUpdateView.as_view(), name='update'),
    path('excluir/<int:pk>/', views.MusicoDeleteView.as_view(), name='delete'),
]