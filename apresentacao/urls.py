from django.urls import path
from apresentacao import views

app_name = 'apresentacao'

urlpatterns = [
    path('listar/', views.ApresentacaoListView.as_view(), name='read'),
    path('criar/', views.ApresentacaoCreateView.as_view(), name='create'),
    path('editar/<int:pk>/', views.ApresentacaoUpdateView.as_view(), name='update'),
    path('excluir/<int:pk>/', views.ApresentacaoDeleteView.as_view(), name='delete'),
]