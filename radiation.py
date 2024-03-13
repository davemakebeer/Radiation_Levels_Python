import statistics

# FUNCTIONS
# Retrieve user-input integer
def get_int(display_string) -> int:
    """
    Continues to ask the user for an int until a valid int is entered.
    """
    while True:
        user_input = input(display_string)
        try:
            user_input = int(user_input)
        except ValueError:
            print("Invalid input. Please enter a whole number.")
        return user_input

# Retrieve user-input string
def get_str(display_string) -> str:
    """
    Continues to ask the user for an str until a valid str is entered.
    """
    while True:
        user_input = input(display_string)
        try:
            user_input = str(user_input)
        except ValueError:
            print("Invalid input.")
        return user_input

# Calculate average figure from a list
def return_average(user_list: list[int]) -> float:
    """
    Calculates and returns the average from a list of numbers
    """
    if not user_list:
        return 0
    return sum(user_list) / len(user_list)

# Calculate standard deviation from a dictionary
def return_stddev(user_dict):
    """
    Calculates and returns the standard deviation of the float values from a
    dictionary
    """
    temp_list = []
    for value in user_dict.values():
        temp_list.append(value)
    result = statistics.pstdev(temp_list)
    return result

# Update averages
def update_average():
    """Updates location_average_dict each time it's called"""
    location_average_dict.update(
        {location: return_average(values)
        for location, values
        in location_levels_dict.items()}
    )

# Print options screen
def options_screen() -> print:
    """
    Displays options screen, calls get_int() to return a viable selection
    """
    print()
    print("1. View Data Printout")
    print("2. View Measurements by Location")
    print("3. Add Data")
    print("4. Exit Program (save function upcoming)")

# Output all data
def data_printout() -> print:
    """
    Calculates and prints averages for each location.
    Prints standard deviation.
    """
    print("Average Radiation Levels:")
    for loc, average in location_average_dict.items():
        print(f"  {average:.1f} in {loc}.")
    standard_deviation = return_stddev(location_average_dict)
    print(f"\nStandard Deviation:\n  {standard_deviation:.1f}")

# Output data points by location
def location_data_printout() -> print:
    """Outputs data points for each location in a clear manner."""
    for loc, levels in location_levels_dict.items():
        print(f"{loc}:\n  {levels}")

# Add measurements by location
def add_data() -> int:
    """
    Loops through location names until user breaks.
    Data points are appended to displayed location name in
    location_levels_dict.
    """
    for loc in location_levels_dict:
        print(f"<<< Gathering data for {loc} >>>")
        print("Type 'next' to proceed or 'exit' to finish.")
        user_input = ""
        while True:
            user_input = input("Enter measurement: ")
            if user_input.lower() == 'exit':
                return
            elif user_input.lower() == 'next':
                break
            try:
                (location_levels_dict[loc]
                .append(int(user_input)))
            except ValueError:
                print("Invalid input. Please enter a whole number.")


# CONSTANTS
# Backend input - list of locations
location_list = [
    'City Centre',
    'Industrial Zone',
    'Residential District',
    'Rural Outskirts',
    'Downtown'
]
# Backend input - list of historical radiation data
radiation_levels = [
    [22, 19, 20, 31, 28],
    [35, 32, 30, 37, 40],
    [15, 12, 18, 20, 14],
    [9, 13, 16, 14, 7],
    [25, 18, 22, 21, 26]
]
# Dictionary of locations and their corresponding historical measurements
location_levels_dict = dict(zip(location_list, radiation_levels))
# Dictionary of locations and their corresponding historical averages
location_average_dict = {
    location: return_average(values)
    for location, values
    in location_levels_dict.items()
}


# MAIN PROGRAM
option_choice = 0

while option_choice != 4:
    options_screen()
    option_choice = get_int('\nChoose option 1-4: ')
    print()
    if option_choice == 1: # View data printout
        data_printout()
    elif option_choice == 2: # View measurements by location
        location_data_printout()
    elif option_choice == 3: # Add Data
        add_data()
        update_average()
    elif option_choice == 4: # Exit
        print("Goodbye for now.")
    else:
        print("Option not available.")
