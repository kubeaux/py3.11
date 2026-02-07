def see_lines(width, height, lines):
    res = np.zeros((height, width), dtype=int)

    for (i_start, j_start, i_end, j_end) in lines:
        x1 = j_start
        y1 = i_start
        x2 = j_end
        y2 = i_end

        e = x2 - x1
        dx = e * 2
        dy = (y2 - y1) * 2

        while x1 <= x2:
            res[y1, x1] = 1
            x1 = x1 + 1
            e = e - dy
            if e <= 0:
                y1 = y1 + 1
                e = e + dx

    return res