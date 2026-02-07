import numpy as np

def see_lines(width, height, lines):
    res = np.zeros((height, width), dtype=int)
    
    for (i_start, j_start, i_end, j_end) in lines:
        x1 = i_start
        y1 = j_start
        x2 = i_end
        y2 = j_end

        e = x2 - x1
        dx = e * 2
        dy = (y2 - y1) * 2
        
        while x1 <= x2:
            if 0 <= x1 < width and 0 <= y1 < height:
                res[x1, y1] = 1
            
            x1 = x1 + 1

            e = e - dy
            if e <= 0:
                y1 = y1 + 1 
                e = e + dx 
                
    return res