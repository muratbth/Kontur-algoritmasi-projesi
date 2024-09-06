import cv2

# video dosyası veya kamera akışı için cv2.VideoCapture() kullanarak kaynak seçin
cap = cv2.VideoCapture("testvideo.mp4")

# Hareket algılama algoritmasını başlatın
fgbg = cv2.createBackgroundSubtractorMOG2()

while True:
    # Yeni bir kare yakalayın
    ret, frame = cap.read()

    # Hareket algılama algoritması kullanarak arka planı çıkarın
    fgmask = fgbg.apply(frame)

    # Morfolojik işlemleri kullanarak gürültüyü azaltın
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
    fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel)

    # Eşik değerleme işlemi yapın
    thresh = 127
    ret, fgmask = cv2.threshold(fgmask, thresh, 255, cv2.THRESH_BINARY)

    # Tüm konturları bulun
    contours, hierarchy = cv2.findContours(fgmask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Kontur çizmek için döngü
    for i in range(len(contours)):
        if cv2.contourArea(contours[i]) > 1000:  # minimum kontur alanı
            (x, y, w, h) = cv2.boundingRect(contours[i])
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

    # Sonuçları gösterin
        cv2.imshow('frame', frame)
        cv2.imshow('fgmask', fgmask)

    # Çıkış yapmak için 'q' tuşuna basın
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Temizleme ve serbest bırakma
cap.release()
cv2.destroyAllWindows()
