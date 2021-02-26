from django import forms

class UrlInputForm(forms.Form):
	video_url = forms.CharField(widget=forms.TextInput(attrs={'class': 'url-inputbox', 'placeholder': "https://www.youtube.com/watch?v=cbq30NoJGV0", "onfocus": "this.placeholder = ''", 'onblur':"this.placeholder = 'https://www.youtube.com/watch?v=cbq30NoJGV0'", 'autocomplete':"off", 'value':''}))