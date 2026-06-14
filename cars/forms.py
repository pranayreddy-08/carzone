from django import forms
from .models import Car


CONDITION_CHOICES = [
    ('', '-- Select Condition --'),
    ('New', 'New'),
    ('Used', 'Used'),
    ('Certified Pre-Owned', 'Certified Pre-Owned'),
]


class CarPostForm(forms.ModelForm):
    condition = forms.ChoiceField(
        choices=CONDITION_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Car
        exclude = ['owner', 'is_featured', 'is_approved', 'created_date']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            if field not in ['features', 'description']:
                self.fields[field].widget.attrs.update({'class': 'form-control'})
