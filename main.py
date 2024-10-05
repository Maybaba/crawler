# param이 없을 경우 기본값 설정하기
def say_hello(user_name="anonymous"):
  print ("hello", user_name)

say_hello("nico")

say_hello()

# 계산기 만들기 
def plus(a, b):
  print(a+b)
def minus(a, b):
  print(a-b)
def mul(a, b):
  print(a*b)
def div(a,b):
  print(a/b)

plus(3,2)
minus(3,2)
mul(3,2)
div(5,3)