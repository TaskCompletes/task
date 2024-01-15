import cv2
import smtplib
from random import randint

#def sendEmail():
    #s = smtplib.SMTP('smtp.gmail.com', 587)
    ## start TLS for security
    #s.starttls()
    ## Authentication
    #s.login("lovelykalai914@gmail.com", "lwxl oexq liqw vdys")
    ## message to be sent
    #message = "Message_you_need_to_send"
    ## sending the mail
    #s.sendmail("lovelykalai914@gmail.com", "narkunan9585@gmail.com", message)
    ## terminating the session
    #s.quit()

def prerequest():
    dnn = cv2.dnn.readNet('yolov4-tiny.weights', 'yolov4-tiny.cfg')
    model = cv2.dnn_DetectionModel(dnn)
    model.setInputParams(size=(416, 416), scale=1/255, swapRB=True)
    
    with open('classes.txt') as f:
        classes = f.read().strip().splitlines()
    
    capture = cv2.VideoCapture(0)
    
    capture.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
    color_map = {}
    
    while True:
        # frame capture
        _, frame = capture.read() 
        frame = cv2.flip(frame,1)
    
        # object detection
        class_ids, confidences, boxes = model.detect(frame)
        j = 1
        for id, confidence, box in zip(class_ids, confidences, boxes):
            x, y, w, h = box
            obj_class = classes[id]
    
            if obj_class not in color_map:
                color = (randint(0, 255), randint(0, 255), randint(0, 255))
                color_map[obj_class] = color
            else:
                color = color_map[obj_class]
                
            if obj_class.title() == 'Person' and j == 1:
                print('somrthing is working')
                procteringActive = True
                j = j + 1
            if procteringActive: 
               cv2.putText(frame, f'{obj_class.title()} {format(confidence, ".2f")}', (x, y-10), cv2.FONT_HERSHEY_DUPLEX, 1, color, 2)
               cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
      
