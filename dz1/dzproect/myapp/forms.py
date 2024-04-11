from django import forms


from .models import Product1

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product1
        fields = '__all__'


class ProductCreateForm(forms.ModelForm):
    class Meta:
        model = Product1
        fields = '__all__'



