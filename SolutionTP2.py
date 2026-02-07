import numpy as np

def see_lines(width, height, lines):
    res = np.zeros((height, width), dtype=int)
    for (i_start, j_start, i_end, j_end) in lines:
        x1, y1 = i_start, j_start
        x2, y2 = i_end, j_end
        
        dx = x2 - x1
        dy = y2 - y1
        e = 2 * dy - dx
        
        while x1 <= x2:
            res[x1, y1] = 1
            if e >= 0:
                y1 = y1 + 1
                e = e - 2 * dx
            x1 = x1 + 1
            e = e + 2 * dy
    return res