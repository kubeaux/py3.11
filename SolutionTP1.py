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

import numpy as np

def see_lines(width, height, lines):
    res = np.zeros((height, width), dtype=int)
    for (i_start, j_start, i_end, j_end) in lines:
        if i_start == i_end:
            for j in range(j_start, j_end):
                res[i_start, j] = 1
        elif j_start == j_end:
            for i in range(i_start, i_end):
                res[i, j_start] = 1
    return res
            
def see_quadrant_complete(image_name, quadrant):
    img = mpimg.imread(image_name)
    
    if img.dtype == np.uint8:
        img = img.astype(float) / 255.0
    else:
        img = img.copy()

    if len(img.shape) == 2:
        img = np.stack((img,)*3, axis=-1)
    
    if img.shape[2] > 3:
        img = img[:, :, :3]
        
    h, w = img.shape[:2]
    
    img[h // 2, :, :] = [1.0, 0.0, 0.0]
    
    img[:, w // 2, :] = [1.0, 0.0, 0.0]
    
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
        
    delta = 3
    
    r_start = max(0, t_i - delta)
    r_end = min(h, t_i + delta + 1)
    c_start = max(0, t_j - delta)
    c_end = min(w, t_j + delta + 1)
    
    img[r_start:r_end, c_start:c_end, :] = [0.0, 0.0, 1.0]
    
    return img