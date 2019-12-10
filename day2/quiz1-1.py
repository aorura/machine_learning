def getWageAndHours():
    hoursworked = eval(input("Enter hours worked: "))
    hourlyWage = eval(input("Enter hourly pay: "))
    return(hourlyWage, hoursworked)


def pay(wage, hours):
    if hours <= 40:
        amount = wage * hours
    else:
        amount = (wage * 40) + ((1.5) * wage * (hours - 40))
    return amount

def displayEarnings(payForWeek):
    print("Week’s pay: ${0:.2f}".format(payForWeek))
    
(wage, hours) = getWageAndHours()
payForWeek = pay(wage, hours)
displayEarnings(payForWeek)