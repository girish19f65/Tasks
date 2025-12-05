def calculate_distance(speed, time):
    return speed * time

speed = float(input("Enter speed: "))
time = float(input("Enter time: "))

distance = calculate_distance(speed, time)
print("Speed =", speed,"km/h")
print("Time =", time,"h")
print("Distance traveled =", distance,"km")
