import cv2
import skimage
from skimage import measure
import numpy as np
import matplotlib.pyplot as plt

# Step 1: preprocessing 
"""
The first step involves thresholding and converting the image to a binary image, as we did in Practical
00. The result will be a binary image with each object of interest expressed as a connected component of
white pixels. Intensity of images that you will process in class may have some linear trend, thus its removal
should help in getting a better binary image (do you remember one of the example dyadic point
operators?). You may also see the need for histogram equalization before binarization. As an example,
the binary image can be obtained in the following way, using the Fisher ratio-based thresholding
approach (we use Otsu’s implementation):
"""

# read the image in but this reads it in rgb 
img = cv2.imread("pills.png")

#turn to greyscale 
grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# doing this cuz said in instructions but maybe cuz some pills r pink?
#equalized = cv2.equalizeHist(grey)

#otsu finds the threshold and it will seperate the pills (makke them white) and the background 0, basically maximizing the intensity btw background
#and foreground??
ret1, binary = cv2.threshold(grey, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

#plt.imshow(binary, cmap='grey')
#plt.title("Binary Image")
#plt.show()

# Step 2: Segmentation
n = 1 or 2
labels = measure.label(binary, n)
#print(labels.max())
# labels finds all the connected components 
#plt.imshow(labels, cmap='nipy_spectral')
#plt.title("Connected Components")
#plt.show()

# Step 3: Feature extraction
features = measure.regionprops(labels)

# step 4: classification
'''
If we use regionprops to get major and minor axis length for each connected component, and plot the
histogram of their ratio, we see that this single feature is sufficient to classify these shapes perfectly:

Now, when we have the features extracted, we can build a simple classifier to classify the objects: just check
if the ratio is above, say, 1.5. If it is, the object is elliptical. If it is not, the object is round.
'''
ratios = []

for region in features:
    major = region.major_axis_length
    minor = region.minor_axis_length

    if minor > 0:   # avoid division by zero
        ratio = major / minor
        ratios.append(ratio)

plt.hist(ratios, bins=10)
plt.xlabel("Major/Minor Axis Length Ratio")
plt.ylabel("Number of Objects")
plt.title("Histogram of Shape Ratios")
plt.show()
