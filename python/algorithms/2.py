def compute_area(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2):
    area_of_a = (ax2 - ax1) * (ay2 - ay1)
    area_of_b = (bx2 - bx1) * (by2 - by1)

    # take leftmost of right corners and subtract by rightmost of left corners
    x_overlap = min(ax2, bx2) - max(ax1, bx1)
    y_overlap = min(ay2, by2) - max(ay1, by1)

    return (area_of_a + area_of_b) - (x_overlap * y_overlap)

print(compute_area(-2, -2, 2, 2, -2, -2, 2, 2))
    