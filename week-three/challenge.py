import cv2
import numpy as np

image = cv2.imread("image.png")
if image is None:
    raise FileNotFoundError("Could not load image.png")

hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
output = image.copy()

color_ranges = {
    "Red": [
        ([0, 100, 50], [10, 255, 255]),
        ([170, 100, 50], [179, 255, 255])
    ],
    "Yellow": [
        ([15, 100, 50], [35, 255, 255])
    ],
    "Purple": [
        ([110, 60, 40], [160, 255, 255])
    ]
}

kernel = np.ones((3, 3), dtype=np.uint8)
min_area = image.shape[0] * image.shape[1] * 0.005

for name, ranges in color_ranges.items():
    mask = np.zeros(image.shape[:2], dtype=np.uint8)

    for lower, upper in ranges:
        color_mask = cv2.inRange(
            hsv, np.array(lower, dtype=np.uint8),
            np.array(upper, dtype=np.uint8)
        )
        mask = cv2.bitwise_or(mask, color_mask)

    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

    contours, _ = cv2.findContours(
        mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
    )

    for contour in contours:
        if cv2.contourArea(contour) < min_area:
            continue

        cv2.drawContours(output, [contour], -1, (0, 255, 0), 2)

        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(output, (x, y), (x + w, y + h),
                      (0, 255, 0), 2)
        cv2.putText(output, name, (x, max(y - 5, 15)),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                    (0, 255, 0), 1)

cv2.imshow("Objects Detected", output)
cv2.waitKey(0)
cv2.destroyAllWindows()