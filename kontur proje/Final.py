import cv2
import numpy as np

cap=cv2.VideoCapture('testvideo.mp4')

ret, frame1 = cap.read()
ret, frame2 = cap.read()

while cap.isOpened():   # Video dosyasının açık olup olmadığını kontrol eden döngü.
    diff = cv2.absdiff(frame1,frame2)   #İki kare arasındaki mutlak farkı hesaplar ve bu farkı diff değişkenine atar.
    gray = cv2.cvtColor(diff,cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray,(5,5),0)   #Gri tonlamalı görüntüyü Gaussian bulanıklığı ile bulanıklaştırır. Bu, küçük gürültüleri azaltmak için kullanılır.
    _,thresh = cv2.threshold(blur,20,255,cv2.THRESH_BINARY)
    dilated = cv2.dilate(thresh,None,iterations=3)  #İkili görüntüyü genişletir (dilate eder). Bu, nesnelerin daha belirgin hale gelmesini sağlar.
    contours,_= cv2.findContours(dilated, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)    
    
    for countour in contours:
        (x,y,w,h) = cv2.boundingRect(countour)

        if cv2.contourArea(countour) < 700:
            continue 

        movement_count = len(contours)

       # cv2.rectangle(frame1,(x,y),(x+w,y+h),(0,255,0),2)
        #cv2.putText(frame1,"status : {}".format('Movement'),(10,20),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),3)
        #cv2.putText(frame1, f'Movements: {movement_count}', (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 255), 2)
       # cv2.putText(frame1,"press q to exit ", (10,60), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255), 2)
    cv2.drawContours(frame1,contours,-1,(0,255,0),2)

    cv2.imshow("Demo",gray)
    frame1  = frame2
    ret,frame2 = cap.read()
    


    key = cv2.waitKey(40)
    # press q to exit the demo
    if key == ord('q'):
        break  
 
cv2.destroyAllWindows()
 
cap.release()