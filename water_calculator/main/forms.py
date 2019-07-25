from django import forms
from .models import User,question_wise_result

class Pincode(forms.ModelForm):
    class Meta:
        model = User
        fields= ["pincode"]


