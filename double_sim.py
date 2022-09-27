import random
import numpy as np
import pandas as pd


def arrival():
    num = random.randint(1, 100)
    
    if 1 <= num <= 25:
        return 1
    elif 26 <= num <= 65:
        return 2
    elif 66 <= num <= 85:
        return 3
    elif 86 <= num <= 100:
        return 4


def service_ali():
    num = random.randint(1, 100)
    
    if 1 <= num <= 30:
        return 2
    elif 31 <= num <= 58:
        return 3
    elif 59 <= num <= 83:
        return 4
    elif 84 <= num <= 100:
        return 5


def service_badu():
    num = random.randint(1, 100)
    
    if 1 <= num <= 35:
        return 3
    elif 36 <= num <= 60:
        return 4
    elif 61 <= num <= 80:
        return 5
    elif 81 <= num <= 100:
        return 6


def get_max(end_times):
    curr_max = end_times[0]

    for i in range(len(end_times)):
        if type(end_times[i]) == str:
            continue

        if end_times[i] > curr_max:
            curr_max = end_times[i]

    return curr_max


def simulate():
    # simulation parameters
    total_customers = 20

    # simulation data
    arrival_times = [0]
    served_by = [""]

    service_ali_start_times = [0]
    service_ali_duration_times = [0]
    service_ali_end_times = [0]

    service_badu_start_times = [0]
    service_badu_duration_times = [0]
    service_badu_end_times = [0]

    # simulation starts
    for i in range(1, total_customers + 1):
        arrival_times.append(arrival_times[i-1] + arrival())

        ali_ends = get_max(service_ali_end_times)
        badu_ends = get_max(service_badu_end_times)

        if (arrival_times[i] >= ali_ends) or (ali_ends <= badu_ends):
            server = "Ali"
            service_ali_start_times.append(max(arrival_times[i], get_max(service_ali_end_times)))
            service_ali_duration_times.append(service_ali())
            service_ali_end_times.append(service_ali_start_times[i] + service_ali_duration_times[i])

            service_badu_start_times.append("")
            service_badu_duration_times.append("")
            service_badu_end_times.append("")

        else:
            server = "Badu"
            service_badu_start_times.append(max(arrival_times[i], get_max(service_badu_end_times)))
            service_badu_duration_times.append(service_badu())
            service_badu_end_times.append(service_badu_start_times[i] + service_badu_duration_times[i])
            
            service_ali_start_times.append("")
            service_ali_duration_times.append("")
            service_ali_end_times.append("")

        served_by.append(server)

    # simulation results table
    simulation_data = {
        "Customer Number" : np.arange(total_customers + 1),
        "Arrival Time" : arrival_times,
        "Served By" : served_by,
        "Time Service Begins (Ali)" : service_ali_start_times,
        "Service Time (Ali)" : service_ali_duration_times,
        "Time Service Ends (Ali)" : service_ali_end_times,
        "Time Service Begins (Badu)" : service_badu_start_times,
        "Service Time (Badu)" : service_badu_duration_times,
        "Time Service Ends (Badu)" : service_badu_end_times,
    }
    
    simulation_dataframe = pd.DataFrame(simulation_data)
    return simulation_dataframe


def main():
    print(simulate())


if __name__ == '__main__':
    main()
