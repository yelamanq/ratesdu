from .models import Message
from django import forms
import datetime

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['title', 'content']

        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Title', 'style': 'display: block; width: 100%; padding: 15px 10px 13px 15px; border: 1px solid #DBDCE1; border-radius: 5px; box-sizing: border-box; font-size: 17px; color: #6D6C6C; margin-top: 5px; transition: 0.2s; font-family: Arial; margin-bottom: 20px'}),
            'content': forms.Textarea(attrs={'class': 'input', 'placeholder': 'Message text'}),
        }

    def save(self, teacher=None, lesson=None, commit=True):
        instance = super().save(commit=False)

        instance.date = datetime.datetime.now()
        instance.teacher = teacher
        instance.lesson = lesson

        if commit:
            instance.save()
        return instance

