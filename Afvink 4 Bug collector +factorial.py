'''Runners = int(input("Enter the amount of runners: "))
Lap_amount = int(input("Enter amount of laps: "))

for lap in range(Runners):
    total = 0.0
    print("Runner", lap + 1)
    print("------------------")
    for lap_time in range(Lap_amount):
        print("lap:", lap_time + 1)
        Lap_time = int(input("Enter Lap time in whole seconds: "))
        total = total + Lap_time

    average = total / Lap_amount
    print("Average lap speed for runner", lap + 1, "is", average)'''



# Opdracht 4.2 Lap Times

# Dit input vraagt de totale Laps
Lap_amount = int(input("Enter the total lap amount: "))
i = 0
total = 0.0
list = []

# while loop om de individuele tijden per Laps te vragen en opslaan
while i < Lap_amount:
    # Elke ronde komt 1 bij de i. Zolang i kleiner is dan totale Laps blijft de while loop door gaan
    i += 1
    # hier vragen we de tijd per lap
    Lap_time = int(input("Enter Lap time in seconds: "))
    print("Your", i,"lap time is: ", Lap_time)
    # hier word de totale tijd berekend, dus tijd van elke ronde word opgeteld en opgeslagen in total
    total = total + Lap_time
    # elke Lap tijd word opgeslagen in een list
    list.append(Lap_time)


print("----------------------------------------")
print("Average lap time: ", total / Lap_amount)
print("Your fastest time: ", min(list))
print("Your slowest time: ", max(list))



#Opdracht 4.3 Calculating the factorial of a number

Number = int(input("Enter a non negative integer: "))
factorial = 1

for fac in range(1, Number + 1):
    factorial = factorial*fac
    print(factorial)






































