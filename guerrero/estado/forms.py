from django import forms
from estado.models import Estado,Partecuerpo,Detallecuerpo,Demonio,Batalla


# formulario de estado

class Estadoform(forms.ModelForm):
    class Meta:
        model = Estado
        fields = ['EstadoNombre']
        labels = {'Estado ' : 'ingrese el  nombre'}
        widget={'EstadoNombre' : forms.TextInput()}

    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'})


#formulario de partecuerpo

class Partecuerpoform(forms.ModelForm):
    class Meta:
        model = Partecuerpo
        fields = ['CuerpoNombre']
        labels = {'parte del cuerpo ' : 'ingrese el  nombre'}
        widget={'CuerpoNombre' : forms.TextInput()}
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'})


#formulario  los detalles del cuerpo

class Detallecuerpoform(forms.ModelForm):
    class Meta:
        model = Detallecuerpo
        fields = ['partecuerpo','estado']
        labels = {'parte del cuerpo' : 'escoja el  nombre',
                   'estado':'escoja el  nombre' }
        widget={'partecuerpo' : forms.TextInput(),
                'estado' : forms.TextInput()
               }
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'})


#formulario  los Demonios

class Demonioform(forms.ModelForm):
    class Meta:
        model = Demonio
        fields = ['DemonioNombre','detallecuerpo']
        labels = {'Nombre del demonio' : 'ingrese el  nombre',
                  'detallecuerpo':'escoja la parte del cuerpo' }
        widget={'DemonioNombre' : forms.TextInput(),
                'detallecuerpo' : forms.TextInput()
               }
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'})


#formulario  los Demonios

class Batallaform(forms.ModelForm):
    class Meta:
        model = Batalla
        fields = ['demonio','estado']
        labels = {'Nombre del demonio' : 'escoja el demonio',
                  'estado':'escoja el estado' }
        widget={'demonio' : forms.TextInput(),
                'estado' : forms.TextInput()
               }
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'})
