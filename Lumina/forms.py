from django import forms

class DashboardFilterForm(forms.Form):
    end_year = forms.CharField(required=False)  # Add more filter fields as needed
    topics = forms.CharField(required=False)
    sector = forms.CharField(required=False)
    region = forms.CharField(required=False)
    pest = forms.CharField(required=False)
    source = forms.CharField(required=False)
    swot = forms.CharField(required=False)
    country = forms.CharField(required=False)
    
