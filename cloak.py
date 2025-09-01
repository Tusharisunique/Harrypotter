import cv2
import numpy as np
import time

cloak_colors = {
    "red": [
        (0, 100, 100), (10, 255, 255),
        (160, 100, 100), (180, 255, 255)
    ],
    "green": [
        (35, 40, 40), (85, 255, 255)
    ],
    "blue": [
        (90, 50, 50), (130, 255, 255)
    ],
    "black": [
        (0, 0, 0), (180, 255, 70)
    ]
}

color_swatches = {
    "red": (0, 0, 255),
    "green": (0, 255, 0),
    "blue": (255, 0, 0),
    "black": (0, 0, 0)
}

def show_color_menu():
    swatch = np.zeros((220, 400, 3), dtype=np.uint8)
    colors = list(color_swatches.keys())

    for i, color in enumerate(colors):
        cv2.rectangle(swatch, (10, 10 + i * 50), (60, 50 + i * 50), color_swatches[color], -1)
        cv2.putText(swatch, f"{color.title()}", (70, 40 + i * 50), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 255, 255), 2)

    cv2.imshow("Choose your cloak color", swatch)
    print("\n👕 Choose the color of your cloak (type one of these): red, green, blue, black")
    color = input("👉 Enter cloak color: ").strip().lower()

    cv2.destroyWindow("Choose your cloak color")

    if color not in cloak_colors:
        print("Invalid color! Defaulting to 'blue'")
        color = "blue"

    return color

cloak_choice = show_color_menu()
cloak_ranges = cloak_colors[cloak_choice]

cap = cv2.VideoCapture(0)
time.sleep(2)

background = None
for i in range(30):
    ret, frame = cap.read()
    if not ret:
        continue
    frame = cv2.flip(frame, 1)
    background = frame

print(f"✅ Background captured. Wear your {cloak_choice.upper()} cloak now!")

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    final_mask = np.zeros_like(cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY))

    for i in range(0, len(cloak_ranges), 2):
        lower = np.array(cloak_ranges[i])
        upper = np.array(cloak_ranges[i + 1])
        mask = cv2.inRange(hsv, lower, upper)
        final_mask = cv2.bitwise_or(final_mask, mask)

    final_mask = cv2.morphologyEx(final_mask, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8), iterations=2)
    final_mask = cv2.dilate(final_mask, np.ones((3, 3), np.uint8), iterations=1)

    inverse_mask = cv2.bitwise_not(final_mask)

    cloak_area = cv2.bitwise_and(background, background, mask=final_mask)
    non_cloak_area = cv2.bitwise_and(frame, frame, mask=inverse_mask)

    final_output = cv2.addWeighted(cloak_area, 1, non_cloak_area, 1, 0)

    cv2.imshow("🧥 Invisibility Cloak - Press 'q' to Quit", final_output)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()