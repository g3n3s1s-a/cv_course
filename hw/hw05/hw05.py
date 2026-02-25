import numpy as np
import matplotlib.pyplot as plt
from skimage.color import rgb2gray
from skimage import data
from skimage.filters import gaussian
from skimage.segmentation import active_contour
import matplotlib.image as mpimg
from skimage import draw


def yolo2xyxy(x: float, y: float, w: float, h: float, img_size: tuple) -> list:
  '''
    Transform YOLO bounding box format annotations to xyxy format.
    YOLO format: see https://docs.ultralytics.com/datasets/detect/#ultralytics-yolo-format
    xyxy format: (x1,y1) -> top-left coordinate, (x2,y2) -> bottom-right coordinate

  '''

  ### COMPLETE CODE HERE ###
  # yolo returns normalized x and y from image so we to unnormalize
  img_h = img_size[0]
  img_w = img_size[1]

  notNorm_x_center = x * img_w
  notNorm_y_center = y * img_h

  notNorm_w = w * img_w
  notNorm_h = h * img_h

  # now we need to get the top left and bottom right given the centers

  #apparently top left is (0,0) in images
  x1 = notNorm_x_center - notNorm_w/2
  y1 = notNorm_y_center - notNorm_h/2

  x2 = notNorm_x_center + notNorm_w/2
  y2 = notNorm_y_center + notNorm_h/2

  return [x1,y1,x2,y2]


def get_curve_from_bbox(x1: int, y1: int, x2: int, y2: int) -> np.array:
  ''' Output is a [r,c] array of points describing a parametric curve. '''

  curve = []
  """
   ------
  |     |
  |     |
   ------
  """
  #1. top edge 
  xs = np.linspace(x1,x2, 100)
  for x in xs:
    curve.append([y1,x])

  #2. right edge
  ys = np.linspace(y1,y2,100)
  for y in ys:
    curve.append([y,x2])

  #3. bottom edge
  xs = np.linspace(x2,x1,100)
  for x in xs:
    curve.append([y2,x])

  #4. left edge
  ys = np.linspace(y2,y1,100)
  for y in ys:
    curve.append([y,x1])
  ### COMPLETE CODE HERE ###
  # row = y col = x


  return np.array(curve)


# Reference source code: https://scikit-image.org/docs/stable/auto_examples/edges/plot_active_contours.html

# 1. Load the frame and annotations
frame = "Actor031_a10_f0001" 
img_color = mpimg.imread(f"{frame}.jpg")
annotation = np.loadtxt(f"{frame}.txt")[1:].tolist()

# 1.5 Adapt format of image and annotations
img_gray = rgb2gray(img_color)
xyxy = yolo2xyxy(*annotation, img_gray.shape)

# 2. Create your initial curve
init = get_curve_from_bbox(*xyxy)

# 3. Run snake function
### NOTE: Feel free to play with parameters here ###
snake = active_contour(
    gaussian(img_gray, sigma=3, preserve_range=False),
    init,
    alpha=0.015,
    beta=10,
    gamma=0.001,
)

# 4. Create segmentation mask from snake boundaries
mask = np.zeros(img_gray.shape, dtype=np.uint8)
fill_row_coords, fill_col_coords = draw.polygon(snake[:, 0], snake[:, 1], img_gray.shape)
mask[fill_row_coords, fill_col_coords] = 1

plt.imshow(mask, cmap='gray')
plt.title("Segmentation Mask")
plt.show()



# 5. Display snake, bbox, and overlayed segmentation mask on color image
color = True # Change this to switch between color and grayscale display
if color:
  img = img_color
  img_h, img_w, _ = img.shape
else:
  img = img_gray
  img_h, img_w = img.shape

dpi=600
fig, ax = plt.subplots(figsize=( img_w/dpi, img_h/dpi), dpi=dpi)
ax = fig.add_axes([0, 0, 1, 1])
ax.imshow(img, cmap=plt.cm.gray)
masked_data = np.ma.masked_where(mask == 0, mask)
ax.imshow(masked_data, cmap='jet', alpha=0.5)
ax.plot(init[:, 1], init[:, 0], '--r', lw=1)
ax.plot(snake[:, 1], snake[:, 0], '-b', lw=1)
ax.set_xlim(0, img_w)
ax.set_ylim(img_h, 0)
ax.axis('off')

plt.savefig('img_results.png', dpi=dpi, pad_inches=0)

plt.show()
