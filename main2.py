# Import modules to use the functions & methods they contain
from Robot import Robot
from Robot import fetch
from Robot import sleep
from store_state import data

# Create Robot1 object with arguments
robot_1 = Robot.one_string('Altman-X27-Cobalt')

# Call the robotInfo function using the Robot1 object
robot_1.robot_info()

# Set variables equal to values from data dictionary
shelf = data["Shelf status"]
stock = data["Product stock"]
print("Power = On")
print("Altman activated and ready to work. Checking store for any \
      missing product.\n")

# Call functions depending on values of data dictionary
if shelf == 'Full':
    print("Shelf status: " + shelf)
    sleep()
elif shelf == 'Empty':
    print("Shelf status: " + shelf + "\nChecking stockroom for missing \
          product.\n")
    if stock == 'Full':
        print("Stock status: " + stock)
        fetch()
        shelf = "Full"
        print("\nShelf status: " + shelf)
        sleep()
    elif stock == 'Empty':
        print("Stock status: " + stock)
        sleep()
    else:
        print('Sensor reading corrupted. Check input file for errors.')
else:
    print('Sensor reading corrupted. Check input file for errors.')
