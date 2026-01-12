from django import forms
from django.contrib.auth.models import User
from courses.models import AdditionalInfo


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']


class AdditionalInfoForm(forms.ModelForm):
    class Meta:
        model = AdditionalInfo
        fields = [
            'profile_picture',
            'phone_number',
            'address',
            'school',
            'district',
            'upazilla',
            'batch_year',
        ]
