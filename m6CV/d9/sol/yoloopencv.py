import cv2 
import numpy as np

cap = cv2.VideoCapture(0)

classesFile = 'C:/Users/emrre/Downloads/opencvv/coco.names' 
classes = []

with open(classesFile, 'rt') as F:
    classes = F.read().rstrip('\n').split('\n')
print(classes)


m_c = 'yolov3.cfg'
m_w = 'yolov3.weights'

net = cv2.dnn.readNetFromDarknet(m_c,m_w)

net.setPreferableBackend(cv2.dnn.DNN_BACKEND_OPENCV)
net.setPreferableTarget(cv2.dnn.DNN_TARGET_CPU)


def objectfinder(outs,img):
    height , width, channels = img.shape
    boxes = []
    class_ids = []
    confidences = []

    for out in outs:
        
        for detection in out:
            scores = detection[5:]

            class_id = np.argmax(scores)
            confidence = scores[class_id]

            if confidence > 0.5:
                c_x = int(detection[0]*width)
                c_y = int(detection[1]*height)
                w = int(detection[2]*width)
                h = int(detection[3]*height)

                #cv2.circle(img1, (c_x,c_y), 10,(0,255,0),2)
                x = int(c_x-w / 2)
                y = int(c_y-h / 2)

                boxes.append([x,y,w,h],)
                confidences.append(float(confidence))

                class_ids.append(class_id)

                cv2.rectangle(img,(x,y),(x+w , y+h),(0,255,0),3)



while True:

    succes , img = cap.read()


    blob = cv2.dnn.blobFromImage(img, 1/25, (416,416),(0,0,0),1,crop = False)

    net.setInput(blob)

    layer_names = net.getLayerNames()
    outputlayers = [layer_names[i[0]-1] for i in net.getUnconnectedOutLayers()]

    outs = net.forward(outputlayers) 


    boxes = []

    objectfinder(outs,img)

    cv2.imshow('yoloyolo', img )

    cv2.waitKey(2   )

    k = cv2.waitKey(30)

    if k == ord('Q') or k == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()
cv2.waitKey(1)