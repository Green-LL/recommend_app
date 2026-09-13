# forms.py
from django import forms
from .models import Feedback

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['media_type', 'title', 'comment']
        widgets = {
            'media_type': forms.Select(attrs={'class': 'form-select'}),
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '例: 〇〇（作品名）'}),
            'comment': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'おすすめの理由やコメントをどうぞ（任意）'}),
        }