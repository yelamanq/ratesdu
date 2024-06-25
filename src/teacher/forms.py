from .models import Comment
from django import forms
import datetime

class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

        widgets = {
            'content': forms.Textarea(attrs={'class': 'input', 'placeholder': 'Write comment'}),
        }

    def save(self, user_id=None, teacher_id=None, commit=True):
        instance = super().save(commit=False)

        instance.user_id = user_id
        instance.teacher_id = teacher_id
        instance.date = datetime.datetime.now()
        instance.block = False

        if commit:
            instance.save()
        return instance

