from .models import Tickets
from django.forms import ModelForm, TextInput, Textarea, forms


class TicketForm(ModelForm):
    class Meta:
        model = Tickets
        fields = ('title', 'description', 'category')
        labels = {
            'title': 'Title',
            'description': 'Description',
            'category': 'Category'
        }

    def __init__(self, *args, **kwargs):
        super(TicketForm,self).__init__(*args, **kwargs)
        self.fields['category'].empty_label= "Select"