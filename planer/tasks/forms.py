from .models import Tasks
from django import forms


class TaskForm(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = ['title', 'task']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Title'
            }),
            'task': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Task'
            })
        }


class TaskFormChange(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = ['title', 'task']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Title',
            }),
            'task': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Task',
            })
        }

    def __init__(self, *args, **kwargs):
        super(TaskFormChange, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs['value'] = kwargs['instance'].title
        self.fields['task'].widget.attrs['placeholder'] = kwargs['instance'].task
