from django import forms
from django.core.exceptions import ValidationError

from .models import *


class StudentForm(forms.Form):
    ism = forms.CharField(label='Ism ')
    jins = forms.CharField(label='Jins')
    bitiruvchi = forms.BooleanField()
    kitob_soni = forms.IntegerField(label='Kitob soni ')

    def clean_ism(self):
        qiymat = self.cleaned_data.get('ism')
        if not qiymat.endswith('jon') and not qiymat.endswith('bek'):
            raise ValidationError("Ism o'zbekcha emas!")
        return qiymat

    def clean_kitob_soni(self):
        qiymat = self.cleaned_data.get('kitob_soni')
        if qiymat < 0 or qiymat > 5:
            raise ValidationError('Talabga to\'g\'ri kelmaydi')
        return qiymat

class KitobForm(forms.ModelForm):
    class Meta:
        model = Kitob
        fields = ('nom', 'sahifa', 'janr', 'muallif')

class MuallifForm(forms.Form):
    ism = forms.CharField()
    tirik = forms.BooleanField(required=False)
    kitob_soni = forms.IntegerField()
    tugilgan_yil = forms.DateField()


class RecordForm(forms.ModelForm):

    class Meta:
        model = Record
        fields = ('student', 'kitob', 'olingan_sana', 'qaytardi', 'qaytargan_sana')


    # student = forms.CharField()
    # kitob = forms.CharField()
    # olingan_sana = forms.DateField()
    # qaytardi = forms.BooleanField(required=False)
    # qaytargan_sana = forms.DateField()









