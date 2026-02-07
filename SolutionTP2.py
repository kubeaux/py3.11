import numpy as np

def see_lines(height, width, lines):
    image = np.zeros((height, width), dtype=int)

    for line in lines:
        i_start, j_start, i_end, j_end = line
        
        x1, y1 = j_start, i_start
        x2, y2 = j_end, i_end
    
        e = x2 - x1
        dx = e * 2
        dy = (y2 - y1) * 2
        while x1 <= x2:
            if 0 <= x1 < width and 0 <= y1 < height:
                image[y1, x1] = 1
            x1 = x1 + 1
            e = e - dy
            if e <= 0:
                y1 = y1 + 1
                e = e + dx

    return image