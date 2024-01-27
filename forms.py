# from django import forms
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User

# class signupform(UserCreationForm):
#     pseudo = forms.CharField(max_length=100)
#     password = forms.CharField(max_length=100)

#     class meta:
#         model = User
#         fields = ('username','password1', 'password2', 'pseudo'  'password')
    
#     def save(self,commit=True):
#         user = super(signupform,self).save(commit=False)
#         user.pseudo = self.cleaned_data['pseudo']
#         user.password = self.cleaned_data['password']

#         if commit:
#             user.save()
#         return user

