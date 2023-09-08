#Exercise 2: Rewrite your pay program using try and except so that your program handles non-numeric
# input gracefully by printing a message and exiting the program. The following shows two executions of the program:

try:
    hrs = float(input('Enter Hours: '))
    rate = float(input('Enter Rate: '))
except:
    print("Error, please enter numeric input")
rpay = hrs * rate
otpay = (hrs - 40) * (rate * 0.5)
pay = rpay + otpay
if hrs <= 40:
    print('Regular')
    print('Pay:',rpay)
else:
    print("Overtime")
    print('rpay:',rpay)
    print("otpay:",otpay)
    print("Pay:",pay)
