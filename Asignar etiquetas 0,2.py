# -*- coding: utf-8 -*-
"""
Created on Fri Dec 16 22:53:31 2022

@author: Rotoxe
"""

import csv
from io import StringIO
import PyPDF2

# Abre el PDF
pdf_reader = PyPDF2.PdfFileReader('D:/Años/2022/Python/etiquetas pdf/Libro_1.pdf')

# Crea un diccionario para almacenar el número de veces que aparece cada palabra
palabras = {}

# Recorre cada página del PDF
for num_pagina in range(pdf_reader.getNumPages()):
    # Obtiene el texto de la página actual
    texto = pdf_reader.getPage(num_pagina).extractText()

    # Separa el texto en palabras
    lista_palabras = texto.split()

    # Cuenta el número de veces que aparece cada palabra
    for palabra in lista_palabras:
        if palabra.lower() in palabras:
            # Si la palabra es una de las que no quieres contar, continúa con la siguiente iteración
            if palabra.lower() in ['el', 'la', 'los', 'las']:
                continue
            palabras[palabra.lower()] += 1
        else:
            # Si la palabra es una de las que no quieres contar, continúa con la siguiente iteración
            if palabra.lower() in ['l','a', 'al', 'asi', 'así', 'cada', 'como', 'con', 'cuando', 'de', 'debe', 'del', 'donde', 'e', 'el', 'en', 'entre', 'es', 'este', 'esto', 'ha', 'la', 'las', 'lo', 'los', 'manera', 'más', 'no', 'nos', 'o', 'para', 'por', 'puede', 'que', 's', 'se', 'sea', 'ser', 'si', 'sin', 'sobre', 'son', 'su', 'sus', 'tener', 'un', 'una', 'y', '•']:
                continue
            palabras[palabra] = 1

# Ordena el diccionario por el número de veces que aparece cada palabra
palabras_ordenadas = sorted(palabras.items(), key=lambda x: x[1], reverse=True)

# Toma las 10 palabras más frecuentes
palabras_top_20 = palabras_ordenadas[:20]

# Asigna un valor inicial a la variable tema
tema = None
temas = []

# Lista de etiquetas 
etiquetas = ['arte', 'psicología', 'medicina']

# Intera sobre las palabras más frecuentes
for palabra, frecuencia in palabras_top_20:
    #Verifica si la palbra está contenida en la lista de temas
    if palabra in etiquetas:
        #tema = palabra
        temas.append(palabra)
        #temas[0] = temas[-1]
        break

# Itera sobre la lista de temas
for t in palabras_ordenadas:
    # Verifica si el tema ya está presente en la lista temas
    if t[0] in temas:
        continue
    # Agregar el tema a la lista temas
    temas.append(t[0])
    # Si la lista temas tiene tres elementos, rompe el bucle
    if len(temas) == 3:
        break


# Itera sobre la lista de temas
for t in temas:
# Verifica si el tema está presente en el texto
    if t in temas:
        tema = t
        break


# Crea un archivo CSV con el tema del libro
csv_file = StringIO()
writer = csv.writer(csv_file)
writer.writerow(['tema 1', 'tema 2', 'tema 3'])
writer.writerow([temas[0], temas[1], temas[2]])

try:
    # Escribe el contenido del archivo CSV en un archivo en disco
    with open('D:\\Años\\2022\\Python\\etiquetas pdf\\Libro.csv', 'w') as file:
        file.write(csv_file.getvalue())
except Exception as e:
    print(f'Ocurrió un error al escribir el archivo CSV: {e}')
print(temas)