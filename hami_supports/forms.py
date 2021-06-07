from django import forms
from django.core import validators

class SupportForm(forms.Form):

    project_id = forms.IntegerField(
        widget=forms.HiddenInput(),
        required=False,
        initial=1
    )

    price = forms.FloatField(
        widget=forms.NumberInput(attrs={'placeholder': 'لطفا مبلغ مورد نظر خود را وارد نمایید','class': 'form-control'}),
        label='مبلغ حمایت',
    )
