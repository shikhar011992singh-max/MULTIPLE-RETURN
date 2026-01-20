def make_chai():
      return "here is masala chai"

return_value = make_chai()
print(return_value)

def sp_chaiwala():
      pass
print(sp_chaiwala())

def sold_cups():
      return 12

total = sold_cups()
print(total)

def chai_status(cups_left):
      if cups_left == 0:
            return "sorry"
      return "chai ready"


print(chai_status(0))
print(chai_status(2))

def chai_report():
      return 10,20 #sold,remaining

sold, remaining, = chai_report()
print("Sold:",sold)
print("Remaining:",remaining)
