# Practical 1
* [Github Link] (https://github.com/g3n3s1s-a/cv_course)
* [Video Link] (https://drive.google.com/file/d/1SI7xLJmaHpEkeqWJj_mDXu0Ax7EHRHc2/view?usp=sharing)

## Questions
1. Check if HSV color space works better. Can you ignore one or two channels when working in HSV color space (btw – think how to "ignore” the selected channel)?
If so, why?
HSV worked better for me because the peaks were much cleaner and easier to identify in the histogram. In RGB, lighting changes affect all three channels simultaneously, making it harder to isolate a specific color. In HSV, lighting changes primarily affect only the V channel, while the H channel remains relatively stable. I think you can ignore one or two channels by widening their range to the maximum values. 

2. What happens when you present two objects of the same color to the camera?
My code was able to pick them up. 
Since the mask is created based on the HSV color range using cv2.inRange(), any pixel that falls within the specified color range will be included in the mask, regardless of how many separate objects there are



