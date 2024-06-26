def contar_letras_y_espacios(archivo):
    try:#intentar abrir el el archibo 
        with open(archivo, 'r') as file:
            contenido = file.read()
            letras = sum(c.isalpha() for c in contenido)  # Contar letras
            espacios = sum(c.isspace() for c in contenido)  # Contar espacios

            return letras, espacios
    except FileNotFoundError:#except si esque el archibo no existe tira error
        print(f"Error: El archivo {archivo} no fue encontrado.")#f es para poder meter bariables o llaves dentro del texto
        return None, None #es para debolver nada :v
    except Exception as e: #Exception de cualquier errr no espesificado tira error 
        print(f"Error inesperado: {e}")
        return None, None
    #output_archivo es la variable salida 
def generar_resumen(input_archivo, output_archivo):#def funsion= def generar_ resumen
    letras, espacios = contar_letras_y_espacios(input_archivo)#sa 2 variables de la fincion contar letras y espacios
    if letras is not None and espacios is not None: #if e si
        with open(output_archivo, 'w',) as file:
            file.write(f"El archivo {input_archivo} contiene:\n") #write sirve para escivir las cosas en el archivo y file es archibo
            file.write(f"Número de letras: {letras}\n")
            file.write(f"Número de espacios: {espacios}\n")
        print(f"Resumen generado correctamente en {output_archivo}")
    else:
        print("No se pudo generar el resumen debido a errores.")

# Ejemplo de uso:
archivo_origen = "C:/Users/admin/Desktop/uwu.txt"  # Cambiar por el nombre de tu archivo de texto
archivo_resumen = 'C:/Users/admin/Desktop/resumen.txt'  # Nombre del archivo de resumen que se generará
generar_resumen(archivo_origen, archivo_resumen)
    

    