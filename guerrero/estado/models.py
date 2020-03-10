from django.db import models


# modelo de estado

class Estado(models.Model):
    EstadoNombre = models.CharField(
       max_length = 50,
       )
    def __str__(self):
        return '{}'.format(self.EstadoNombre)
    def save(self):
        self.EstadoNombre = self.EstadoNombre.upper()
        super(Estado,self).save()
class Meta:
    verbose_name_plural='Articulos'


#modelo del parte de cuerpo

class Partecuerpo(models.Model):
    CuerpoNombre = models.CharField(
        max_length = 50,
    )
    def __str__(self):
        return '{}'.format(self.CuerpoNombre)
    def save(self):
        self.CuerpoNombre= self.CuerpoNombre.upper()
        super(Partecuerpo,self).save()
class Meta:
    verbose_name_plural='Partes del ceurpo'


#modelo de los detalles del cuerpo

class Detallecuerpo(models.Model):
    partecuerpo=models.ForeignKey(Partecuerpo, on_delete=models.CASCADE)
    estado=models.ForeignKey(Estado, on_delete=models.CASCADE)
    def __str__(self):
        return 'EL DEMONIO {} ESTA PARTE DEL CUERPO : {}  '.format(self.estado.EstadoNombre ,self.partecuerpo.CuerpoNombre )
    def save(self):
        super(Detallecuerpo,self).save()
class Meta:
    verbose_name_plural='Detalles del cuerpo'


#modelo del Demonio

class Demonio(models.Model):
    DemonioNombre = models.CharField(
        max_length = 50,
    )
    detallecuerpo=models.ForeignKey(Detallecuerpo, on_delete=models.CASCADE)
    def __str__(self):
        return '{}'.format(self.DemonioNombre)
    def save(self):
        self.DemonioNombre= self.DemonioNombre.upper()
        super(Demonio,self).save()
class Meta:
    verbose_name_plural='Demonios'


#modelo de batalla

class Batalla(models.Model):
    demonio=models.ForeignKey(Demonio, on_delete=models.CASCADE)
    estado=models.ForeignKey(Estado, on_delete=models.CASCADE)
    def __str__(self):
        return '{}:{}'.format(self.demonio.DemonioNombre, self.estado.EstadoNombre)
    def save(self):
        super(Batalla,self).save()
class Meta:
    verbose_name_plural='batallas'
