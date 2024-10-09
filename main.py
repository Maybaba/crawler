# Dicts data structure

# key value pair

player = {
  'name': 'May',
  'age': 25,
  'alive': True,
  'fav_food': ["🎃", "☕️"]
}

print(player.get('age'))
print(player.get('fav_food'))
print(player['fav_food'])
print(player['fav_food'][0])

player.pop('name')
print(player)
player['xp'] = 1500
print(player)
player['fav_food'].append("❤︎")
print(player.get('fav_food'))
print(player['fav_food'])
