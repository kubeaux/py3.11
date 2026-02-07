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

def see_lines_complete(height, width, lines):
    res = np.zeros((height, width), dtype=int)
    
    for (i_start, j_start, i_end, j_end) in lines:
        x0 = int(j_start)
        y0 = int(i_start)
        x1 = int(j_end)
        y1 = int(i_end)
        
        dx = abs(x1 - x0)
        dy = -abs(y1 - y0)
        sx = 1 if x0 < x1 else -1
        sy = 1 if y0 < y1 else -1
        err = dx + dy
        
        while True:
            if 0 <= y0 < height and 0 <= x0 < width:
                res[y0, x0] = 1
            
            if x0 == x1 and y0 == y1:
                break
            
            e2 = 2 * err
            if e2 >= dy:
                err += dy
                x0 += sx
            if e2 <= dx:
                err += dx
                y0 += sy
                
    return res