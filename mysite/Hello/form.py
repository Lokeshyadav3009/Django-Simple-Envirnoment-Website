from Hello.models import Feedback
from django import forms


class PostForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ('name', 'email', 'message')

        widgets ={
            'name':forms.TextInput(attrs={ 'placeholder': 'Enter Name','required': True, 'size': 20}),
            'email':forms.TextInput(attrs={ 'placeholder': 'Enter Email', 'maxlength': 10000, 'required': True, 'size': 20}),
            'message':forms.TextInput(attrs={ 'placeholder': 'Enter Message','required': True, 'size': 20}),
       }