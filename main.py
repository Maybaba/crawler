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

