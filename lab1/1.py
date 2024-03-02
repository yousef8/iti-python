def inRange(start, end, num):
    for i in range(start, end + 1):
        if i == num:
            print(f"In range [{start}-{end}]")
            return
    print(f"{num} not in range [{start}-{end}]")


try:
    num = int(input("Enter a number _> "))
    inRange(20, 50, num)
except ValueError:
    print("Only numbers allowed")
