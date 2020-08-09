from django import forms
from .models import Listing


class listingForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = ('title', 'description', 'price', 'imgURL', 'category')
        labels = {'title': 'Title',
                  'description': 'Clear Description of the Product',
                  'price': 'Price ($)',
                  'imgURL': 'Image Link',
                  'category': 'Choose Category'
                  }
