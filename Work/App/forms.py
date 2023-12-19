from django import forms
from .models import Films

class FormAdd(forms.Form):
    name = forms.CharField(required=True, label='', widget=forms.TextInput(attrs={'name': 'name'}))
    category = forms.ChoiceField(choices=(('Комедии', 'Комедии'), ('Драмы', 'Драмы'), ('Приключения', 'Приключения'), ('Мелодрамы', 'Мелодрамы'), ('Боевики', 'Боевики'), ('Фантастика', 'Фантастика'), ('Ужастики', 'Ужастики')), label='', widget=forms.Select(attrs={'name': 'category'}))
    date_create = forms.CharField(required=True, label='', widget=forms.TextInput(attrs={'name': 'date_create'}))
    actors = forms.CharField(required=True, label='', widget=forms.Textarea(attrs={'name': 'actors'}))
    date_visible = forms.CharField(required=True, label='', widget=forms.TextInput(attrs={'name': 'date_visible'}))

class FilmsEditForm(forms.ModelForm):
    class Meta:
        model = Films
        fields = '__all__'