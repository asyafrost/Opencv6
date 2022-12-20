import cv2 
from tkinter import *


def Video(cap):
  cap.set(3,1280) 
  cap.set(4,700)

  ret, frame1 = cap.read()
  ret, frame2 = cap.read()

  while cap.isOpened(): 
  
    diff = cv2.absdiff(frame1, frame2) 
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY) 
    blur = cv2.GaussianBlur(gray, (5, 5), 0) 
    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY) 
    dilated = cv2.dilate(thresh, None, iterations = 3) 
  
    сontours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) 
    
    for contour in сontours:
      (x, y, w, h) = cv2.boundingRect(contour) 
    
      if cv2.contourArea(contour) < 700: 
        continue
      cv2.drawContours(frame1, сontours, -1, (0, 255, 0), 2)
      
      cv2.putText(frame1, "Status: {}".format("Dvigenie"), (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3, cv2.LINE_AA) # вставляем текст
    
    #cv2.rectangle(frame1, (x, y), (x+w, y+h), (0, 255, 0), 2) также можно было просто нарисовать контур объекта
  
    cv2.imshow("frame1", frame1)
    frame1 = frame2  #
    ret, frame2 = cap.read() #  
  
    if cv2.waitKey(1) & 0xFF == ord('q'):
      cap.release()
      cv2.destroyAllWindows()
      break
  
  


def clicked1():

  cap = cv2.VideoCapture("girl.mp4")
  Video(cap)

def clicked2():

  cap = cv2.VideoCapture(0)
  Video(cap)




def Menu():
    window = Tk()

    
    window.title("Menu")

    w = window.winfo_screenwidth()
    h = window.winfo_screenheight()
    w = w//2 # середина экрана
    h = h//2 
    w = w - 200 # смещение от середины
    h = h - 200
    window.geometry('300x300+{}+{}'.format(w, h))
    window.configure(bg='#bb85f3')

    btn = Button(window, text="Обнаружение движение с видео", padx=5, pady=5, command = clicked1, bg='#eec6ea')  
    btn.pack(anchor="center", padx=50, pady=20)

    btn2 = Button(window, text="Обнаружение движение с камеры", padx=5, pady=5, command =clicked2, bg='#eec6ea')  
    btn2.pack(anchor="center", padx=50, pady=20)

    btn3 = Button(window, text="Выход", padx=5, pady=5, command =exit, bg='#eec6ea')  
    btn3.pack(anchor="center", padx=50, pady=20)
    


    window.mainloop()

Menu()