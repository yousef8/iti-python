def isPrime(num):
    if not isinstance(num, int):
        return "Not a Number"
    if num <= 1:
        return False
    if num <= 3:
        return True
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


print(f"11 isPrime => {isPrime(11)}")
print(f"ahmed isPrime => {isPrime('ahmed')}")
print(f"3.4 isPrime => {isPrime(3.4)}")
