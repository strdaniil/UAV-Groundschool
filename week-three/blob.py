import cv2
import numpy as np
 

image = cv2.imread("cones.png", cv2.IMREAD_GRAYSCALE)
params = cv2.SimpleBlobDetector_Params()
 
# params.minThreshold = 10
# params.maxThreshold = 200
 
# params.filterByArea = True
# params.minArea = 10
 
# params.filterByCircularity = True
# params.minCircularity = 0.1
 
# params.filterByConvexity = True
# params.minConvexity = 0.87
 
# params.filterByInertia = True
# params.minInertiaRatio = 0.01

params.minThreshold = 0
params.maxThreshold = 255

params.filterByArea = True
params.minArea = 100
params.maxArea = 10000

params.filterByCircularity = False
params.filterByConvexity = False
params.filterByInertia = False
params.filterByColor = False

height, width = image.shape
params.minDistBetweenBlobs = width * 0.12
params.minArea = height * width * 0.005
params.maxArea = height * width * 0.15

params.minRepeatability = 3
params.thresholdStep = 5
 
detector = cv2.SimpleBlobDetector_create(params)
 
keypoints = detector.detect(image)
 
output = cv2.drawKeypoints(image, keypoints, np.array([]), (0, 0, 255),
                           cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
 
cv2.imshow("Blobs Detected", output)
cv2.waitKey(0)
cv2.destroyAllWindows()