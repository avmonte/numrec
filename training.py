import cv2
from os import listdir

dataset = listdir("processed/")


def scale():
	min_val, max_val, _, _ = cv2.minMaxLoc(matrix)

	h, w = matrix.shape
	for col in range(h):
		for row in range(w):
			print(matrix[col, row], end='  ')
			matrix[col, row] = ((matrix[col, row] - min_val) / (max_val - min_val)) * 255


matrix = cv2.imread(f"processed/{dataset[0]}", cv2.IMREAD_GRAYSCALE)

count = 1
for i in dataset[1:]:
	image = cv2.imread(f"processed/{i}", cv2.IMREAD_GRAYSCALE)
	h, w = image.shape

	for col in range(h):
		for row in range(w):
			matrix[col, row] = ((count * matrix[col, row]) + image[col, row]) // (count + 1)

	count += 1

scale()

cv2.imwrite(f"matrices/{dataset[0].split('_')[1]}.png", matrix)
