from PIL import Image, ImageDraw, ImageFont
import os
%pip install Pillow
# Función para crear y descargar la imagen
def referenciar_imagen(file_name, base_ref, specific_ref):
    archivos_png = [f for f in os.listdir("./") if f.endswith('.PNG')]
    if len(archivos_png) != 1:
      return "No hay archivos png o hay mas de uno"
    ruta_imagen = archivos_png[0]
    imagen = Image.open(ruta_imagen)

    # Crear un objeto de dibujo
    dibujo = ImageDraw.Draw(imagen)

    ruta_fuente = "calibri.ttf"
    tamaño_fuente = 24

    # Elegir una fuente y tamaño
    fuente = ImageFont.truetype(ruta_fuente, tamaño_fuente)

    # Definir los textos a insertar
    texto_derecha = f"x-Ref.: {base_ref}.{specific_ref} \nJM 06/2024"
    texto_centrado = f"Ok, veure x-Ref.: {base_ref}"

    # Obtener el tamaño del texto
    ancho_texto_base, alto_texto_base = dibujo.textsize(texto_derecha, font=fuente)
    ancho_texto_specific, alto_texto_specific = dibujo.textsize(texto_centrado, font=fuente)

    # Definir la posición del texto con un margen de 20px desde la derecha y desde arriba
    margen_derecha_base = 20
    margen_arriba_base = 20
    posicion_base = (imagen.width - ancho_texto_base - margen_derecha_base, margen_arriba_base)
    posicion_specific = ((imagen.width - ancho_texto_specific) // 2, (imagen.height - 40))

    # Insertar el texto en la imagen
    dibujo.text(posicion_base, texto_derecha, fill="red", font=fuente)
    dibujo.text(posicion_specific, texto_centrado, fill="red", font=fuente)

    # Guardar la imagen resultante
    output_file_name = f'{base_ref}.{specific_ref}.png'
    imagen.save(output_file_name)

    # Descargar la imagen resultante
    files.download(output_file_name)
    return output_file_name

# Llamar a la función para crear y descargar la imagen
output_file = referenciar_imagen("img.PNG", "B-1.3", "4.5.3")
