import cv2

vid = cv2.VideoCapture("araba.mp4") #Kendi araç videonuzu uygun formatlarda ekleyiniz.

object_detector = cv2.createBackgroundSubtractorMOG2(history=100,varThreshold=40 )


while True :
    
    ret , frame  = vid.read() #framleri okur
    height,width,_ = frame.shape #framleri belirli bir alana indirgerdik
    
    mask = object_detector.apply(frame) #arka plan ile filtreledik
    keskinlik , _ =cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    
    for ksk in keskinlik :
        
        alan = cv2.contourArea(ksk)
        if alan > 2000 : 
            #cv2.drawContours(frame,[ksk],-1,(255,255,0),3) #seçtiğimz renk ve kalınlıkla çecresini çizfdik
            x,y,w,h =cv2.boundingRect(ksk)
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,255,0),3) ## kare çizdik
        
        

    cv2.imshow("Ana yol",frame)
    cv2.imshow("Filtreli görğntü",mask)
    
    k = cv2.waitKey(1) & 0xFF
    
    if k == ord ("q") : # q çıkar beyaz klavyede esc kısayol atanmış 
        break 
    
