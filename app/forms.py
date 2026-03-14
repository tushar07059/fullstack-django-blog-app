from django import forms 
from app.models import Comments,subscribe
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CommentForm(forms.ModelForm):
    class Meta:
        model=Comments
        fields={'content'}
        widgets={
            'content':forms.Textarea(attrs={'placeholder':'Type your comment...'}),
           
        }



class SubscribeForm(forms.ModelForm):
    #  labels= {'email': _('')}
    #  email= forms.EmailField(widget=forms.TextInput(attrs={'placeholder':'Enter your email'}))
       
     class Meta:
        model=subscribe
        fields='__all__'
        labels={'email': _('')}
     def __init__(self,*args, **kwargs):
         super().__init__(*args, **kwargs)  
         self.fields['email'].widget.attrs['placeholder'] ='Enter your email'  

class NewUserForm(UserCreationForm):
    email= forms.EmailField(required=True)
    class Meta:
        model=User
        fields=("username","email","password1","password2")

    def __init__(self,*args,**kwrgs):
        super().__init__(*args,**kwrgs)

        self.fields['username'].widget.attrs['placeholder'] ='Enter Username'  
        self.fields['email'].widget.attrs['placeholder'] = 'Enter email'
        self.fields['password1'].widget.attrs['placeholder'] = 'Enter password'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm password'

    def clean_username(self):
        username=self.cleaned_data['username'].lower()
        new=User.objects.filter(username=username)
        if new.count():
            raise forms.ValidationError("User already exist")
        return username
   
    def clean_email(self):
        email=self.cleaned_data['email'].strip()
        new=User.objects.filter(email=email)
        if new.count():
            raise forms.ValidationError("Email already exist")
        return email
    
    def clean_password2(self):
        password1=self.cleaned_data['password1']
        password2=self.cleaned_data['password2']
        if password1 and password2 and password1 !=password2:
            raise forms.ValidationError("Password don't match")
        return password2