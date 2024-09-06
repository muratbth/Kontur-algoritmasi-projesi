import cv2
import numpy as np
# Video dosyasını yükle
video_capture = cv2.VideoCapture('canada.mp4')

# Video çerçevelerini döngüye al
while True:
    # Bir sonraki kareyi yakalar. 
    ret, frame = video_capture.read()
    
    if not ret:
        break

    # Görüntüyü HSV renk uzayına dönüştürür.
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Kırmızı rengin aralığını tanımlar ton-doygunluk-değer
    lower_red = np.array([0, 50, 50])
    upper_red = np.array([10, 255, 255])

    # Kırmızı rengi tespit eder.HSV çerçevesindeki her pikseli kontrol eder 
    mask = cv2.inRange(hsv_frame, lower_red, upper_red)

    # Konturları bulur.
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Her bir konturu çizer.
    for contour in contours:
        area = cv2.contourArea(contour) #konturun alanını hesaplar.
        if area > 100:  # Minimum alanı belirtir.
            cv2.drawContours(frame, contour, -1, (0, 255, 0), 3)  # Konturu çizer.


    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


video_capture.release()
cv2.destroyAllWindows()
