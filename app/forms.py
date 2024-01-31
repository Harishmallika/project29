from django import forms
from django.core import validators

def validate_for_a(data):
    if data.lower().startswith('a'):
        raise forms.ValidationError('started with a')


    
       

def validate_for_len(data):
    if len(data)<5:
        raise forms.ValidationError('len is < 5')    



class schoolForm(forms.Form):
    sname=forms.CharField(validators=[validate_for_a])
    slocation=forms.CharField(validators=[validate_for_a])
    sprincipal=forms.CharField()
    email=forms.EmailField()
    renteremail=forms.EmailField()


    def clean(self):
        e=self.cleaned_data['email']
        re=self.cleaned_data['renteremail']
        if e!=re:
            raise forms.ValidationError('emails not matched')

