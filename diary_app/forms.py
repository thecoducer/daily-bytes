from django.forms import ModelForm
from diary_app.models import Entry

class EntryForm(ModelForm):
    class Meta: # Meta class is for attach additional information
        model = Entry 
        fields = ('text', )

        # below is done in ModelForm
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['text'].widget.attrs.update({'class': 'textarea', 'placeholder': 'What\'s on your mind?'})