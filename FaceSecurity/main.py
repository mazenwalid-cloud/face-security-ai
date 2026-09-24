from camera.camera_manager import CameraManager
from detection.face_detector import FaceDetector
from recognition.face_encoder import FaceEncoder
from recognition.face_matcher import FaceMatcher
from database.face_database import FaceDatabase
from config.settings import FACE_DATABASE_PATH, FACE_MATCH_THRESHOLD, WINDOW_NAME

def main():
    camera = CameraManager()
    detector = FaceDetector()
    encoder = FaceEncoder()
    matcher = FaceMatcher()
    database = FaceDatabase(FACE_DATABASE_PATH)

    known_encodings = database.get_encodings()

    print("Face Security AI started.")
    print("Press Q to exit.")

    while True:
        frame = camera.read()
        if frame is None:
            print("Could not access the camera.")
            break

        faces = detector.detect(frame)

        for x, y, w, h in faces:
            face_location = (y, x + w, y + h, x)
            face_encoding = encoder.encode(frame, face_location)

            name, distance = matcher.find_best_match(
                known_encodings, face_encoding
            )

            label = (
                name
                if matcher.is_match(distance, FACE_MATCH_THRESHOLD)
                else "Unknown"
            )

            detector.draw_face(frame, x, y, w, h)
            detector.draw_label(frame, label, x, y)

        camera.show(frame, WINDOW_NAME)

        if camera.should_exit():
            break

    camera.release()

if __name__ == "__main__":
    main()
