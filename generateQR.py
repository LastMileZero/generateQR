from PIL import Image
import qrcode

def descargar_procesar_imagen(img_url):
    # im = Image.open(requests.get(img_url, stream=True).raw)
    im = Image.open(img_url)
    return im


def redimensionar_imagen(im, tamano):
    return im.resize((tamano, tamano), Image.Resampling.LANCZOS)


def generar_codigo_qr(texto, imagen):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(texto)
    qr.make(fit=True)
    img_qr = qr.make_image(fill_color="green", back_color="white")
    # Posición para colocar el logo en el centro del QR
    position = ((img_qr.size[0] - imagen.size[0]) // 2, (img_qr.size[1] - imagen.size[1]) // 2)

    # Crear una imagen en blanco para superponer el logo sin afectar el QR
    overlay = Image.new('RGBA', img_qr.size, (255, 255, 255, 0))
    overlay.paste(imagen, position, imagen)

    # Combinar la imagen del QR con el logo superpuesto
    img_qr = Image.alpha_composite(img_qr.convert('RGBA'), overlay)

    return img_qr


def main():
    img_url = 'Logo.png'
    texto = 'https://github.com/LastMileZero/ImpactProject'

    imagen_procesada = descargar_procesar_imagen(img_url)
    imagen_90x90 = redimensionar_imagen(imagen_procesada, 90)

    codigo_qr = generar_codigo_qr(texto, imagen_90x90)
    codigo_qr.save('codigo_qr_con_imagen.png')
    print("Código QR con imagen creado exitosamente. ¡Revise el archivo 'codigo_qr_con_imagen.png'!")

if __name__ == "__main__":
    main()



