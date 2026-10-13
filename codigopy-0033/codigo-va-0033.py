# Keyla Paola NC = 0033

import cv2
from pathlib import Path

# 1. Definir las rutas de trabajo
carpeta_proyecto = Path(__file__).resolve().parent.parent

ruta_original= (
    carpeta_proyecto
    / "img-original-0033"
    / "img-licuadora-0033.jpg"
)

carpeta_resultados = (
    carpeta_proyecto / "resultados-img-0033"
)

# Crear la carpeta de resultados si no existe
carpeta_resultados.mkdir(parents=True, exist_ok=True)

# 2. Leer la imagen original con imread
img0033 = cv2.imread(str(ruta_original))

# Comprobar que la imagen se haya leído correctamente
if img0033 is None:
    raise FileNotFoundError(
        f"No se pudo leer la imagen: {ruta_original}"
    )

# 3. Rotar la imagen 90 grados en sentido horario
img90_0033 = cv2.rotate(
    img0033, cv2.ROTATE_90_CLOCKWISE
)

# 4. Rotar la imagen 45 grados
alto, ancho = img0033.shape[:2]

centro = (ancho // 2, alto // 2)

matriz_rotacion = cv2.getRotationMatrix2D(
    centro, 45, 1.0
)

img45_0033 = cv2.warpAffine(
    img0033,
    matriz_rotacion,
    (ancho, alto)
)

# 5. Redimensionar a 600 píxeles de ancho
# y 500 píxeles de alto
img600x500_0033 = cv2.resize(
    img0033, (600, 500)
)

# 6. Dibujar un rectángulo rojo de 100 x 200
# píxeles sobre una copia de la imagen original
img_rojo_0033 = img0033.copy()

x1, y1 = 50, 50
x2, y2 = x1 + 100, y1 + 200

cv2.rectangle(
    img_rojo_0033,
    (x1, y1),
    (x2, y2),
    (0, 0, 255),
    3
)

# 7. Mostrar las cinco imágenes con sus títulos
cv2.imshow("licuadora original 0033", img0033)

cv2.imshow("licuadora 90 0033", img90_0033)

cv2.imshow("licuadora 45 0777", img45_0033)

cv2.imshow(
    "licuadora 600x500 0777",
    img600x500_0033
)

cv2.imshow("licuadora rojo 0033", img_rojo_0033)

# 8. Guardar las cuatro imágenes procesadas
cv2.imwrite(
    str(carpeta_resultados / "img-licuadora1-0033.jpg"),
    img90_0033
)

cv2.imwrite(
    str(carpeta_resultados / "img-licuadora2-0033.jpg"),
    img45_0033
)

cv2.imwrite(
    str(carpeta_resultados / "img-licuadora3-0033.jpg"),
    img600x500_0033
)

cv2.imwrite(
    str(carpeta_resultados / "img-licuadora4-0033.jpg"),
    img_rojo_0033
)

# 9. Esperar una tecla y cerrar las ventanas
print("Imágenes procesadas y guardadas.")
print("Presiona una tecla en las ventanas para finalizar.")

cv2.waitKey(0)
cv2.destroyAllWindows()

print("Keyla Paola NC = 0033")