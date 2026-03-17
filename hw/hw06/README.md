# homework 06
## forward warping results
<img width="870" height="356" alt="Screenshot 2026-03-16 at 11 52 53 PM" src="https://github.com/user-attachments/assets/91c351d5-563b-4f76-ba97-510df7aa79d5" />
## inverse warping results
<img width="866" height="358" alt="Screenshot 2026-03-16 at 11 50 47 PM" src="https://github.com/user-attachments/assets/4c0d01e4-fce3-43d4-9839-051baed118dd" />

## reflection
At first I was a little confused on how to do this assignment because to be honest, I don't remember what we covered before break. After watching this [quick video](https://www.youtube.com/watch?v=9iN-dAKqcwM),
I was able to quickly realized that forward warping maps pixels from the original image to a new location T(p) = p'. However, it can create holes as seen above. 
On the other hand, inverse warping maps pixels from the destination image back to the source to ensure every output pixel is filled so we don't have holes T(p') = p. Then it become obvious (i looked at my notes) that to apply inverse warping,
we simply use the inverse of the transformation matrix and swap the source and dst coordinates. It is cool to see how something so simple can greatly increase the quality of our final image. 
