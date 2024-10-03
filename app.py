from flask import Flask, render_template, request
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut

app = Flask(__name__)

# Crear el geocodificador
geolocator = Nominatim(user_agent="Pasante_app_v1")

@app.route('/', methods=['GET', 'POST'])
def index():
    direccion = ''
    latitud = ''
    longitud = ''
    if request.method == 'POST':
        latitud = request.form.get('latitud')
        longitud = request.form.get('longitud')
        try:
            # Obtener dirección a partir de coordenadas
            location = geolocator.reverse(f"{latitud}, {longitud}")
            if location:
                direccion = location.address
            else:
                direccion = "No se encontró la dirección."
        except GeocoderTimedOut:
            direccion = "Error: la solicitud tardó demasiado tiempo."

    return render_template('index.html', direccion=direccion, latitud=latitud, longitud=longitud)

if __name__ == '__main__':
    app.run(debug=True)