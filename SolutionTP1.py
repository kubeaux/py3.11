import numpy as np;
import matplotlib.image as mpimg;
def blackout(width, height) : 
    res = np.zeros((height, width))
    return res 

def see_points(width, height, points) :
    res = np.zeros((height, width))
    for i,j in points:
        res[i,j] = 1
    return res

def see_quadrant(image_name, quadrant) :
    img = mpimg.imread(image_name)
    if img.max() <= 1.0 :
        img = img * 255
    img = img.astype(int)
    h,w = img.shape[:2]
    t_i = 0
    t_j = 0

    if quadrant == 'top_left':
        t_i = h // 4
        t_j = w // 4
    elif quadrant == 'top_right':
        t_i = h // 4
        t_j = (3 * w) // 4
    elif quadrant == 'bottom_left':
        t_i = (3 * h) // 4
        t_j = w // 4
    elif quadrant == 'bottom_right':
        t_i = (3 * h) // 4
        t_j = (3 * w) // 4
    
    pxl_val = img[t_i, t_j]
    return int(pxl_val)

def see_lines(width, height, lines):
    res = np.zeros((height, width), dtype=np.uint8)
    for i_start, j_start, i_end, j_end in lines:
        if i_start == i_end:
            res[i_start, j_start : j_end + 1] = 1
        else:
            res[i_start : i_end + 1, j_start] = 1
     
    return res