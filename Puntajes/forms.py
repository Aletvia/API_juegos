from django import forms
from .models import Score

class  Create_Score(object):
    class Meta:
        model = Score
        fields = '__all__'
