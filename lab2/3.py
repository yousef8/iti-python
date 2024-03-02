import json

numbers = [3, 4, 9, 16, 25, 36]

print(f" {numbers} = Squared => {list(map(lambda i: i * i, numbers))}")

numbers_squares = {num: num * num for num in numbers}

with open("numbers_squares.json", "w") as file:
    json.dump(numbers_squares, file, indent=2)
    print("Wrote numbers and theirs squares to json file")
