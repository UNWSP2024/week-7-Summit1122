# Program #1: Rainfall
# Design a program that lets the user enter the total rainfall for each of 12 months into a list.
# The program should calculate and display the total rainfall for the year, 
# the average monthly rainfall, # and the months with the highest and lowest amounts.


def rainfall_program():
    print("Welcome to the yearly Rainfall Analyzer")
    rain_list = []

    for rct in range(1,13):
        rainfall = float(input (f"In month {str(rct)} What was the amount of rain?: "))
        rain_list.append(rainfall)


    total = sum(rain_list)
    avg = total/rct

    print("The most rain within a month was", max(rain_list))
    print("The least amount of rain within a month was", min(rain_list))
    print(f"The total rainfall for this year was: {total} ")
    print(f"The average rainfall per month was: {format(avg, ".2f")}")

rainfall_program()