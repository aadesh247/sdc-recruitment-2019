from django import forms

class ToDoForm(forms.Form):
	content = forms.CharField(max_length = 40,
		widget=forms.TextInput(attrs={'class':"form-control", 'placeholder':'Enter Your Task'} ))