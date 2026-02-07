import numpy as np

def see_lines(height, width, lines):
    # Création de l'image noire (matrice de 0)
    res = np.zeros((height, width), dtype=int)
    
    for (i_start, j_start, i_end, j_end) in lines:
        # Correspondance des coordonnées :
        # Dans l'algo Wikipedia : x est la colonne, y est la ligne (rangée)
        # Dans la matrice numpy : j est la colonne, i est la ligne
        
        x1, y1 = j_start, i_start
        x2, y2 = j_end, i_end
        
        # --- DÉBUT ALGORITHME BRESENHAM (Wikipedia) ---
        
        # e ← x2 - x1
        e = x2 - x1
        
        # dx ← e × 2
        dx = e * 2
        
        # dy ← (y2 - y1) × 2
        dy = (y2 - y1) * 2
        
        # tant que x1 ≤ x2 faire
        while x1 <= x2:
            # tracerPixel(x1, y1)
            # (On vérifie juste qu'on ne sort pas de l'image)
            if 0 <= x1 < width and 0 <= y1 < height:
                res[y1, x1] = 1
            
            # x1 ← x1 + 1  // colonne du pixel suivant
            x1 = x1 + 1
            
            # si (e ← e - dy) ≤ 0 alors
            e = e - dy
            if e <= 0:
                # y1 ← y1 + 1  // choisir plutôt le pixel suivant dans la rangée supérieure
                y1 = y1 + 1
                
                # e ← e + dx  // ajuste l’erreur
                e = e + dx
            # fin si
        # fin faire
        
        # --- FIN ALGORITHME ---
        
    return res