import cv2 as cv
import numpy as np
import tensorflow as tf
model=tf.keras.models.load_model("model_2.keras")

cap=cv.VideoCapture(0)
img_height, img_width = 28, 28


try:
    while True:
        ret,frame=cap.read()
        if not ret:
            break
        gray=cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        thresh = cv.threshold(gray, 90, 255, cv.THRESH_BINARY_INV)[1]
        # Redimensionar a 28x28
        resized = cv.resize(thresh, (img_height, img_width))
        # Normalizar a rango [0,1]
        normalized = resized.astype("float32") / 255.0
        input_img=normalized.reshape(1,28,28,1)
        prediction=model.predict(input_img)
        predicted_label=np.argmax(prediction)
        frame_with_prediction=cv.putText(frame, str(predicted_label),(10,30),
                                        cv.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2,cv.LINE_AA)
        cv.imshow('Predicción en tiempo real',frame_with_prediction)
        upscaled_norm=cv.resize(normalized,(280,280),interpolation=cv.INTER_NEAREST)
        cv.imshow('Imagen Re-escalada',upscaled_norm)
        # Tecla para terminar programa
        if cv.waitKey(1) & 0xFF==ord('d'):
            break
    


except KeyboardInterrupt:
    pass
finally:
    cap.release()
    cv.destroyAllWindows()