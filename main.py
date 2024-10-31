# function : unbounded with data (modifiable)

# method : bounded with data (unmodifiable)

print("May".encode("utf-8"))

numbers = [5, 4, 3, 2, 1, "True", True, 12, ["☕️", "🎃", "🎃", "🎃", "🎃", "🎃"]]

numbers.append("🪼")

print(numbers)
print(numbers[3])

# tuple () dict {} list []

player = {
  "name":"May",
  "age" : 25,
  "alive" : True,
  "fav_food" : ["🥦", "🍓"],
  "friend" : {
    "name" : "Jay",
    "fav_food" : ["🍕", "🍔"]
  }
}

print(player)

player['fav_food'] = "☕️"
player.pop("alive")

print(player['friend']['fav_food'].append("🧃"))

print(player)

def calculator():
  print("Happy halloween 🎃")

  while True:
      first_number = input("Choose a number :")
      second_number = input("Choose another one :")

      print("Enter the operation +, -, * and / if you want to exit enter 'exit'")
      operation = input()
      if operation == "exit":
        break

        # transform the string to int
        try:
            first_number = int(first_number)
            second_number = int(second_number)
        except ValueError:
          print("Invalid number")
          continue

      if operation == "+":
        print(int(first_number) + int(second_number))
      elif operation == "-":
        print(int(first_number) - int(second_number))
      elif operation == "*":
        print(int(first_number) * int(second_number))
      elif operation == "/":
        print(int(first_number) / int(second_number))
      else:
        print("Invalid operation")

calculator()


