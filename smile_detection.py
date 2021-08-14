import cv2

'''Haar-cascades are classifiers that are used to detect features (of face in this case) by superimposing predefined patterns over
 face segments and are used as XML files. In our model, we shall use face, eye and smile haar-cascades, which after downloading need
 to be placed in the working directory.'''

face = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
smile = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_smile.xml')


def detect(gray, frame):
    faces = face.detectMultiScale(gray, 1.3, 5)                 # Find co-ordinates afetr detecting face
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), ((x+w), (y+h)), (255, 0, 0), 2)    # Draw rectangle around face
        roi_gray = gray[x:x+w, y:y+h]
        roi_color = frame[x:x+w, y:y+h]
        smiles = smile.detectMultiScale(roi_gray, 1.8, 20)      # Detect smile inside that face 
        for (sx, sy, sw, sh) in smiles:
            cv2.rectangle(roi_color, (sx, sy),                          # Draw rectangle around that smile
                          ((sx+sw), (sy+sh)), (0, 0, 255), 2)
    return frame


video_capture = cv2.VideoCapture(0)
while video_capture.isOpened():
    _, frame = video_capture.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    canvas = detect(gray, frame)
    cv2.imshow("Video", canvas)
    if cv2.waitKey(1) & 0xff == ord('q'):  #Click 'q' while quitting
        break
video_capture.release()
cv2.destroyAllWindows()
