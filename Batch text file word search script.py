import os
import re

# Lista de codificaciones a probar (en orden de prioridad)
codificaciones_txt = ['utf-8', 'latin-1', 'utf-16', 'cp1252']

while True:
    directorio = input("Enter directory: ")
    if not os.path.isdir(directorio):
        print("Directory not found")
        
        continue
    
    palabra = input("Enter text to search: ")
    print("------------------------------------")
    
    # Búsqueda insensible a mayúsculas/minúsculas:
    patron_busqueda = re.compile(r'\b' + re.escape(palabra) + r'\b', flags = re.IGNORECASE)
    
    # Buscar en todos los archivos del directorio
    for raiz, _, archivos in os.walk(directorio):
        for archivo_iter in archivos:
            ruta_completa = os.path.join(raiz, archivo_iter)
            
             # Probar diferentes codificaciones
            for codificacion_iter in codificaciones_txt:
                try:
                    with open(ruta_completa, 'r', encoding = codificacion_iter) as arch:
                        if patron_busqueda.search(arch.read()):
                            print(ruta_completa)
                            
                            break
                except (UnicodeDecodeError, PermissionError, IOError):
                    continue
    
    print("------------------------------------\n")
