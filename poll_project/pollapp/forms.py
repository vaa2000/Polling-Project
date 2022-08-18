from django import forms
from .models import PollModel

class PollForm(forms.ModelForm):
	class Meta:
		model = PollModel
		fields = ["question", "op1", "op2", "op3"]
		widgets = {"question":forms.Textarea(attrs={'rows':4, 'cols':22, 'style':'resize:none' })}