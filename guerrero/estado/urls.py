
from django.urls import path, include
from estado.views import Estadoview,Estadoinsertar,Estadoeditar,Estadoeliminar,Partecuerpoview,Partecuerpoinsertar,Partecuerpoeditar,Partecuerpoeliminar,Detallecuerpoview,Detallecuerpoinsertar,Detallecuerpoeditar,Detallecuerpoeliminar,Demonioview,Demonioinsertar,Demonioeditar,Demonioeliminar,Batallaview,Batallainsertar,Batallaeditar,Batallaeliminar

urlpatterns = [
    path('', Estadoview.as_view(), name='Estados'),
    path('Estado/new', Estadoinsertar.as_view(), name='Agregar'),
    path('Estado/edit/<int:pk>', Estadoeditar.as_view(), name='Editar'),
    path('Estado/delete/<int:pk>', Estadoeliminar.as_view(), name='Eliminar'),

    path('Partecuerpo/', Partecuerpoview.as_view(), name='Partecuerpos'),
    path('Partecuerpo/new', Partecuerpoinsertar.as_view(), name='Agregar'),
    path('Partecuerpo/edit/<int:pk>', Partecuerpoeditar.as_view(), name='Editar'),
    path('Partecuerpo/delete/<int:pk>', Partecuerpoeliminar.as_view(), name='Eliminar'),

    path('Detallecuerpo/', Detallecuerpoview.as_view(), name='Detallecuerpos'),
    path('Detallecuerpo/new', Detallecuerpoinsertar.as_view(), name='Agregar'),
    path('Detallecuerpo/edit/<int:pk>', Detallecuerpoeditar.as_view(), name='Editar'),
    path('Detallecuerpo/delete/<int:pk>', Detallecuerpoeliminar.as_view(), name='Eliminar'),

    path('Batalla/', Demonioview.as_view(), name='Batallas'),
    path('Batalla/new', Demonioinsertar.as_view(), name='Agregar'),
    path('Batalla/edit/<int:pk>', Demonioeditar.as_view(), name='Editar'),
    path('Batalla/delete/<int:pk>', Demonioeliminar.as_view(), name='Eliminar'),
  ]
