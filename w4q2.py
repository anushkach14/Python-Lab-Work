def sphere_volume(r):
    return (4/3) * 3.1415 * r**3


radius = float(input("Enter radius of sphere: "))
vol = sphere_volume(radius)
print(f"Volume of the sphere with radius {radius} is: {vol:.3f}")
