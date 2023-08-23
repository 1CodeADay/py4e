#Exercise 7: Rewrite the grade program from the previous chapter using a function called
# computegrade that takes a score as its parameter and returns a grade as a string.
#Run the program repeatedly to test the various different values for input.

def computepay(hours, rate) :
    #print("In computepay", hours, rate)
    if hours > 40:
        rpay = hours * rate
        otpay = (hours - 40) * (rate * 0.5)
        pay = rpay + otpay
    else:
        pay = hours * rate
    #print("Returning", pay)
    return pay

hours = float(input('Enter Hours: '))
rate = float(input('Enter Rate: '))

pay = computepay(hours, rate)
print("Pay", pay)

#Function call: type()
#Built-in functions
#math functions: module.function (dot notation)
#define a function
#parameters and arguments
#Fruitful functions and void functions




