from django.urls import path
from instrumento import views

app_name = 'instrumento'

urlpatterns = [
    path('listar/', views.InstrumentoListView.as_view(), name='read'),
    path('criar/', views.InstrumentoCreateView.as_view(), name='create'),
    path('editar/<int:pk>/', views.InstrumentoUpdateView.as_view(), name='update'),
    path('excluir/<int:pk>/', views.InstrumentoDeleteView.as_view(), name='delete'),
]
