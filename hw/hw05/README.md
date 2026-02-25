Doing this activity really helped me understand how active contours work in practice. To be honest, I was confused about the snakes but know I know that the snake needs a good starting curve, 
so converting the bounding box correctly and keeping track of rows vs. columns was important. Switching the x and y when trying to make the curve did trip me up.
I also learned that the parameters like alpha and beta really change how the contour behaves like if its too stiff and it won’t follow the object, but if it's too flexible, it can get messy. 
Seeing the contour gradually adjust to the edges of the object made the process feel much more intuitive, and I got a better sense of how preprocessing and careful setup matter in segmentation.

Below is a screenshot of the resulting image. The png file is in this dir. It was too big to upload here :( 
<img width="1277" height="693" alt="Screenshot 2026-02-24 at 8 49 02 PM" src="https://github.com/user-attachments/assets/e045a94b-d3a4-455f-ac63-16e4b456a5dc" />

