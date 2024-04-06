import requests

def descargar_y_guardar_csv(url):
    # Realiza la solicitud GET
    respuesta = requests.get(url)
    
    # Asegúrate de que la solicitud fue exitosa
    if respuesta.status_code == 200:
        # Abre un archivo en modo de escritura
        with open('datos_descargados.csv', 'w') as archivo:
            # Escribe el contenido de la respuesta en el archivo
            archivo.write(respuesta.text)
        print("Los datos han sido descargados y guardados en 'datos_descargados.csv'.")
    else:
        print(f"Error al descargar los datos: status code {respuesta.status_code}")

# Ejemplo de uso de la función con la URL proporcionada
descargar_y_guardar_csv('https://huggingface.co/datasets/mstz/heart_failure/raw/main/heart_failure_clinical_records_dataset.csv')
