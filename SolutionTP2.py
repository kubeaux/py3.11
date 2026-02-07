import numpy as np

def see_lines(width, height, lines):
    res = np.zeros((height, width), dtype=int)
    
    for (i_start, j_start, i_end, j_end) in lines:
        x1 = int(i_start)
        y1 = int(j_start)
        x2 = int(i_end)
        y2 = int(j_end)
        
        if x1 > x2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1
            
        e = x2 - x1          
        dx = e * 2           
        dy = (y2 - y1) * 2   
        
        while x1 <= x2:
            res[x1, y1] = 1
            
            x1 = x1 + 1
            
            e = e - dy
            if e <= 0:
                y1 = y1 + 1 
                e = e + dx  
                
    return res