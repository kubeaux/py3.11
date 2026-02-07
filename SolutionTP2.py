import numpy as np

def see_lines(width, height, lines):
    """
    Adaptation du see_lines du TP1 avec l'algorithme de Bresenham du TP2.
    Signature conservée : (width, height, lines).
    """
    # 1. Structure issue du TP1 (Validée)
    res = np.zeros((height, width), dtype=int)
    
    for (i_start, j_start, i_end, j_end) in lines:
        # 2. Mapping des coordonnées
        # TP1 utilise (i, j) -> (ligne, colonne)
        # Bresenham (1er octant) utilise x principal -> x correspond aux colonnes (j)
        x1 = int(j_start)
        y1 = int(i_start)
        x2 = int(j_end)
        y2 = int(i_end)
        
        # 3. Normalisation "Arbitrairement orientées"
        # L'algorithme 'tant que x1 <= x2' impose que x1 soit le point de gauche.
        # Si la ligne est définie de droite à gauche, on inverse les points.
        if x1 > x2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1
            
        # 4. Algorithme de Bresenham (Consigne TP2 / Wikipedia)
        e = x2 - x1          # Erreur initiale
        dx = e * 2           # Constante dx
        dy = (y2 - y1) * 2   # Constante dy
        
        while x1 <= x2:
            # Tracé du pixel : res[ligne, colonne] => res[y, x]
            if 0 <= y1 < height and 0 <= x1 < width:
                res[y1, x1] = 1
            
            # Avance sur l'axe colonne (x)
            x1 = x1 + 1
            
            # Mise à jour de l'erreur
            # "si (e <- e - dy) <= 0"
            e = e - dy
            if e <= 0:
                y1 = y1 + 1  # Montée sur l'axe ligne (y)
                e = e + dx   # Ajustement erreur
                
    return res