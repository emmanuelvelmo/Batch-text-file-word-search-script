import os
import re

# Lista de codificaciones a probar (en orden de prioridad)
codificaciones_txt = ['utf-8', 'latin-1', 'utf-16', 'cp1252']

# Bucle principal continuo
while True:
    # Directorio de entrada
    while True:
        directorio_val = input("Enter directory: ").strip('"\'')

        if os.path.isdir(directorio_val):
            break

        print("Wrong directory")
    
    palabra_val = input("Enter text to search: ")
    
    print("------------------------------------")
    
    # Búsqueda insensible a mayúsculas/minúsculas:
    patron_busqueda = re.compile(r'\b' + re.escape(palabra_val) + r'\b', flags = re.IGNORECASE)
    
    # Buscar en todos los archivos del directorio
    for raiz_val, _, archivos_val in os.walk(directorio_val):
        for archivo_iter in archivos_val:
            ruta_completa = os.path.join(raiz_val, archivo_iter)
            
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
