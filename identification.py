import cv2
import numpy as np
from sys import argv

path = argv[1]
test = cv2.imread(path, cv2.IMREAD_GRAYSCALE)

correlation = cv2.imread(f"matrices/{path.split('/')[-1].split('_')[1]}.png", cv2.IMREAD_GRAYSCALE)

h, w = correlation.shape

for i in range(h):
	for j in range(w):
		correlation[i, j] = (255 - abs(correlation[i, j] - test[i, j]))

confidence = correlation.mean() / 255
threshold = 0.5
print(f"\nConfidence: {confidence}\nThreshold: {threshold}, thus ", end='')
if confidence > threshold:
	print(f"this is a {path.split('/')[-1].split('_')[1]}\n")
else:
	print(f"this is NOT a {path.split('/')[-1].split('_')[1]}\n")
