import cv2, numpy as np
import matplotlib.pyplot as plt

src = cv2.imread("apple.png")

converted = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)

color_ranges = [
    [[0, 50, 41],   [10, 255, 255]],   # Red (first range)
    [[170, 50, 41], [179, 255, 255]],  # Red (second range)
    [[11, 50, 41],  [24, 255, 255]],   # Orange
    [[25, 50, 41],  [34, 255, 255]],   # Yellow
    [[35, 50, 41],  [85, 255, 255]],   # Green
    [[86, 50, 41],  [99, 255, 255]],   # Cyan
    [[100, 50, 41], [129, 255, 255]],  # Blue
    [[130, 50, 41], [169, 255, 255]],  # Purple/pink
    [[0, 0, 0],    [179, 255, 40]],   # Black
    [[0, 0, 41],   [179, 49, 199]],   # Gray
    [[0, 0, 200],  [179, 49, 255]],   # White
]

masked_slices = []

red1 = masked = cv2.inRange(converted, np.array(color_ranges[0][0]), np.array(color_ranges[0][1]))
red2 = masked = cv2.inRange(converted, np.array(color_ranges[1][0]), np.array(color_ranges[1][1]))
red_mask = cv2.bitwise_or(red1, red2)
if cv2.countNonZero(red_mask) > 100:
    masked_slices.append(red_mask)

for color in color_ranges[2:]:
    masked = cv2.inRange(converted, np.array(color[0]), np.array(color[1]))
    if cv2.countNonZero(masked) > 100:
        masked_slices.append(masked)

for i in range(len(masked_slices)):
    ys, xs = np.where(masked_slices[i] > 0)
    center_x, center_y = xs.mean(), ys.mean()
    masked_slices[i] = [masked_slices[i], (center_x, center_y)]
    

cols = 3
rows = (len(masked_slices) + cols - 1) // cols

if masked_slices:
    plt.figure(figsize=(12, rows * 4))

    for i, (mask, (x, y)) in enumerate(masked_slices):
        colored = cv2.bitwise_and(src, src, mask=mask)
        colored = cv2.cvtColor(colored, cv2.COLOR_BGR2RGB)

        ax = plt.subplot(rows, cols, i + 1)
        ax.imshow(colored)
        ax.set_title(f"Color {i + 1}")
        ax.set_xlabel(f"Center: ({x:.1f}, {y:.1f})")
        ax.set_xticks([])
        ax.set_yticks([])

    plt.tight_layout()
    plt.show()