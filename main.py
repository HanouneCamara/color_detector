import cv2
from camera import open_camera, read_frame, close_camera

def main():
    try:
        cap = open_camera()

        cv2.namedWindow("Flux Vidéo", cv2.WINDOW_NORMAL)

        while True:
            ret, frame = read_frame(cap)
            if not ret:
                print("Erreur lors de la lecture de l'image")
                break

            cv2.imshow("Flux Vidéo", frame)
            
            if cv2.getWindowProperty("Flux Vidéo", cv2.WND_PROP_VISIBLE) < 1:
                break

            key = cv2.waitKey(1) & 0xFF
            if key == ord('q'):
                break

    except Exception as e:
        print(f"Erreur : {e}")
    finally:
        close_camera(cap)

if __name__ == "__main__":
    main()
