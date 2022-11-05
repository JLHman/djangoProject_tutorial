# INF601 - Advanced Programming in Python
# Jesse Heckman
# Mini Project # 4

from django import forms

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)
