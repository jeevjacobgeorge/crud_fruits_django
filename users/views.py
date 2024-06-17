from django.shortcuts import render,redirect
from .models import Fruit
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .forms import FruitForm,NutritionForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def index(request):   
    fruits = Fruit.objects.all()
    return render(request, 'users/index.html', {'fruits': fruits})

def search_fruits(request):
    query = request.GET.get('q')
    print(query)
    if query:
        fruits = Fruit.objects.filter(name__icontains=query)
    else:
        fruits = Fruit.objects.all()
    fruits_list = [{
        'id': fruit.id,
        'name': fruit.name,
        'family': fruit.family,
        'order': fruit.order,
        'genus': fruit.genus,
        'nutrition': {
            'calories': fruit.nutrition.calories,
            'fat': fruit.nutrition.fat,
            'sugar': fruit.nutrition.sugar,
            'carbohydrates': fruit.nutrition.carbohydrates,
            'protein': fruit.nutrition.protein,
        }
    } for fruit in fruits]
    return JsonResponse({'fruits': fruits_list})


def delete_fruit(request, fruit_id):
    # Retrieve the fruit object from the database
    fruit = get_object_or_404(Fruit, pk=fruit_id)
    if request.method == 'POST':
        # Delete the fruit
        if fruit:
            fruit.delete()
            return redirect('home')
        else:
            return JsonResponse({'error': 'fruit doesn\'t exist'}, status=400)
    else: #get
        return render(request, 'users/delete.html', {'fruit': fruit})

def add_fruit(request):
    if request.method == 'POST':
        nutrition_form = NutritionForm(request.POST)
        fruit_form = FruitForm(request.POST)
        if nutrition_form.is_valid() and fruit_form.is_valid():
            print('valid')
            nutrition = nutrition_form.save()
            fruit = fruit_form.save(commit=False)
            fruit.nutrition = nutrition
            fruit.save()
            return redirect('home')  # Replace 'home' with your desired redirect URL
        else:
            print('not valid')
            # Print errors for debugging
            print(nutrition_form.errors)
            print(fruit_form.errors)
    else:
        nutrition_form = NutritionForm()
        fruit_form = FruitForm()

    return render(request, 'users/add_fruit.html', {
        'nutrition_form': nutrition_form,
        'fruit_form': fruit_form,
    })



def update_fruit(request, fruit_id):
    fruit = get_object_or_404(Fruit, pk=fruit_id)
    if request.method == 'POST':
        fruit_form = FruitForm(request.POST, instance=fruit)
        nutrition_form = NutritionForm(request.POST, instance=fruit.nutrition)
        if fruit_form.is_valid() and nutrition_form.is_valid():
            fruit_form.save()
            nutrition_form.save()
            return redirect('home')
    else:
        fruit_form = FruitForm(instance=fruit)
        nutrition_form = NutritionForm(instance=fruit.nutrition)

    return render(request, 'users/update.html', {
        'fruit_form': fruit_form,
        'nutrition_form': nutrition_form,
    })


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})