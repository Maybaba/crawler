# tax calculator
# return statement can use return value anywhere
def tax_calc(money):
  return money * 0.35

def pay_tax(tax):
  print("thx for paying", tax)

pay_tax(tax_calc(120))