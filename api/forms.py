from django import forms


class myForm(forms.Form):
   Input_Json=forms.JSONField()