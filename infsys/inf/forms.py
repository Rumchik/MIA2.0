from django import forms
from .models import Ammo, Weapon
from django.core.exceptions import ValidationError


class WeaponForm(forms.ModelForm):
    class Meta:
        model = Weapon
        fields = ['name', 'slug', 'description', 'caliber', 'ammos']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'caliber': forms.NumberInput(attrs={'class': 'form-control'}),
            'ammos': forms.SelectMultiple(attrs={'class': 'form-control'})
        }

    def clean_slug(self):
        new_slug = self.cleaned_data['slug'].lower()

        if new_slug == 'create':
            raise ValidationError('Ошибка, введите другие символы')
        return new_slug


class AmmoForm(forms.ModelForm):
    class Meta:
        model = Ammo
        fields = ['name', 'slug']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'})
        }

        
#    name = forms.CharField(max_length=150,)
#    slug = forms.CharField(max_length=150)

#    name.widget.attrs.update({'class': 'form-control'})
#    slug.widget.attrs.update({'class': 'form-control'})


    def clean_slug(self):
        new_slug = self.cleaned_data['slug'].lower()

        if new_slug == 'create':
            raise ValidationError('Ошибка, введите другие символы')
#        if Ammo.objects.filter(slug__iexact=new_slug).count():
#            raise ValidationError('Ошибка, такое имя уже существует'.format(new_slug))
        return new_slug

#    def save(self):
#        new_ammo = Ammo.objects.create(
#            name=self.cleaned_data['name'],
#            slug=self.cleaned_data['slug']
#        )
#        return new_ammo