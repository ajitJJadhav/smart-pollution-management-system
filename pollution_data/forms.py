from django import forms

class DateForm(forms.Form):
    created_on = forms.DateField(input_formats=('%d-%m-%Y',),widget=forms.widgets.DateInput(format="%d-%m-%Y"))

    class Meta:
        fields = '__all__'
