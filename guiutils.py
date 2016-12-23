import cv2

class SmoothImage:
    def __init__(self, image, average_filter_size=1, gaussian_filter_size=1, median_filter_size=1, bilateral_filter_size=1):
        self.image = image
        self._average_filter_size = average_filter_size
        self._gaussian_filter_size = gaussian_filter_size
        self._median_filter_size = median_filter_size
        self._bilateral_filter_size = bilateral_filter_size 

        def onchangeAvgFltrSz(pos):
            self._average_filter_size = pos
            self._average_filter_size += (self._average_filter_size + 1) % 2        # make sure the filter size is odd
            self._render()

        def onchangeGaussFltrSz(pos):
            self._gaussian_filter_size = pos
            self._gaussian_filter_size += (self._gaussian_filter_size + 1) % 2      # make sure the filter size is odd
            self._render()

        def onchangeMdnFltrSz(pos):
            self._median_filter_size = pos
            self._median_filter_size += (self._median_filter_size + 1) % 2          # make sure the filter size is odd
            self._render()

        def onchangeBltrlFltrSz(pos):
            self._bilateral_filter_size = pos
            self._bilateral_filter_size += (self._bilateral_filter_size + 1) % 2    # make sure the filter size is odd
            self._render()

        cv2.namedWindow('blurred')

        cv2.createTrackbar('average_filter_size', 'blurred', self._average_filter_size, 20, onchangeAvgFltrSz)
        cv2.createTrackbar('gaussian_filter_size', 'blurred', self._gaussian_filter_size, 20, onchangeGaussFltrSz)
        cv2.createTrackbar('median_filter_size', 'blurred', self._median_filter_size, 20, onchangeMdnFltrSz)
        cv2.createTrackbar('bilateral_filter_size', 'blurred', self._bilateral_filter_size, 20, onchangeBltrlFltrSz)
        
        self._render()

        print "Adjust the parameters as desired.  Hit any key to close."

        cv2.waitKey(0)

        cv2.destroyWindow('blurred')

    def blurred_image(self):
        return self._blurred_image

    def averageFilterSize(self):
        return self._average_filter_size

    def gaussianFilterSize(self):
        return self._gaussian_filter_size

    def medianFilterSize(self):
        return self._median_filter_size

    def bilateralFilterSize(self):
        return self._bilateral_filter_size
        
    def _render(self):
        self._blurred_image = cv2.blur(self.image, (self._average_filter_size, self._average_filter_size))
        self._blurred_image = cv2.GaussianBlur(self._blurred_image, (self._gaussian_filter_size, self._gaussian_filter_size), 0)
        self._blurred_image = cv2.medianBlur(self._blurred_image, self._median_filter_size)
        self._blurred_image = cv2.bilateralFilter(self._blurred_image, 5, self._bilateral_filter_size, self._median_filter_size)
            
        cv2.imshow('blurred', self._blurred_image)



class EdgeFinder:
    def __init__(self, image, filter_size=1, threshold1=0, threshold2=0):
        self.image = image
        self._filter_size = filter_size
        self._threshold1 = threshold1
        self._threshold2 = threshold2

        def onchangeThreshold1(pos):
            self._threshold1 = pos
            self._render()

        def onchangeThreshold2(pos):
            self._threshold2 = pos
            self._render()

        def onchangeFilterSize(pos):
            self._filter_size = pos
            self._filter_size += (self._filter_size + 1) % 2  # make sure the filter size is odd
            self._render()

        cv2.namedWindow('edges')

        cv2.createTrackbar('threshold1', 'edges', self._threshold1, 255, onchangeThreshold1)
        cv2.createTrackbar('threshold2', 'edges', self._threshold2, 255, onchangeThreshold2)
        cv2.createTrackbar('filter_size', 'edges', self._filter_size, 20, onchangeFilterSize)

        self._render()

        print "Adjust the parameters as desired.  Hit any key to close."

        cv2.waitKey(0)

        cv2.destroyWindow('edges')
        cv2.destroyWindow('smoothed')

    def threshold1(self):
        return self._threshold1

    def threshold2(self):
        return self._threshold2

    def filterSize(self):
        return self._filter_size

    def edgeImage(self):
        return self._edge_img

    def smoothedImage(self):
        return self._smoothed_img

    def _render(self):
        self._smoothed_img = cv2.GaussianBlur(self.image, (self._filter_size, self._filter_size), sigmaX=0, sigmaY=0)
        self._edge_img = cv2.Canny(self._smoothed_img, self._threshold1, self._threshold2)
        cv2.imshow('smoothed', self._smoothed_img)
        cv2.imshow('edges', self._edge_img)

