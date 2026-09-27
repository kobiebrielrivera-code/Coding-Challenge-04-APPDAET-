import math

# A tiny number used to compare floats safely.
# We can't just check "if x == 0" with decimals, because of rounding errors,
# so instead we check "if x is really really close to 0".
TOLERANCE = 1e-6


# FUNCTION 1: distance
# Finds the distance between two points using the distance formula.
def distance(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    return math.sqrt(dx ** 2 + dy ** 2)


# FUNCTION 2: triangle_area
# Finds the area of a triangle using the coordinate (shoelace) formula.
def triangle_area(ax, ay, bx, by, cx, cy):
    area = 0.5 * abs(ax * (by - cy) + bx * (cy - ay) + cx * (ay - by))
    return area


# FUNCTION 3: classify_by_sides
# Looks at the 3 side lengths and decides the triangle type.
def classify_by_sides(ab, bc, ca):
    # We compare using a small tolerance instead of "==" because of
    # decimal rounding.
    ab_bc_equal = abs(ab - bc) < TOLERANCE
    bc_ca_equal = abs(bc - ca) < TOLERANCE
    ca_ab_equal = abs(ca - ab) < TOLERANCE

    if ab_bc_equal and bc_ca_equal:
        return "equilateral"
    elif ab_bc_equal or bc_ca_equal or ca_ab_equal:
        return "isosceles"
    else:
        return "scalene"

# FUNCTION 4: classify_by_angles
# Uses the squared side lengths (like the Pythagorean theorem) to
# decide if the triangle is acute, right, or obtuse.
# The rule: compare the square of the longest side to the sum of the
# squares of the other two sides.
def classify_by_angles(ab, bc, ca):
    sides_squared = sorted([ab ** 2, bc ** 2, ca ** 2])
    smallest_two_sum = sides_squared[0] + sides_squared[1]
    longest = sides_squared[2]

    if abs(longest - smallest_two_sum) < TOLERANCE:
        return "right"
    elif longest > smallest_two_sum:
        return "obtuse"
    else:
        return "acute"

# FUNCTION 5: locate_point
# Decides if point P is INSIDE, ON THE BOUNDARY, or OUTSIDE
# triangle ABC, using the area-decomposition method described above.
def locate_point(ax, ay, bx, by, cx, cy, px, py):
    area_abc = triangle_area(ax, ay, bx, by, cx, cy)

    area_pab = triangle_area(px, py, ax, ay, bx, by)
    area_pbc = triangle_area(px, py, bx, by, cx, cy)
    area_pca = triangle_area(px, py, cx, cy, ax, ay)

    total_small_areas = area_pab + area_pbc + area_pca

    # If the 3 small areas do NOT add up to the big area, P is outside.
    if abs(total_small_areas - area_abc) > TOLERANCE:
        return "OUTSIDE"

    # If they DO add up, P is inside or exactly on an edge.
    # If P sits exactly on an edge, one of the 3 small triangles has
    # zero area (because P, and the two vertices of that edge, are
    # all on the same line).
    if area_pab < TOLERANCE or area_pbc < TOLERANCE or area_pca < TOLERANCE:
        return "ON THE BOUNDARY"

    return "INSIDE"


# FUNCTION 6: nearest_vertex
# Finds which vertex (A, B, or C) is closest to point P.
# Returns the vertex name and the distance to it.
def nearest_vertex(ax, ay, bx, by, cx, cy, px, py):
    dist_a = distance(px, py, ax, ay)
    dist_b = distance(px, py, bx, by)
    dist_c = distance(px, py, cx, cy)

    smallest_distance = min(dist_a, dist_b, dist_c)

    if smallest_distance == dist_a:
        return "A", dist_a
    elif smallest_distance == dist_b:
        return "B", dist_b
    else:
        return "C", dist_c


# FUNCTION 7: analyze_landing_zone
# This is the "main" function that uses all the other functions
# together and prints a full, readable report.
def analyze_landing_zone(ax, ay, bx, by, cx, cy, px, py):
    print("-" * 55)
    print(f"A = ({ax}, {ay})   B = ({bx}, {by})   C = ({cx}, {cy})")
    print(f"P (proposed drone landing point) = ({px}, {py})")
    print("-" * 55)

    # STEP 1: Check if A, B, C form a real triangle.
    area = triangle_area(ax, ay, bx, by, cx, cy)

    if area < TOLERANCE:
        print("Result: INVALID landing zone.")
        print("Reason: Points A, B, and C are collinear (they form a")
        print("straight line, not a triangle), so the area is 0.")
        print("-" * 55)
        return  # Stop here, there is nothing else to calculate.

    # STEP 2: Calculate the side lengths.
    ab = distance(ax, ay, bx, by)
    bc = distance(bx, by, cx, cy)
    ca = distance(cx, cy, ax, ay)
    perimeter = ab + bc + ca

    # STEP 3: Classify the triangle.
    side_type = classify_by_sides(ab, bc, ca)
    angle_type = classify_by_angles(ab, bc, ca)

    # STEP 4: Locate point P relative to the triangle.
    location = locate_point(ax, ay, bx, by, cx, cy, px, py)

    # STEP 5: Find the nearest vertex to P.
    vertex_name, vertex_distance = nearest_vertex(ax, ay, bx, by, cx, cy, px, py)

    # STEP 6: Print the final, readable summary.
    print("Result: VALID triangular landing zone.")
    print(f"Side AB = {ab:.4f}")
    print(f"Side BC = {bc:.4f}")
    print(f"Side CA = {ca:.4f}")
    print(f"Perimeter = {perimeter:.4f}")
    print(f"Area = {area:.4f}")
    print(f"Classification by sides: {side_type}")
    print(f"Classification by angles: {angle_type}")
    print(f"Drone landing point P is: {location}")
    print(f"Nearest vertex to P is {vertex_name}, at distance {vertex_distance:.4f}")
    print("-" * 55)


# MAIN PROGRAM
# Here we run the 4 test cases given in the challenge sheet so we can
# check that our functions give the expected results.
if __name__ == "__main__":

    print("EMERGENCY DRONE LANDING GEOMETRY ANALYZER")
    print("=" * 55)

    # Test Case 1: expect area=40, isosceles, acute, INSIDE, nearest = C (dist 4)
    print("\nTEST CASE 1")
    analyze_landing_zone(0, 0, 10, 0, 4, 8, 4, 4)

    # Test Case 2: expect P = ON THE BOUNDARY
    print("\nTEST CASE 2")
    analyze_landing_zone(0, 0, 10, 0, 4, 8, 5, 0)

    # Test Case 3: expect P = OUTSIDE
    print("\nTEST CASE 3")
    analyze_landing_zone(0, 0, 10, 0, 4, 8, 12, 2)

    # Test Case 4: expect INVALID (collinear points)
    print("\nTEST CASE 4")
    analyze_landing_zone(0, 0, 5, 5, 10, 10, 3, 3)
