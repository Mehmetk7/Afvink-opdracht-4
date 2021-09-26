# Bug collector
T = 0
Total = 0
for i in range(5):
    T = T + 1
    print("Day", T)
    Bugs = int(input("Give total number of bugs for the day \a"))
    Total = Total + Bugs
print("Total number of bugs for the week are: ", Total)


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
    print("lap", i, "time is: ", Lap_time)
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






































