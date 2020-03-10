
from django.urls import path, include
from estado.views import Estadoview,Estadoinsertar,Estadoeditar,Estadoeliminar,Partecuerpoview,Partecuerpoinsertar,Partecuerpoeditar,Partecuerpoeliminar,Detallecuerpoview,Detallecuerpoinsertar,Detallecuerpoeditar,Detallecuerpoeliminar,Demonioview,Demonioinsertar,Demonioeditar,Demonioeliminar,Batallaview,Batallainsertar,Batallaeditar,Batallaeliminar


urlpatterns = [
    path('Estado', Estadoview.as_view(), name='Estados'),
    path('Estado/new', Estadoinsertar.as_view(), name='AgregarE'),
    path('Estado/edit/<int:pk>', Estadoeditar.as_view(), name='EditarE'),
    path('Estado/delete/<int:pk>', Estadoeliminar.as_view(), name='EliminarE'),

    path('Partecuerpo', Partecuerpoview.as_view(), name='Partecuerpos'),
    path('Partecuerpo/new', Partecuerpoinsertar.as_view(), name='AgregarP'),
    path('Partecuerpo/edit/<int:pk>', Partecuerpoeditar.as_view(), name='EditarP'),
    path('Partecuerpo/delete/<int:pk>', Partecuerpoeliminar.as_view(), name='EliminarP'),

    path('Detallecuerpo', Detallecuerpoview.as_view(), name='Detallecuerpos'),
    path('Detallecuerpo/new', Detallecuerpoinsertar.as_view(), name='AgregarDC'),
    path('Detallecuerpo/edit/<int:pk>', Detallecuerpoeditar.as_view(), name='EditarDC'),
    path('Detallecuerpo/delete/<int:pk>', Detallecuerpoeliminar.as_view(), name='EliminarDC'),

    path('', Batallaview.as_view(), name='Batallas'),
    path('Batalla/new', Batallainsertar.as_view(), name='AgregarB'),
    path('Batalla/edit/<int:pk>', Batallaeditar.as_view(), name='EditarB'),
    path('Batalla/delete/<int:pk>', Batallaeliminar.as_view(), name='EliminarB'),

    path('Demonio', Demonioview.as_view(), name='Demonios'),
    path('Demonio/new', Demonioinsertar.as_view(), name='AgregarD'),
    path('Demonio/edit/<int:pk>', Demonioeditar.as_view(), name='EditarD'),
    path('Demonio/delete/<int:pk>', Demonioeliminar.as_view(), name='EliminarD'),
  ]
