import requests
from django.core.management.base import BaseCommand
from users.models import Fruit, Nutrition

class Command(BaseCommand):
    help = 'Fetches fruit data from an external API and saves it to the database'

    def handle(self, *args, **kwargs):
        api_url = 'https://www.fruityvice.com/api/fruit/all'
        response = requests.get(api_url)
        if response.status_code == 200:
            data = response.json()
            for item in data:
                name = item['name']
                family = item['family']
                order = item['order']
                genus = item['genus']
                nutritions = item['nutritions']

                nutrition, created = Nutrition.objects.get_or_create(
                    calories=nutritions['calories'],
                    fat=nutritions['fat'],
                    sugar=nutritions['sugar'],
                    carbohydrates=nutritions['carbohydrates'],
                    protein=nutritions['protein']
                )

                fruit, created = Fruit.objects.get_or_create(
                    name=name,
                    family=family,
                    order=order,
                    genus=genus,
                    nutrition=nutrition
                )

                if created:
                    self.stdout.write(self.style.SUCCESS(f'Successfully added {name}'))
                else:
                    self.stdout.write(self.style.WARNING(f'{name} already exists'))
        else:
            self.stdout.write(self.style.ERROR('Failed to fetch data from API'))
