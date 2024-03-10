from django.forms import ModelForm

from .models import Property


class PropertyForm(ModelForm):
    class Meta:
        model = Property
        fields = (
            'title',
            'description',
            'price_per_night',
            'bedrooms',
            'bathrooms',
            'guests',
            'country',
            'country_code',
            'category',
            'image',
        )