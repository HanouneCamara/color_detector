import cv2

#ouvre la webcam
def open_camera(index=0):
    cap = cv2.VideoCapture(index, cv2.CAP_V4L2)
    if not cap.isOpened():
        raise IOError("Impossible d'ouvrir la caméra")
    return cap

#lire une image depuis la caméra
def read_frame(cap):
    ret, frame = cap.read()
    return ret, frame

#fermer la caméra
def close_camera(cap):
    cap.release()
    cv2.destroyAllWindows()