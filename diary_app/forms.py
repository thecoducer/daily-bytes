from django.forms import ModelForm
from diary_app.models import Entry
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class EntryForm(ModelForm):
    class Meta: # Meta class is for attach additional information
        model = Entry 
        fields = ('title', 'text', )

        # below is done in ModelForm
    """ def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': 'input is-medium', 'placeholder': 'Enter a title'})
        self.fields['text'].widget.attrs.update({'class': 'textarea', 'id': 'add_textarea', 'placeholder': 'Write here'}) """


class UserForm(UserCreationForm):
    class Meta:
        model = User 
        fields = ('email', 'username', 'password1', 'password2')

