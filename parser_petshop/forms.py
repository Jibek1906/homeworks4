from django import forms
from . import models, parser_petshop

class ParserForm(forms.Form):
    WEBSITE_CHOICES = (
        ('petshop', 'petshop'),
    )

    website_choice = forms.ChoiceField(choices=WEBSITE_CHOICES)
    class Meta:
        fields = [
            'website_choice',
        ]

    def parser_data(self):
        if self.data['website_choice'] == 'petshop':
            file_petshop = parser_petshop.parsing()
            for i in file_petshop:
                models.PetShopModel.objects.create(**i)