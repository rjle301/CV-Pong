import cv2
import mediapipe

cap = cv2.VideoCapture(1)

mpHands = mediapipe.solutions.hands
hands = mpHands.Hands(max_num_hands=10)
mpDraw = mediapipe.solutions.drawing_utils



def main():
    prev_hand_location = (0, 0)

    run = True
    while run:
        success, img = cap.read()

        hand_location = get_hand_location(img)
        if hand_location is not None:
            prev_hand_location = hand_location

        update(trees, prev_hand_location, img)


main()


cv2.destroyWindow("Image")