import cv2 
threshold_value = 137
threshold_type = 0
threshold_types = [cv2.THRESH_BINARY,cv2.THRESH_BINARY_INV,cv2.THRESH_TOZERO_INV]
window_name = 'filters'
cv2.namedWindow(window_name)

cap = cv2.VideoCapture(0)
key = 0 
cv2.namedWindow(window_name,cv2.WINDOW_AUTOSIZE)
while (True):
    ret, frame = cap.read()
    gray_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    thresh,bla = cv2.threshold(gray_frame, threshold_value,255,threshold_types[threshold_type])


    cv2.imshow(window_name,bla)

    if key == ord('q'):
        break
    
    key = cv2.waitKey(1)



cap.release()

cv2.destroyAllWindows()
cv2.waitKey(1)