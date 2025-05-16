import cv2
import webcolors
from webcolors import IntegerRGB
from camera import open_camera, read_frame, close_camera

def closest_color(requested_rgb):
    min_colors = {}
    for name in webcolors.names():
        r_c, g_c, b_c = webcolors.name_to_rgb(name)
        rd = (r_c - requested_rgb[0]) ** 2
        gd = (g_c - requested_rgb[1]) ** 2
        bd = (b_c - requested_rgb[2]) ** 2
        min_colors[(rd + gd + bd)] = name
    return min_colors[min(min_colors.keys())]


def get_color_name(rgb):
    try:
        # Convertir le tuple RGB standard en IntegerRGB pour compatibilité
        rgb_obj = IntegerRGB(*rgb)
        color_name = webcolors.rgb_to_name(rgb_obj)
    except ValueError:
        color_name = closest_color(rgb)
    return color_name

def main():
    try:
        cap = open_camera()

        cv2.namedWindow("Flux Vidéo", cv2.WINDOW_NORMAL)

        while True:
            ret, frame = read_frame(cap)
            if not ret:
                print("Erreur lors de la lecture de l'image")
                break

            # Calculer le centre
            height, width, _ = frame.shape
            center_x = width // 2
            center_y = height // 2

            # Lire la couleur du pixel au centre
            b, g, r = frame[center_y, center_x]
            color_text = f"B:{b} G:{g} R:{r}"

            # Obtenir le nom de la couleur
            color_name = get_color_name((r, g, b))
            
            # Dessiner le carré coloré
            cv2.rectangle(frame, (10, 10), (60, 60), (int(b), int(g), int(r)), -1)

            # Afficher les valeurs RGB et le nom de la couleur
            cv2.putText(
                frame,
                f"{color_text} - {color_name}",
                (70, 40),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (255, 255, 255),
                2,
                cv2.LINE_AA
            )

            # Marquer le centre de l'image
            cv2.circle(frame, (center_x, center_y), 5, (0, 255, 0), -1)

            # Afficher le cadre modifié
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
