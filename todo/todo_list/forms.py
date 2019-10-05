from django import forms

class ToDoForm(forms.Form):
	content = forms.CharField(max_length = 40)