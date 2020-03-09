
from django.urls import path, include
from celda.views import ,Estadoview,Estadoinsertar,Estadoeditar,Estadoeliminar,Partecuerpoview,Partecuerpoinsertar,Partecuerpoeditar,Partecuerpoeliminar,Detallecuerpoview,Detallecuerpoinsertar,Detallecuerpoeditar,Detallecuerpoeliminar,Demonioview,Demonioinsertar,Demonioeditar,Demonioeliminar,Batallaview,Batallainsertar,Batallaeditar,Batallaeliminar
    path('', CeldaView.as_view(), name='Celdas'),
    path('Celda/new', CeldaInsertar.as_view(), name='Agregar'),
    path('Celda/edit/<int:pk>', CeldaEditar.as_view(), name='Editar'),
    path('Celda/delete/<int:pk>', CeldaEliminar.as_view(), name='Eliminar'),
  ]
