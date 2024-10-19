# Program #3: US_Population
def main():
    # Have the user input (using a loop) various information that contains three pieces of data: 
    # year, name of state, and population.  
    # Store all of this information in a list of lists.  For ,example it might be stored like this:
    
    # [[2010, "Maine", 1987435], [2010,"Minnesota",6873202], [2011, "Iowa", 3421988]]
    all_entered_values = []
    question = "y"
    mainloop = "true"
    while mainloop == "true":


        if question == 'y':
            value = [input("Please enter the year, the state and the total population: ")]
            all_entered_values = all_entered_values + value
            question = input("Would you add to add another value y or n?: ")
        else:
            mainloop = "false"


    # Now have the user enter a year.
    print(all_entered_values)
    year = int(input("please enter the year that you would like to add of the populations together: "))
    # The program will add the populations from all states in the list of list for that year only.
    # Pass the list and year to the sum_population_for_year
    sum_population_for_year(all_entered_values, year)

def sum_population_for_year(all_entered_values, year_to_sum):
    # Loop through and sum the populations for the appropriate year. 
    # e.g. for the list on line 7 the total would be 8,860,637 if the user entered 2010 for the year to sum,
    # or 3,421,988 if they entered 2011 for the year to sum.

    list2 = []

    for all_entered_values in all_entered_values:
        if all_entered_values[0] == year_to_sum:
            list2.append(all_entered_values[2])



    # print the totalled population
    answer = sum(list2)
    print(answer)
# Call the main function.
if __name__ == '__main__':
    main()