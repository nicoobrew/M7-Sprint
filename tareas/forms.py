from django import forms
from .models import Etiqueta, Tarea, User, Prioridad

class TareaForm(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = ['titulo', 'descripcion', 'fecha_vencimiento', 'estado', 'etiqueta', 'usuario_asignado', 'prioridad']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['usuario_asignado'].queryset = User.objects.all()
        
class FiltroTareasForm(forms.Form):
    etiqueta = forms.ModelChoiceField(
        queryset=Etiqueta.objects.all(),
        empty_label='Todas las etiquetas',
        required=False
    )
    
    estado = forms.ChoiceField(
        choices=[('', 'Todos los estados')] + list(Tarea.ESTADOS),  
        required=False
    )
    
    prioridad = forms.ChoiceField(
        choices=[('', 'Todas las prioridades')] + list(Prioridad.NIVELES),  
        required=False
    )
