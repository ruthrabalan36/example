import cv2
import mediapipe as mp

# Initialize Mediapipe Hands and drawing utilities
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

# Start video capture
cap = cv2.VideoCapture(0)

with mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7) as hands:
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            print("Failed to capture video.")
            break

        # Flip the frame horizontally for a mirror-like effect
        frame = cv2.flip(frame, 1)
        h, w, _ = frame.shape

        # Convert the frame to RGB
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Process the frame and find hands
        result = hands.process(rgb_frame)

        # Initialize the finger count
        finger_count = 0

        if result.multi_hand_landmarks:
            for hand_landmarks in result.multi_hand_landmarks:
                # Draw hand landmarks on the frame
                mp_drawing.draw_landmarks(
                    frame, hand_landmarks, mp_hands.HAND_CONNECTIONS
                )

                # Finger tips indices in Mediapipe
                finger_tips = [8, 12, 16, 20]  # Index, Middle, Ring, and Pinky finger tips
                thumb_tip = 4

                # Get landmarks
                landmarks = hand_landmarks.landmark

                # Check the thumb
                if landmarks[thumb_tip].x < landmarks[thumb_tip - 2].x:
                    finger_count += 1

                # Check the fingers
                for tip in finger_tips:
                    if landmarks[tip].y < landmarks[tip - 2].y:  # Compare y-coordinates
                        finger_count += 1

        # Display the finger count
        cv2.putText(
            frame,
            f"Fingers: {finger_count}",
            (10, 50),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (255, 0, 0),
            2,
        )

        # Show the video frame
        cv2.imshow("Fingers Counter", frame)

        # Break the loop on pressing 'q'
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

# Release resources
cap.release()
cv2.destroyAllWindows()
