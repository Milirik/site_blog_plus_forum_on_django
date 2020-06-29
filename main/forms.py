from django import forms
from .models import Feedback
from captcha.fields import CaptchaField

class FeedbackForm(forms.ModelForm):
	captcha = CaptchaField(label='Введите текст с картинки',
							error_messages={'invalid': 'Wrong captcha'})

	class Meta:
		model = Feedback
		fields = "__all__"

class SearchForm(forms.Form):
	search = forms.CharField(required=False, max_length=20, label='Ключевое слово')