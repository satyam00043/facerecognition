import cv2
from tkinter import*
from tkinter import ttk
from tkinter import messagebox
import numpy as np
import os 
import sqlite3
class Detect:

    facedetect=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    cam=cv2.VideoCapture(0);
    rec=cv2.face.LBPHFaceRecognizer_create()
    rec.read("recognizer/trainingData.yml")


    def getprofile(id):
        conn=sqlite3.connect("sqlite.db")
        cursor=conn.execute("select * from students where id=?",(id,))

        profile=None
        for row in cursor:
            profile=row
        conn.close()
        return profile



    while(True):
        ret, img = cam.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = facedetect.detectMultiScale(gray, 1.3, 5)
        for (x,y,w,h) in faces:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
                id,conf=rec.predict(gray[y:y+h,x:x+w])
                profile=getprofile(id)
                print(profile)
                if(profile!=None):
                    cv2.putText(img,"Name: "+str(profile[1]),(x,y+h+20),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,125),2)
                    cv2.putText(img,"age: "+str(profile[2]),(x,y+h+45),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,125),2)       
        cv2.imshow("FACE",img);
        if(cv2.waitKey(1)==ord('q')):
            break;
    cam.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    root=Tk()
    root.title("Studen data")
    obj=Detect(root)
    root.mainloop()          
        