i = 0
j = 1

while i <= 2:
    for c in range(0,3):
        if i % 1 == 0 or i > 1.9:
            print(f"I={i:.0f}", end=" ") 
            print(f"J={(j+c)+i:.0f}")
        else:
            print(f"I={i:.1f}", end=" ")
            print(f"J={(j+c)+i:.1f}")
    i += 0.2