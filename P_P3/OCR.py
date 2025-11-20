import cv2 as cv
import numpy as np
import tensorflow as tf

model = tf.keras.models.load_model("best_model.keras")

cap = cv.VideoCapture(0)
img_height, img_width = 28, 28

# Ajuste para mayor velocidad, capturamos imágenes de menor resolución
cap.set(3, 640)  # Ancho
cap.set(4, 480)  # Alto

try:
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Preprocesado básico
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

        blurred = cv.GaussianBlur(gray, (11, 11), 0)  # mayor difusión para eliminar ruido
        _, thresh = cv.threshold(blurred, 120, 255, cv.THRESH_BINARY_INV)

        # Encontrar contornos (posibles dígitos)
        contours, _ = cv.findContours(thresh, cv.RETR_EXTERNAL,
                                      cv.CHAIN_APPROX_SIMPLE)

        digit_boxes = []  # array para guardar (x, label) y luego armar el número

        for c in contours:
            x, y, w, h = cv.boundingRect(c)

            # Filtro para quitar ruido (ajustar tamaño mínimo de contornos)
            if w * h < 150 or h < 10:  # El área del contorno tiene que ser mayor
                continue

            # Recortar región del dígito
            roi = thresh[y:y + h, x:x + w]

            # Redimensionar a 28x28
            roi_resized = cv.resize(roi, (img_height, img_width))

            # Normalizar [0,1]
            roi_norm = roi_resized.astype("float32") / 255.0
            input_img = roi_norm.reshape(1, 28, 28, 1)

            # Predicción
            prediction = model.predict(input_img, verbose=0)
            predicted_label = int(np.argmax(prediction))
            predicted_prob = np.max(prediction)  # Obtener la probabilidad máxima

            # Dibujar bbox y dígito en la imagen original
            cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv.putText(frame, f'{predicted_label} ({predicted_prob:.2f})', (x, y - 10),
                       cv.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

            # Guardamos para armar el número de izquierda a derecha
            digit_boxes.append((x, predicted_label))

        # Mostrar imágenes
        cv.imshow('Predicción OCR en tiempo real', frame)
        cv.imshow('Threshold', thresh)

        # Tecla para terminar
        if cv.waitKey(1) & 0xFF == ord('d'):
            break

except KeyboardInterrupt:
    pass
finally:
    cap.release()
    cv.destroyAllWindows()