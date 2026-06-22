import requests

def obtener_usuario(username):
    url = f"https://api.github.com/users/{username}"
    respuesta = requests.get(url)
    if respuesta.status_code == 200:
        datos = respuesta.json()
        print(f"Nombre: {datos.get('name')}")
        print(f"Bio: {datos.get('bio')}")
    else:
        print("No se pudo encontrar al usuario")

if __name__ == "__main__":
    obtener_usuario("python")