import requests
from django.shortcuts import render
from django.http import HttpResponse

# Простая функция для получения данных
def get_character_data(character_id):
    try:
        url = f"https://swapi.dev/api/people/{character_id}/"
        response = requests.get(url, timeout=10, verify=False)
        response.raise_for_status()
        data = response.json()
        return data
    except Exception as e:
        print(f"Error fetching data from {url}: {str(e)}")
        import traceback
        traceback.print_exc()
        return None

# Главная страница
def home(request):
    # Простой список персонажей для главной страницы
    characters = [
        {'id': 1, 'name': 'Люк Скайуокер'},
        {'id': 2, 'name': 'С-3PO'},
        {'id': 3, 'name': 'Р2-Д2'},
    ]
    return render(request, 'home.html', {'characters': characters})

# Первый персонаж
def character1(request):
    try:
        data = get_character_data(1)
        if not data:
            return HttpResponse("Error: Could not fetch character data from API")
        
        # Получаем названия фильмов
        films = []
        for film_url in data.get('films', []):
            try:
                film_data = requests.get(film_url, timeout=10, verify=False).json()
                films.append(film_data['title'])
            except:
                films.append("Unknown Film")
        
        # Получаем названия транспорта
        vehicles = []
        for vehicle_url in data.get('vehicles', []):
            try:
                vehicle_data = requests.get(vehicle_url, timeout=10, verify=False).json()
                vehicles.append(vehicle_data['name'])
            except:
                vehicles.append("Unknown Vehicle")
        
        # Получаем названия кораблей
        starships = []
        for ship_url in data.get('starships', []):
            try:
                ship_data = requests.get(ship_url, timeout=10, verify=False).json()
                starships.append(ship_data['name'])
            except:
                starships.append("Unknown Starship")
        
        context = {
            'name': data.get('name', 'Unknown'),
            'height': data.get('height', 'N/A'),
            'mass': data.get('mass', 'N/A'),
            'hair_color': data.get('hair_color', 'N/A'),
            'skin_color': data.get('skin_color', 'N/A'),
            'eye_color': data.get('eye_color', 'N/A'),
            'birth_year': data.get('birth_year', 'N/A'),
            'gender': data.get('gender', 'N/A'),
            'films': films,
            'vehicles': vehicles,
            'starships': starships,
        }
        return render(request, 'character.html', context)
    except Exception as e:
        return HttpResponse(f"Error: {str(e)}")

# Второй персонаж (просто копируем и меняем ID)
def character2(request):
    try:
        data = get_character_data(2)
        if not data:
            return HttpResponse("Error: Could not fetch character data from API")
        
        films = []
        for film_url in data.get('films', []):
            try:
                film_data = requests.get(film_url, timeout=10, verify=False).json()
                films.append(film_data['title'])
            except:
                films.append("Unknown Film")
        
        vehicles = []
        for vehicle_url in data.get('vehicles', []):
            try:
                vehicle_data = requests.get(vehicle_url, timeout=10, verify=False).json()
                vehicles.append(vehicle_data['name'])
            except:
                vehicles.append("Unknown Vehicle")
        
        starships = []
        for ship_url in data.get('starships', []):
            try:
                ship_data = requests.get(ship_url, timeout=10, verify=False).json()
                starships.append(ship_data['name'])
            except:
                starships.append("Unknown Starship")
        
        context = {
            'name': data.get('name', 'Unknown'),
            'height': data.get('height', 'N/A'),
            'mass': data.get('mass', 'N/A'),
            'hair_color': data.get('hair_color', 'N/A'),
            'skin_color': data.get('skin_color', 'N/A'),
            'eye_color': data.get('eye_color', 'N/A'),
            'birth_year': data.get('birth_year', 'N/A'),
            'gender': data.get('gender', 'N/A'),
            'films': films,
            'vehicles': vehicles,
            'starships': starships,
        }
        return render(request, 'character.html', context)
    except Exception as e:
        return HttpResponse(f"Error: {str(e)}")

# Третий персонаж
def character3(request):
    try:
        data = get_character_data(3)
        if not data:
            return HttpResponse("Error: Could not fetch character data from API")
        
        films = []
        for film_url in data.get('films', []):
            try:
                film_data = requests.get(film_url, timeout=10, verify=False).json()
                films.append(film_data['title'])
            except:
                films.append("Unknown Film")
        
        vehicles = []
        for vehicle_url in data.get('vehicles', []):
            try:
                vehicle_data = requests.get(vehicle_url, timeout=10, verify=False).json()
                vehicles.append(vehicle_data['name'])
            except:
                vehicles.append("Unknown Vehicle")
        
        starships = []
        for ship_url in data.get('starships', []):
            try:
                ship_data = requests.get(ship_url, timeout=10, verify=False).json()
                starships.append(ship_data['name'])
            except:
                starships.append("Unknown Starship")
        
        context = {
            'name': data.get('name', 'Unknown'),
            'height': data.get('height', 'N/A'),
            'mass': data.get('mass', 'N/A'),
            'hair_color': data.get('hair_color', 'N/A'),
            'skin_color': data.get('skin_color', 'N/A'),
            'eye_color': data.get('eye_color', 'N/A'),
            'birth_year': data.get('birth_year', 'N/A'),
            'gender': data.get('gender', 'N/A'),
            'films': films,
            'vehicles': vehicles,
            'starships': starships,
        }
        return render(request, 'character.html', context)
    except Exception as e:
        return HttpResponse(f"Error: {str(e)}")

# Create your views here.
