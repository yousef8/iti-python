def isEven(num):
    try:
        num = int(num)
        return num % 2 == 0
    except ValueError:
        return "Not a Number"


print(f"10 isEven => {isEven(10)}")
print(f"11 isEven => {isEven('11')}")
print(f"ahmed isEven => {isEven('ahmed')}")
