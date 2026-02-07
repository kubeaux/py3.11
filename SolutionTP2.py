import numpy as np

def see_lines(height, width, lines):
    res = np.zeros((height, width), dtype=int)
    
    for (i_start, j_start, i_end, j_end) in lines:
        x1, y1 = j_start, i_start
        x2, y2 = j_end, i_end
        
        is_steep = abs(y2 - y1) > abs(x2 - x1)
        if is_steep:
            x1, y1 = y1, x1
            x2, y2 = y2, x2
            
        if x1 > x2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1
            
        ystep = 1 if y1 < y2 else -1
        
        e = x2 - x1
        
        dx = e * 2  
        
        dy = abs(y2 - y1) * 2 
        
        x_curr = x1
        y_curr = y1
        
        while x_curr <= x2:
            if is_steep:
                if 0 <= x_curr < height and 0 <= y_curr < width:
                    res[x_curr, y_curr] = 1
            else:
                if 0 <= y_curr < height and 0 <= x_curr < width:
                    res[y_curr, x_curr] = 1
            
            x_curr = x_curr + 1
            
            e = e - dy
            if e <= 0:
                y_curr = y_curr + ystep
                e = e + dx
        
    return res