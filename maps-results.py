from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import json
import time

# Configura el navegador Chrome
driver = webdriver.Chrome()

# Abre la URL de la lista de resultados
url = "https://www.google.com/maps/search/sp%C3%A4ti/@52.5175801,13.2367057,10z/data=!4m2!2m1!6e6?entry=ttu"
driver.get(url)

# Espera a que la página se cargue completamente
time.sleep(5)  # Puedes ajustar el tiempo de espera según sea necesario

# Extrae los resultados de la página
results = []
soup = BeautifulSoup(driver.page_source, 'html.parser')
for item in soup.find_all('div', class_='section-result'):
    name = item.find('h3', class_='section-result-title').text.strip()
    address = item.find('span', class_='section-result-location').text.strip()
    results.append({'name': name, 'address': address})

# Cierra el navegador
driver.quit()

# Guarda los resultados en un archivo JSON
with open('resultados.json', 'w', encoding='utf-8') as f:
    json.dump(results, f, ensure_ascii=False, indent=4)

print("Los resultados se han guardado en el archivo 'resultados.json'.")
