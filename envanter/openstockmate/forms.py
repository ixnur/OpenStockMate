from django import forms
from .models import StockAlert, Category, Component, Document, DocumentType, PurchaseDetail, Package, StokPage, Supplier

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['title', 'description', 'document_type', 'document']
        widgets = {
            'document_type': forms.Select(attrs={'class': 'form-control'}),
        }

class StockAlertForm(forms.ModelForm):
    class Meta:
        model = StockAlert
        fields = ['component', 'threshold'] 

    def __init__(self, user, *args, **kwargs):
        super(StockAlertForm, self).__init__(*args, **kwargs)
        self.fields['component'].queryset = Component.objects.filter(user=user)  

    def clean_threshold(self):
        threshold = self.cleaned_data['threshold']
        if threshold < 0:
            raise forms.ValidationError("Threshold must be a positive number.")
        return threshold
    
class ComponentForm(forms.ModelForm):
    class Meta:
        model = Component
        fields = ['model', 'description', 'manufacturer', 'category', 'package', 'location', 'stock']

class FeedbackForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea(attrs={'rows': 4, 'cols': 50}), required=True)
