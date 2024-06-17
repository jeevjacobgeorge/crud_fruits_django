from django import forms
from .models import Fruit, Nutrition

from django import forms
from .models import Fruit, Nutrition

class NutritionForm(forms.ModelForm):
    class Meta:
        model = Nutrition
        fields = ['calories', 'fat', 'sugar', 'carbohydrates', 'protein']

class FruitForm(forms.ModelForm):
    class Meta:
        model = Fruit
        fields = ['name', 'family', 'order', 'genus']
