# Radiation Measurement Data Collector

## Overview
This Python program serves as a tool for collecting and managing radiation level measurements at various locations. It allows users to input new measurements, view data printouts, and access location-specific information.

## Features
1. **View Data Printout:** Display the average radiation levels for each predefined location and the overall standard deviation.

2. **View Measurements by Location:** Output historical data points for each location.

3. **Add Data:** Append new measurements to the existing historical data for each location.

4. **Exit Program:** Safely exit the program.

## How to Use
1. Run the program and choose an option from the main menu (1-4).
2. Follow the prompts to perform the selected action.

### Option 1: View Data Printout
This option displays the average radiation levels for each location and the overall standard deviation.

### Option 2: View Measurements by Location
Provides a detailed view of historical data points for each location.

### Option 3: Add Data
Allows users to input new measurements for each location. Enter measurements until satisfied, and type 'exit' to finish.

### Option 4: Exit Program
Exits the program with a farewell message.

## Constants
The program includes predefined location names (`location_list`), historical radiation data (`radiation_levels`), a dictionary of locations and historical measurements (`location_levels_dict`), and a dictionary of locations and their corresponding historical averages (`location_average_dict`).

## Functions
- `get_int(display_string)`: Retrieve a valid integer input from the user.
- `get_str(display_string)`: Retrieve a valid string input from the user.
- `return_average(user_list)`: Calculate and return the average from a list of numbers.
- `return_stddev(user_dict)`: Calculate and return the standard deviation from a dictionary.
- `update_average()`: Update the dictionary of location averages.
- `options_screen()`: Display the main menu with available options.
- `data_printout()`: Calculate and print the average radiation levels and standard deviation.
- `location_data_printout()`: Output historical data points for each location.
- `add_data()`: Loop through locations, allowing users to input new measurements.

## Main Program
The main program consists of a loop that continues until the user chooses to exit (Option 4). It dynamically responds to user input, executing the corresponding functions based on the selected option.

**Note:** The program lacks a save function, as indicated in the comments, and it's recommended to implement one for data persistence.
