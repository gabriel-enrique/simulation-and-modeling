import random
import numpy as np
import pandas as pd


def choose(pertamina_price, shell_price):
    delta = pertamina_price - shell_price
    delta /= 100 # scale down (normalize)

    num = random.randint(1, 100)
    middle = int(50 - delta) # round to int

    if 1 <= num <= middle:
        return "Pertamina"
    elif (middle + 1) <= num <= 100:
        return "Shell"


def vehicle():
    num = random.randint(1, 138550)

    if 1 <= num <= 113030:
        return "Motorcycle"
    elif 113031 <= num <= 120550:
        return "Trucks"
    elif 120551 <= num <= 123060:
        return "Bus"
    elif 123061 <= num <= 138550:
        return "Car"


def liters(vehicle):
    if vehicle == "Motorcycle":
        num = random.randint(1, 4)
    elif vehicle == "Trucks":
        num = random.randint(1, 100)
    elif vehicle == "Bus":
        num = random.randint(1, 350)
    elif vehicle == "Car":
        num = random.randint(1, 45)

    return num


def buy(liters, price):
    return liters * price


def simulate():
    # simulation parameters
    total_customers = 10
    pertamina_price = 12500
    shell_price = 15000

    # simulation data
    choices = []
    vehicle_types = []
    liters_filled = []
    pertamina_sales = []
    shell_sales = []

    for i in range(total_customers):
        choices.append(choose(pertamina_price, shell_price))
        vehicle_types.append(vehicle())
        liters_filled.append(liters(vehicle_types[i]))

        if choices[i] == "Pertamina":
            pertamina_sales.append(buy(liters_filled[i], pertamina_price))
            shell_sales.append(0)

        elif choices[i] == "Shell":
            shell_sales.append(buy(liters_filled[i], shell_price))
            pertamina_sales.append(0)

    # simulation results table
    simulation_data = {
        "Customer" : np.arange(1, total_customers + 1),
        "Gas Station" : choices,
        "Vehicle" : vehicle_types,
        "Liters" : liters_filled,
        "Pertamina Sales" : pertamina_sales,
        "Shell Sales" : shell_sales,
    }
    
    simulation_dataframe = pd.DataFrame(simulation_data)
    print(simulation_dataframe)
    print(f"Total Pertamina Sales: {sum(pertamina_sales):,}")
    print(f"Total Shell Sales: {sum(shell_sales):,}")


def main():
    simulate()


if __name__ == "__main__":
    main()
