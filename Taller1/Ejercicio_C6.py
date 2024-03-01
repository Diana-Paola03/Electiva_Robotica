import cv2
import numpy as np
import matplotlib.pyplot as plt

def obtener_contornos(imagen_path):
    imagen = cv2.imread(imagen_path)

    if imagen is None:
        print(f"No se pudo cargar la imagen en la ruta: {imagen_path}")
        return [], None

    gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
    _, umbral = cv2.threshold(gris, 240, 255, cv2.THRESH_BINARY)
    contornos, _ = cv2.findContours(umbral, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contornos_xy = []

    for contorno in contornos:
        xy = np.squeeze(contorno)
        contornos_xy.append(xy)

    return contornos_xy, imagen

def main():
    imagenes = [
        'C:/Users/diana/Pictures/ejercicio_6/Renault.PNG',
        'C:/Users/diana/Pictures/ejercicio_6/mazda png.png' 
    ]

    for imagen_path in imagenes:
        contornos, imagen = obtener_contornos(imagen_path)
        nombre_imagen = imagen_path.split('/')[-1].split('.')[0]
        print(f"Coordenadas de contornos de la imagen {nombre_imagen}:")

        for i, contorno in enumerate(contornos):
            print(f"Contorno {i + 1}:")
            for x, y in contorno:
                print(f"X: {x}, Y: {y}")

        # Dibujar contornos en la imagen
        cv2.drawContours(imagen, contornos, -1, (0, 255, 0), 2)

        # Mostrar la imagen con contornos
        plt.imshow(cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB))
        plt.title(f'Contornos de la imagen {nombre_imagen}')
        plt.axis('off')
        plt.show()

if __name__ == "__main__":
    main()
