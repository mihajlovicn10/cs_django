from django import forms
from . import models 



class SupportForm(forms.Form): 
    name = forms.CharField(required=True , max_length= 50, widget=forms.TextInput(attrs={'placeholder': 'Name', 'style': 'width: 300px;', 'class': 'form-control'}))
    phone_number = forms.CharField(max_length=30 , required= False, widget=forms.TextInput(attrs={'placeholder': 'Phone number', 'style': 'width: 300px;', 'class': 'form-control'}))
    company = forms.CharField(max_length=100, required=False , widget=forms.TextInput(attrs={'placeholder': 'Company', 'style': 'width: 300px;', 'class': 'form-control'}))
    email = forms.EmailField(max_length=50, required= True, widget=forms.EmailInput(attrs={'placeholder': 'Email', 'style': 'width: 300px;', 'class': 'form-control'}))
    subject = forms.CharField(max_length=50, required= True,widget=forms.TextInput(attrs={'placeholder': 'Subject', 'style': 'width: 300px;', 'class': 'form-control'}))
    problem_desc = forms.CharField(max_length=1000,widget=forms.Textarea(attrs={"rows":5, "cols":20, 'placeholder': 'Description', 'style': 'width: 300px;', 'class': 'form-control'}), required=False)
    date_and_time = forms.DateField(required= False, widget=forms.DateTimeInput(attrs={'style': 'width: 300px;', 'class': 'form-control datetimepicker-input'}))
    


