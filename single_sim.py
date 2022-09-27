import random
import numpy as np
import pandas as pd


def arrival():
    num = random.randint(1, 1000)
    
    if num <= 125:
        return 1
    elif 126 <= num <= 250:
        return 2
    elif 251 <= num <= 375:
        return 3
    elif 376 <= num <= 500:
        return 4
    elif 501 <= num <= 625:
        return 5
    elif 626 <= num <= 750:
        return 6
    elif 751 <= num <= 875:
        return 7
    elif 876 <= num <= 1000:
        return 8


def service():
    num = random.randint(1, 100)
    
    if num <= 10:
        return 1
    elif 11 <= num <= 30:
        return 2
    elif 31 <= num <= 60:
        return 3
    elif 61 <= num <= 85:
        return 4
    elif 86 <= num <= 95:
        return 5
    elif 96 <= num <= 100:
        return 6


def simulate():
    # simulation parameters
    total_customers = 20

    # simulation data
    arrival_times = [0]
    service_start_times = [0]
    service_duration_times = [0]
    service_end_times = [0]
    
    # simulation starts
    for i in range(1, total_customers + 1):
        arrival_times.append(arrival_times[i-1] + arrival())
        service_start_times.append(max(arrival_times[i], service_end_times[i-1]))
        service_duration_times.append(service())
        service_end_times.append(service_start_times[i] + service_duration_times[i])
    
    # simulation results table
    simulation_data = {
        "Customer Number" : np.arange(total_customers + 1),
        "Arrival Time" : arrival_times,
        "Time Service Begins" : service_start_times,
        "Service Time" : service_duration_times,
        "Time Service Ends" : service_end_times,
    }

    simulation_dataframe = pd.DataFrame(simulation_data)
    return simulation_dataframe


def main():
    print(simulate())


if __name__ == '__main__':
    main()
