from typing import Any
from django import forms
from .models import ComponentDocumentLink, Component, Purchase, StockMovement, LocationType, Manufacturer, Location, LocationType, StockAlert, Category, Component, Document, DocumentType, PurchaseDetail, Package, Supplier
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import CustomUser


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }
        def __init__(self, *args, **kwargs):
            super(CategoryForm, self).__init__(*args, **kwargs)
            self.fields['name'].widget.attrs['placeholder'] = 'Category Name'
            self.fields['description'].widget.attrs['placeholder'] = 'Category Description'
            self.fields['name'].widget.attrs['class'] = 'form-control'
            self.fields['description'].widget.attrs['class'] = 'form-control'
            self.fields['name'].widget.attrs['required'] = True
            self.fields['description'].widget.attrs['required'] = True
            self.fields['name'].widget.attrs['maxlength'] = 50
            self.fields['description'].widget.attrs['maxlength'] = 200
            self.fields['name'].widget.attrs['minlength'] = 2
            self.fields['description'].widget.attrs['minlength'] = 10
            self.fields['name'].widget.attrs['pattern'] = '^[a-zA-Z0-9\s]+$'
            self.fields['description'].widget.attrs['pattern'] = '^[a-zA-Z0-9\s]+$'

##sorun var 

class ComponentForm(forms.ModelForm):
    class Meta:
        model = Component
        fields = ['model', 'description', 'manufacturer', 'category', 'package', 'location', 'stock']
        widgets = {
            'model': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'manufacturer': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'package': forms.Select(attrs={'class': 'form-control'}),
            'location': forms.Select(attrs={'class': 'form-control'}),
            'stock': forms.NumberInput(attrs={'class': 'form-control'}),
        }
        #burdakaldın !

class CustomAuthenticationForm(AuthenticationForm):
    username_email = forms.CharField(max_length=254, required=True, widget=forms.TextInput(attrs={'autofocus': True}))

    class Meta:
        model = CustomUser
        fields = ['username_email', 'password']

class DocumentForm(forms.ModelForm):#kontrol et
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
        widgets = {
            'model': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'manufacturer': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'package': forms.Select(attrs={'class': 'form-control'}),
            'location': forms.Select(attrs={'class': 'form-control'}),
            'stock': forms.NumberInput(attrs={'class': 'form-control'}),
      
        }

class DocumentTypeForm(forms.ModelForm):
    class Meta:
        model = DocumentType
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }

class LocationTypeForm(forms.ModelForm):
    class Meta:
        model = LocationType
        fields = ['name', ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }
class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = ['name', 'location_type', 'parent_id']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'location_type': forms.Select(attrs={'class': 'form-control'}),
            'parent_id': forms.Select(attrs={'class': 'form-control'}),
        }
class ManufacturerForm(forms.ModelForm):
    class Meta:
        model = Manufacturer
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }
#devam et burdan yazmaya 

class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }
        
class StockMovement(forms.ModelForm):
    class Meta:
        model = StockMovement
        fields = ['component', 'quantity', 'source_location', 'destination_location']
        widgets = {
            'component': forms.Select(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            'source_location': forms.Select(attrs={'class': 'form-control'}),
            'destination_location': forms.Select(attrs={'class': 'form-control'}),

        }
        def __init__(self, user, *args, **kwargs):
            super(StockMovement, self).__init__(*args, **kwargs)
            self.fields['component'].queryset = Component.objects.filter(user=user)
            self.fields['source_location'].queryset = Location.objects.filter(user=user)


class PackageForm(forms.ModelForm):
    class Meta:
        model = Package
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }
        def __init__(self, user, *args, **kwargs):
            super(PackageForm, self).__init__(*args, **kwargs)
            self.fields['name'].queryset = Package.objects.filter(user=user)
            self.fields['description'].queryset = Package.objects.filter(user=user)
            self.fields['name'].widget.attrs['class'] = 'form-control'
            self.fields['description'].widget.attrs['class'] = 'form-control'
            

class PurchaseDetailForm(forms.ModelForm):
    class Meta:
        model = PurchaseDetail
        fields = ['purchase', 'component', 'quantity']
        widgets = {
            'purchase': forms.Select(attrs={'class': 'form-control'}),
            'component': forms.Select(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            'total_cost': forms.NumberInput(attrs={'class': 'form-control'}),
        }
        def __init__(self, user, *args, **kwargs):
            super(PurchaseDetailForm, self).__init__(*args, **kwargs)
            self.fields['component'].queryset = Component.objects.filter(user=user)
            self.fields['purchase'].queryset = Purchase.objects.filter(user=user)
            self.fields['component'].widget.attrs['class'] = 'form-control'
            self.fields['purchase'].widget.attrs['class'] = 'form-control'
            self.fields['quantity'].widget.attrs['class'] = 'form-control'
            self.fields['total_cost'].widget.attrs['class'] = 'form-control'

class PurchaseForm(forms.Form):
    supplier = forms.ModelChoiceField(queryset=Supplier.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    date = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control'}))

    

class FeedbackForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea(attrs={'rows': 4, 'cols': 50}), required=True)


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=50, required=True)
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=50, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)
    password_repeat = forms.CharField(widget=forms.PasswordInput, required=True)

class LoginForm(forms.Form):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
        }
        def __init__(self, *args, **kwargs):
            super(LoginForm, self).__init__(*args, **kwargs)
            self.fields['username'].widget.attrs['class'] = 'form-control'
            self.fields['email'].widget.attrs['class'] = 'form-control'
            self.fields['password'].widget.attrs['class'] = 'form-control'
            self.fields['password_repeat'].widget.attrs['class'] = 'form-control'
            self.fields['password_repeat'].widget.attrs['placeholder'] = 'Şifre Tekrar'
            self.fields['password_repeat'].widget.attrs['required'] = 'required'
            self.fields['password'].widget.attrs['placeholder'] = 'Şifre'
            self.fields['password'].widget.attrs['required'] = 'required'
            self.fields['username'].widget.attrs['placeholder'] = 'Kullanıcı Adı'
            self.fields['username'].widget.attrs['required'] = 'required'
            self.fields['email'].widget.attrs['placeholder'] = 'E-posta'

class ComponentDocumentLinkForm(forms.Form):
    class Meta:
        model = ComponentDocumentLink
        fields = ['component', 'document']
        widgets = {
            'component': forms.Select(attrs={'class': 'form-control'}),
            'document': forms.Select(attrs={'class': 'form-control'}),
        }
        def __init__(self, user, *args, **kwargs):
            super(ComponentDocumentLinkForm, self).__init__(*args, **kwargs)
            self.fields['component'].queryset = Component.objects.filter(user=user)
            self.fields['document'].queryset = Document.objects.filter(user=user)
            self.fields['component'].widget.attrs['class'] = 'form-control'
            self.fields['document'].widget.attrs['class'] = 'form-control'
            self.fields['component'].widget.attrs['placeholder'] = 'Bir ürün seçiniz.'
            self.fields['document'].widget.attrs['placeholder'] = 'Bir belge seçiniz.'
            self.fields['component'].widget.attrs['required'] = 'required'
            self.fields['document'].widget.attrs['required'] = 'required'
            self.fields['component'].widget.attrs['id'] = 'component_id'
            self.fields['document'].widget.attrs['id'] = 'document_id'
            self.fields['component'].widget.attrs['name'] = 'component_id'

      