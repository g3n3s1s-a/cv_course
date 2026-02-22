#Computer Vision Course (CSE 40535/60535)
# University of Notre Dame, Fall 2024
# ________________________________________________________________
# Adam Czajka, Andrey Kuehlkamp, September 2017 - 2024

# Here are your tasks:
#
# Task 2a:
# - Select one object that you want to track and set the RGB
#   channels to the selected ranges (found by colorSelection.py).
# - Check if HSV color space works better. Can you ignore one or two
#   channels when working in HSV color space? Why?
# - Try to track candies of different colors (blue, yellow, green).
# 
# Task 2b:
# - Adapt your code to track multiple objects of *the same* color simultaneously, 
#   and show them as separate objects in the camera stream.
#
# Task 2c:
# - Adapt your code to track multiple objects of *different* colors simultaneously,
#   and show them as separate objects in the camera stream. Make your code elegant 
#   and requiring minimum changes when the number of different objects to be detected increases.
#
# Task for students attending 60000-level course:
# - Choose another color space (e.g., LAB or YCrCb), modify colorSelection.py, select color ranges 
#   and after some experimentation say which color space was best (RGB, HSV or the additional one you selected).
#   Try to explain the reasons why the selected color space performed best. 

import cv2
import numpy as np

cam = cv2.VideoCapture(0)

while (True):
    retval, img = cam.read()

    res_scale = 0.5 # rescale the input image if it's too large
    img = cv2.resize(img, (0,0), fx = res_scale, fy = res_scale)


    #######################################################
    # Use colorSelection.py to find good color ranges for your object(s):

    # Detect selected color (NOTE: OpenCV uses BGR instead of RGB)
    # This example is tuned to blue, in a relatively dark room
    #lower = np.array([30, 100, 70])
    #upper = np.array([120, 210, 180])
    #objmask = cv2.inRange(img, lower, upper)

    # Uncomment this if you want to use HSV
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    #lower = np.array([40,90,150])
    #upper = np.array([50,200,180])
    #lower = np.array([20,70,70])
    #upper = np.array([40,180,180])
    #objmask = cv2.inRange(hsv, lower, upper)


    # to select multiple colors
    color_ranges = {
    "green": {
        "lower": np.array([20, 70, 70]),
        "upper": np.array([40, 180, 180]),
        "draw_color": (0, 255, 0)
    },
    "blue": {
        "lower": np.array([105, 130, 130]),
        "upper": np.array([120, 190, 200]),
        "draw_color": (255, 0, 0)
    },
    "orange": {
        "lower": np.array([0, 150, 180]),
        "upper": np.array([15, 220, 200]),
        "draw_color": (0, 255, 255)
    }
}
    #######################################################

    
    # You may use this for debugging
    #cv2.imshow("Binary image", objmask)

    # Resulting binary image may have large number of small objects.
    # You may check different morphological operations to remove these unnecessary
    # elements. You may need to check your ROI defined in step 1 to
    # determine how many pixels your object may have.
    #kernel = np.ones((5,5), np.uint8)
    #objmask = cv2.morphologyEx(objmask, cv2.MORPH_CLOSE, kernel=kernel)
    #objmask = cv2.morphologyEx(objmask, cv2.MORPH_DILATE, kernel=kernel)
    #cv2.imshow("Image after morphological operations", objmask)

    # find connected components
    #cc = cv2.connectedComponents(objmask)
    #ccimg = cc[1].astype(np.uint8)

    # Find contours of these objects
    #contours, hierarchy = cv2.findContours(ccimg,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)[-2:]

    # We are using [-2:] to select the last two return values from the above function to make the code work with
    # both opencv3 and opencv4. This is because opencv3 provides 3 return values but opencv4 discards the first.

    # You may display the countour points if you want:
    #cv2.drawContours(img, contours, -1, (0,255,0), 3)

    # Ignore bounding boxes smaller than "minObjectSize"
    minObjectSize = 20;
    
    for color_name, color_info in color_ranges.items():
      objmask = cv2.inRange(hsv,color_info["lower"], color_info["upper"])

      kernel = np.ones((5,5), np.uint8)
      objmask = cv2.morphologyEx(objmask, cv2.MORPH_CLOSE, kernel)
      objmask = cv2.morphologyEx(objmask, cv2.MORPH_DILATE, kernel)

      contours, _ = cv2.findContours(objmask,
                                    cv2.RETR_TREE,
                                    cv2.CHAIN_APPROX_SIMPLE)

      #######################################################
      # TIP: think if the "if" statement
      # can be replaced with a "for" loop
      for c in contours:
        #######################################################
    
        # use the biggest object to draw a rectangle
        #c = max(contours, key = cv2.contourArea)
        x, y, w, h = cv2.boundingRect(c)

        #######################################################
        # TIP: you want to get bounding boxes
        # of ALL contours (not only the first one)
        #######################################################

        # Do not show very small objects
        if w > minObjectSize or h > minObjectSize:
            cv2.rectangle(img, (x, y), (x+w, y+h), color_info["draw_color"], 2)
            cv2.putText(img,            # image
            color_name,        # text
            (x, y-10),                  # start position
            cv2.FONT_HERSHEY_SIMPLEX,   # font
            0.7,                        # size
            color_info["draw_color"],                # BGR color
            2,                          # thickness
            cv2.LINE_AA)                # type of line

    cv2.imshow("Live WebCam", img)

    action = cv2.waitKey(1)
    if action==27:
        break
    
cam.release()
cv2.destroyAllWindows()
