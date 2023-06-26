from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views as view
from django.conf.urls.static import static
from core import views
from escola_de_musica import settings

urlpatterns = [
    path('admin/', admin.site.urls, name='admin:index'),
    path('', views.IndexView.as_view(), name='home'),
    path('sinfonia/', include('sinfonia.urls')),
    path('instrumentos/', include('instrumento.urls')),
    path('orquestras/', include('orquestra.urls')),
    path('apresentacoes/', include('apresentacao.urls')),
    path('musico/', include('musico.urls')),
    path('registrar/', views.registrar, name='registrar'),
    path('login/', views.logar, name='login'),
    path('logout/', view.LogoutView.as_view(next_page='home'), name='logout'),
] 
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
