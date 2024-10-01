# user_name 에 함수가 실행될 때마다의 parameter / argument 를 저장한다. 
def say_hello(user_name):
  print("hellow ~",user_name," haw ar you?")

# 스코프 내에서만 유용하다. 
say_hello("user_name_test")
say_hello("lynn")
say_hello("lewis")

def say_bye():
  print("bye bye")


say_bye()


