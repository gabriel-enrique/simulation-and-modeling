import numpy as np
import pandas as pd

from random import choices, randint


def choose(pertamina_price, shell_price):
    delta = pertamina_price - shell_price
    delta /= 100 # scale down (normalize)
    middle = int(50 - delta) # round to int

    num = randint(1, 100) 

    if 1 <= num <= middle:
        return "Pertamina"
    elif (middle + 1) <= num <= 100:
        return "Shell"


def vehicle():
    '''
    Motorcycle  : 50%
    Cars        : 40%
    Trucks      : 10%
    '''
    vehicle_type = ["Motorcycle", "Cars", "Trucks"]
    prob = [0.5, 0.4, 0.1]

    return choices(vehicle_type, prob)[0]


def fuel_rating(vehicle):
    if vehicle == "Motorcycle":
        ratings = ["RON 90"]
        prob = [1]
    elif vehicle == "Cars":
        ratings = ["RON 90", "RON 92", "RON 98", "CN 51", "CN 53"]
        prob = [0.4, 0.3, 0.1, 0.05, 0.15]
    elif vehicle == "Trucks":
        ratings = ["CN 48", "CN 51", "CN 53"]
        prob = [0.2, 0.7, 0.1]
    
    return choices(ratings, prob)[0]


def liters(vehicle):
    if vehicle == "Motorcycle":
        num = randint(1, 4)
    elif vehicle == "Cars":
        num = randint(1, 45)
    elif vehicle == "Trucks":
        num = randint(1, 100)

    return num


def buy(liters, price):
    return liters * price


def simulate():
    # simulation parameters
    total_customers = 10000
    pertamina_prices = {
        "RON 90" : 10000,
        "RON 92" : 14500,
        "RON 98" : 15900,
        "CN 48" : 6800,
        "CN 51" : 17100,
        "CN 53" : 17400,
    }
    shell_prices = {
        "RON 90" : 11000, # data n/a (approx. used)
        "RON 92" : 15420,
        "RON 98" : 16510,
        "CN 48" : 7200, # data n/a (approx. used)
        "CN 51" : 18000, # data n/a (approx. used)
        "CN 53" : 18310,
    }

    # simulation data
    choices = []
    vehicle_types = []
    fuel_ratings = []
    liters_filled = []
    pertamina_sales = []
    shell_sales = []

    for i in range(total_customers):
        vehicle_types.append(vehicle())
        fuel_ratings.append(fuel_rating(vehicle_types[i]))
        liters_filled.append(liters(vehicle_types[i]))
        choices.append(choose(pertamina_prices[fuel_ratings[i]], shell_prices[fuel_ratings[i]]))

        if choices[i] == "Pertamina":
            pertamina_sales.append(buy(liters_filled[i], pertamina_prices[fuel_ratings[i]]))
            shell_sales.append(0)

        elif choices[i] == "Shell":
            shell_sales.append(buy(liters_filled[i], shell_prices[fuel_ratings[i]]))
            pertamina_sales.append(0)

    # simulation results table
    simulation_data = {
        "Customer" : np.arange(1, total_customers + 1),
        "Gas Station" : choices,
        "Vehicle" : vehicle_types,
        "Fuel Rating" : fuel_ratings,
        "Liters" : liters_filled,
        "Pertamina Sales" : pertamina_sales,
        "Shell Sales" : shell_sales,
    }
    
    simulation_dataframe = pd.DataFrame(simulation_data)
    print(simulation_dataframe)
    print()

    print("=== Total Sales ===")
    print("{:<25}: {:>20,}".format("Total Pertamina Sales", sum(pertamina_sales)))
    print("{:<25}: {:>20,}".format("Total Shell Sales", sum(shell_sales)))
    print()

    print("=== Vehicle Distribution ===")
    print(simulation_dataframe["Vehicle"].value_counts(normalize=True))
    print()


def main():
    simulate()


if __name__ == "__main__":
    main()
