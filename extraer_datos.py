# Import libraries
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def extractor_de_datos():
    print("Iniciando extractor de datos...")

    options = Options()
    options.headless = True

    browser = webdriver.Chrome(
        executable_path=r"C:\Users\fernando_Dember\Apps\chromedriver.exe",
        chrome_options=options,
    )

    browser.get(
        "https://geosocial.maps.arcgis.com/apps/opsdashboard/index.html#/2c6e932c690d467b85375af52b614472"
    )

    time.sleep(20)
    print("Cargando pagina y obteniendo datos...")

    soup = BeautifulSoup(browser.page_source, features="html.parser")

    lista_div_id = [
        {"nombre": "casos", "id": "ember12"},
        {"nombre": "casos_por_corregimiento", "id": "ember46"},
        {"nombre": "casos_por_genero", "id": "ember54"},
        {"nombre": "cantidad_de_pruebas", "id": "ember113"},
        {"nombre": "rango_de_edades", "id": "ember27"},
    ]

    for pagina in lista_div_id:
        archivo = f"./output/{pagina.get('nombre')}.html"
        print(f"Creando archivo: {pagina.get('nombre')}.html")
        casos = open(archivo, "w")
        casos.write(str(soup.find("div", {"id": pagina.get("id")})))
        casos.close()

    print(f"Listo, cantidad de archivos html creados: {len(lista_div_id)}")

    browser.quit()


extractor_de_datos()
