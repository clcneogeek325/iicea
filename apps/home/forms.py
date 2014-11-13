from django import forms


class alumnoLoginForm(forms.Form):
    no_control = forms.CharField()
    contrasenia = forms.CharField()

        
