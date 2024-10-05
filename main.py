# machine that making juice
def make_juice(fruit):
  return f"{fruit} + 🥤"

def add_ice(juice):
  return f"{juice} + 🥶"

def add_sugar(iced_juice):
  return f"{iced_juice} + ✰"

juice = make_juice("🍓")
cold_juice = add_ice(juice)
perfecto_juice = add_sugar(cold_juice)

print(perfecto_juice)

# keword return kills the code after it