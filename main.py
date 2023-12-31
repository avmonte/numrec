import cv2
import numpy as np
from sys import argv

# Reads the image and identifies the props
path = argv[1]
image = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
height, width = image.shape

size = 512
n = 32  ##
blank_img = np.zeros(shape=(n, n, 1), dtype=np.int16)


def crop():
	global image, height, width
	center_h = height // 2
	center_w = width // 2
	image = image[(center_h - (size // 2)):(center_h + (size // 2)), (center_w - (size // 2)):(center_w + (size // 2))]
	height, width = image.shape


def color_scale():
	min_val, max_val, _, _ = cv2.minMaxLoc(blank_img)

	h, w, _ = blank_img.shape
	for col in range(h):
		for row in range(w):
			blank_img[col, row] = ((blank_img[col, row] - min_val) / (max_val - min_val)) * 255


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
			k = size // n
			h = i // k
			w = j // k

			nop = (i - 1) % k + (j - 1) % k
			blank_img[h, w] = (nop * blank_img[h, w] + image[i, j]) // (nop + 1)


def main():

	crop()
	# maximize()
	merge()
	color_scale()

	# Save
	try:
		cv2.imwrite(f"processed/cellsmerged16_{path.split('/')[-1]}", blank_img)
	except:
		print("The filename is not standardized")


main()
