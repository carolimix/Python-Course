from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import json
import time

# Cambia la ruta a la ubicación de tu ChromeDriver
service = Service(r'C:\Users\carol\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe')
driver = webdriver.Chrome(service=service)

def buscar_en_google_maps(busqueda):
    driver.get("https://www.google.com/maps")
    time.sleep(5)  # Espera a que la página cargue
    
    # Encuentra el cuadro de búsqueda y escribe la consulta
    search_box = driver.find_element(By.ID, "searchboxinput")
    search_box.send_keys(busqueda)
    search_box.send_keys(Keys.ENTER)
    time.sleep(5)  # Espera a que los resultados carguen

    return driver.page_source

def extraer_resultados(html):
    soup = BeautifulSoup(html, 'html.parser')
    resultados = []
    
    # Encuentra los contenedores de cada resultado
    for resultado in soup.find_all('div', class_='section-result'):
        try:
            nombre = resultado.find('h3', class_='section-result-title').text
            direccion = resultado.find('span', class_='section-result-location').text
            # Aquí podrías agregar más detalles según necesites
            resultados.append({
                'Nombre': nombre,
                'Dirección': direccion,
                'Tiene baño': None,  # Puedes ajustar esto según tus necesidades
                'Mesas': None,       # Puedes ajustar esto según tus necesidades
                'Horario de apertura': None,  # Puedes ajustar esto según tus necesidades
                'Foto': None         # Puedes ajustar esto según tus necesidades
            })
        except Exception as e:
            print(f'Error al procesar un resultado: {e}')

    return resultados

def guardar_json(resultados, nombre_archivo='resultados.json'):
    with open(nombre_archivo, 'w', encoding='utf-8') as f:
        json.dump(resultados, f, ensure_ascii=False, indent=4)

busqueda = "restaurantes en [ciudad]"  # Reemplaza [ciudad] por la ciudad que deseas buscar
html = buscar_en_google_maps(busqueda)
resultados = extraer_resultados(html)
guardar_json(resultados)

# Cierra el navegador
driver.quit()
