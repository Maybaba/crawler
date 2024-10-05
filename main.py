# AND OR

age = int(input("How old are you?"))

print(type(age))

print("user answer : ", age)

if age < 18:
  print("You are not old enough to vote")
elif age > 17 and age < 21:
  print("You are in the prime of your life")
else:
  print("go vote")