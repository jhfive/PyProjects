from django.forms import ModelForm
from Community.models import *

class Form(ModelForm):
    class Meta:
        model = Dto
        fields = ['name', 'title', 'contents', 'url', 'email']