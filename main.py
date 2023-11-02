import cv2
import numpy as np
import sys

# Reads the image and identifies the props
filename = sys.argv[1]
image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
height, width = image.shape

size = 512
n = 8
blank_img = np.zeros(shape=(8, 8, 1), dtype=np.int16)


def crop():
	global image, height, width
	center_h = height // 2
	center_w = width // 2
	image = image[(center_h - (size // 2)):(center_h + (size // 2)), (center_w - (size // 2)):(center_w + (size // 2))]
	height, width = image.shape


def maximize():
	min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(image)
	avg_color = (max_val + min_val) / 2

	for i in range(height):
		for j in range(width):
			if image[i, j] < avg_color:
				image[i, j] = 0  # maximizing


def merge():
	for i in range(height):
		for j in range(width):
			k = width // n
			h = i // k
			w = j // k
			nop = (i - 1) % k + (j - 1) % k
			blank_img[h, w] = (nop * blank_img[h, w] + image[i, j]) // (nop + 1)


def main():
	crop()
	maximize()
	merge()

	# Save
	cv2.imwrite(f"example/cellsmerged_{filename.split('/')[-1]}", blank_img)


main()
