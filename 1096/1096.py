i = 1
j = 7

while i < 10:
    for c in range(0,3):
        print(f"I={i}", end=" ")
        print(f"J={j-c}")
    i += 2