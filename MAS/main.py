import cv2
from deepface import DeepFace
import time
import requests

# --- CONFIG ---
DB_PATH = "faces_db"
MODEL_FACE = "VGG-Face"
DETECTOR = "opencv"
ALERT_INTERVAL = 10         # secondes minimum entre 2 alertes
TOLERANCE_COUNT = 3         # nombre de frames consécutives pour déclencher alerte
TELEGRAM_BOT_TOKEN = "**********:hsfnf************"
CHAT_IDS = ["**********", "************"]  # liste de destinataires

# --- Fonction reconnaissance faciale ---
def recognize_face(frame):
    try:
        results = DeepFace.find(
            img_path=frame,
            db_path=DB_PATH,
            model_name=MODEL_FACE,
            detector_backend=DETECTOR,
            enforce_detection=False,
            silent=True
        )
        if isinstance(results, list) and len(results) > 0 and not results[0].empty:
            identity = results[0].iloc[0]["identity"]
            return identity.split("/")[-1].split("\\")[-1]
        else:
            return "Inconnu"
    except:
        return "Erreur"

# --- Fonction d'envoi Telegram à plusieurs destinataires ---
def send_telegram_alert(frame, name="Inconnu"):
    filename = "alert.jpg"
    cv2.imwrite(filename, frame)
    for chat_id in CHAT_IDS:
        try:
            url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendPhoto"
            with open(filename, "rb") as photo:
                requests.post(
                    url,
                    data={"chat_id": chat_id, "caption": f"🚨 Alerte ! Visage détecté : {name}"},
                    files={"photo": photo}
                )
            print(f"[INFO] Alerte envoyée à chat_id {chat_id}")
        except Exception as e:
            print(f"[ERREUR] Envoi Telegram chat_id {chat_id}: {e}")

# --- Initialisation webcam ---
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("[ERREUR] Impossible d'ouvrir la webcam")
    exit()

unknown_counter = 0
last_alert_time = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break

    face_name = recognize_face(frame)

    # --- Tolérance ---
    if face_name == "Inconnu":
        unknown_counter += 1
    else:
        unknown_counter = 0

    # Déclenchement alerte si Inconnu sur plusieurs frames et intervalle respecté
    if unknown_counter >= TOLERANCE_COUNT and (time.time() - last_alert_time) > ALERT_INTERVAL:
        send_telegram_alert(frame, face_name)
        last_alert_time = time.time()
        unknown_counter = 0

    # Affichage
    cv2.putText(frame, f"Personne: {face_name}", (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)
    cv2.imshow("Surveillance DeepFace", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
