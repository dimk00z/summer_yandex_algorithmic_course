
def is_triangle(points) -> str:
    a, b, c = points
    if a + b <= c or b + c <= a or a + c <= b:
        return 'NO'
    return 'YES'


points = []
for _ in range(3):
    points.append(float(input()))
print(is_triangle(points))
