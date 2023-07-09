from django import forms
from cyclist.models import Cyclist


class cyclistform(forms.ModelForm):
    class meta:
        model=Cyclist
        fields="__all__"