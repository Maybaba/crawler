# user_name 에 함수가 실행될 때마다의 parameter / argument 를 저장한다. 
def say_hello(user_name, user_age):
  print("hellow ~",user_name," haw ar you?")
  print("your age is" , user_age)

#calling function by using function name and argument
say_hello("user_name_test", 12)
say_hello("lynn", 23)
say_hello("lewis", 6)

print(1, 2, 3,4 ,5 ,6, 7,8 ,8, 9)

def say_bye():
  print("bye bye")


say_bye()

def tax_calculator(money):
  print("your october tax is", money * 0.353)

tax_calculator(300)