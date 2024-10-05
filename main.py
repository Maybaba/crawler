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

True and True == True
False and True == False
True and False == False
False and False == False

True or True == True
True or False == True
False or True == True
False or False == False