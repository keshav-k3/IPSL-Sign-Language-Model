
import os
import cv2
cap=cv2.VideoCapture(0)
directory='Image/'
while True:
    _,frame=cap.read()
    count = {
             'a': len(os.listdir(directory+"/Hello")),
             'b': len(os.listdir(directory+"/Bye")),
             'c': len(os.listdir(directory+"/ILoveYou")),
             'd': len(os.listdir(directory+"/Beautiful")),
             'e': len(os.listdir(directory+"/Win")),
             'f': len(os.listdir(directory+"/Lose")),
             'g': len(os.listdir(directory+"/Remember")),
             'h': len(os.listdir(directory+"/Sit")),
             'i': len(os.listdir(directory+"/Up")),
             'j': len(os.listdir(directory+"/Write"))

             
             }
   
    row = frame.shape[1]
    col = frame.shape[0]
    cv2.rectangle(frame,(0,40),(300,400),(255,255,255),2)
    cv2.imshow("data",frame)
    cv2.imshow("ROI",frame[40:400,0:300])
    frame=frame[40:400,0:300]
    interrupt = cv2.waitKey(10)
    if interrupt & 0xFF == ord('a'):
        cv2.imwrite(directory+'Hello/'+str(count['a'])+'.png',frame)
    if interrupt & 0xFF == ord('b'):
        cv2.imwrite(directory+'Bye/'+str(count['b'])+'.png',frame)
    if interrupt & 0xFF == ord('c'):
        cv2.imwrite(directory+'ILoveYou/'+str(count['c'])+'.png',frame)
    if interrupt & 0xFF == ord('d'):
        cv2.imwrite(directory+'Beautiful/'+str(count['d'])+'.png',frame)
    if interrupt & 0xFF == ord('e'):
        cv2.imwrite(directory+'Win/'+str(count['e'])+'.png',frame)
    if interrupt & 0xFF == ord('f'):
        cv2.imwrite(directory+'Lose/'+str(count['f'])+'.png',frame)
    if interrupt & 0xFF == ord('g'):
        cv2.imwrite(directory+'Remember/'+str(count['g'])+'.png',frame)
    if interrupt & 0xFF == ord('h'):
        cv2.imwrite(directory+'Sit/'+str(count['h'])+'.png',frame)
    if interrupt & 0xFF == ord('i'):
        cv2.imwrite(directory+'Up/'+str(count['i'])+'.png',frame)
    if interrupt & 0xFF == ord('j'):
        cv2.imwrite(directory+'Write/'+str(count['j'])+'.png',frame)
        
    


cap.release()
cv2.destroyAllWindows()