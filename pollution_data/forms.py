from django import forms

class DateForm(forms.Form):
    created_on = forms.DateField()

    class Meta:
        fields = '__all__'
