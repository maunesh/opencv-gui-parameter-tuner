"""
How to run:
python blur_image.py <image path>
"""

import argparse
import cv2
import os

from guiutils import SmoothImage

def main():
    parser = argparse.ArgumentParser(description='Visualize smoothed image with various filter sizes')
    parser.add_argument('filename')

    args = parser.parse_args()

    img = cv2.imread(args.filename, cv2.IMREAD_GRAYSCALE)

    cv2.imshow('input', img)

    blur_image = SmoothImage(img, average_filter_size=5, gaussian_filter_size=1, median_filter_size=1, bilateral_filter_size=1)
    #edge_finder = EdgeFinder(img, filter_size=13, threshold1=28, threshold2=115)

    print "Filter Sizes:"
    print "Average Blur Filter Size: %f" % blur_image.averageFilterSize()
    print "Gaussian Blur Filter Size: %f" % blur_image.gaussianFilterSize()
    print "Gaussian Blur Filter Size: %f" % blur_image.gaussianFilterSize()
    print "Median Blur Filter Size: %f" % blur_image.medianFilterSize()
    print "Bilateral Filter Size: %f" % blur_image.bilateralFilterSize()

    (head, tail) = os.path.split(args.filename)

    (root, ext) = os.path.splitext(tail)

    blurred_filename = os.path.join("output_images", root + "-blurred" + ext)
    
    cv2.imwrite(blurred_filename, blur_image.blurred_image())

    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
