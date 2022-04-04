# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np




imagem = cv.imread('quadro1.jpg')
imagem = cv.resize(imagem,(600,800))
seedPic = np.random.randint(150,200)

cont = 0;
tempres = []
while True:
    subImagemBGR = imagem.copy()
    lstPontos = []  
    mask = np.zeros(imagem.shape[:2],np.uint8)
    
    if np.random.randint(0,100) %2 == 0:
    
        subImagemBGR[:,:,np.random.randint(0,2)] += np.random.randint(0,32)
        
    else:
        
        subImagemBGR[:,:,np.random.randint(0,2)] -= np.random.randint(0,32)
    
      
    for i in range(np.random.randint(3,13)):
        x = np.random.randint(0,600)
        y = np.random.randint(0,800)
        lstPontos.append( (x,y) )
    pontos = np.array([lstPontos])
    
   
    
    cv.fillPoly(mask,pontos,(255))
    
    res1 = cv.bitwise_and(subImagemBGR,subImagemBGR,mask = mask)
    tempres.append(res1)
    
    if cont == seedPic:
        break
    cont +=1


imgresult = imagem.copy()

h,w = imgresult.shape[:2]
video = cv.VideoWriter('./Quadro_'+str(cont)+'.mp4',cv.VideoWriter.fourcc(*'mp4v'),15,(w,h+50))

imgAssinatura = np.zeros((50,600,3),np.uint8)
cv.putText(imgAssinatura,'Mixed Glass: Heron TF Gomes',(140,25),cv.FONT_HERSHEY_SCRIPT_SIMPLEX ,1,(190,190,190),1,cv.LINE_AA )
cv.putText(imgAssinatura,'11/06/2020',(495,45),cv.FONT_HERSHEY_SCRIPT_SIMPLEX ,0.5,(190,190,190),1,cv.LINE_AA )    
cv.putText(imgAssinatura,'Seed:'+str(seedPic),(0,45),cv.FONT_HERSHEY_SCRIPT_SIMPLEX ,0.5,(190,190,190),1,cv.LINE_AA )


for i in tempres:
    
    imgresult = cv.bitwise_xor(imgresult,i).copy()
    
    quadro = cv.vconcat([imgresult,imgAssinatura])
    
    video.write(quadro)
    
    cv.imshow('Novo Quadro',quadro)
    cv.waitKey(100)
    tecla = cv.waitKey(100)
    if tecla == ord('q'):
        cv.destroyAllWindows()
        break
video.release()

    
cv.imshow('Quadro: '+str(seedPic),quadro)
cv.imwrite('Quadro_'+str(seedPic)+'.jpg', quadro)
cv.waitKey()
cv.destroyAllWindows()
