from django import forms
from .models import Car


class CarPostForm(forms.ModelForm):
    class Meta:
        model = Car
        exclude = ['owner', 'is_featured', 'is_approved', 'created_date']
        widgets = {
            'state': forms.Select(attrs={'class': 'form-control'}),
            'year': forms.Select(attrs={'class': 'form-control'}),
            'condition': forms.Select(attrs={'class': 'form-control', 'choices': [('New','New'),('Used','Used')]}),
            'doors': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            if field not in ['features', 'description']:
                self.fields[field].widget.attrs.update({'class': 'form-control'})
