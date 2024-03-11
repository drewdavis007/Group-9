from django import forms
from .models import Item


INPUT_CLASSES = 'w-full py-4 rounded-xl border'

class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('category', 'name', 'description', 'price', 'image')

        widgets = {
            'category': forms.Select(attrs={
                'class': INPUT_CLASSES,
                'placeholder': 'Choose category',
            }),
            'name': forms.TextInput(attrs={
                'class': INPUT_CLASSES,
                'placeholder': 'Enter name of item'
            }),
            'description': forms.Textarea(attrs={
                'class': INPUT_CLASSES,
                'placeholder': 'Enter item description'
            }),
            'price': forms.TextInput(attrs={
                'class': INPUT_CLASSES,
                'placeholder': 'Enter item price'
            }),
            'image': forms.FileInput(attrs={
                'class': INPUT_CLASSES,
                'placeholder': 'attach item image'
            })
        }


class EditItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('name', 'description', 'price', 'image', 'is_sold')

        widgets = {
            'name': forms.TextInput(attrs={
                'class': INPUT_CLASSES,
                'placeholder': 'Enter name of item'
            }),
            'description': forms.Textarea(attrs={
                'class': INPUT_CLASSES,
                'placeholder': 'Enter item description'
            }),
            'price': forms.TextInput(attrs={
                'class': INPUT_CLASSES,
                'placeholder': 'Enter item price'
            }),
            'image': forms.FileInput(attrs={
                'class': INPUT_CLASSES,
                'placeholder': 'attach item image'
            })
        }