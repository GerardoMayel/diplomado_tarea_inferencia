import requests

# URL del endpoint de predicción (ajusta según sea necesario)
url = "http://127.0.0.1:8000/prediction"

# Datos de prueba
data = {
    "pclass": 1,
    "name": "Allen, Miss. Elisabeth Walton",
    "sex": "female",
    "age": 29,
    "sibsp": 0,
    "parch": 0,
    "ticket": "24160",
    "fare": 211.3375,
    "cabin": "B5",
    "embarked": "S",
    "boat": "2",
    "body": "?",
    "home_dest": "St Louis, MO"
}





# Realizar la solicitud POST
response = requests.post(url, json=data)

# Verificar la respuesta
if response.status_code == 200:
    print("Predicción recibida:", response.json())
else:
    print("Error en la solicitud:", response.status_code, response.text)
