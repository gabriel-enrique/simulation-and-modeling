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


def get_max(end_times):
    curr_max = end_times[0]

    for i in range(len(end_times)):
        if type(end_times[i]) == str:
            continue

        if end_times[i] > curr_max:
            curr_max = end_times[i]

    return curr_max


def get_end_times(all_server_end_times):
    end_times = []

    for server_end_times in all_server_end_times:
        end_times.append(get_max(server_end_times))

    return end_times


def get_first_done(end_times):
    min_index = 0

    for i in range(len(end_times)):
        if end_times[i] < end_times[min_index]:
            min_index = i

    return min_index


def simulate():
    # simulation parameters
    total_customers = 20
    total_servers = 2

    # simulation data
    arrival_times = [0]
    served_by = [""]
    service_start_times = []
    service_duration_times = []
    service_end_times = []

    for i in range(total_servers):
        service_start_times.append([0])
        service_duration_times.append([0])
        service_end_times.append([0])

    # simulation starts
    for i in range(1, total_customers + 1):
        arrival_times.append(arrival_times[i-1] + arrival())

        end_times = get_end_times(service_end_times)
        server = None
        for s in range(total_servers):
            if arrival_times[i] >= end_times[s]:
                server = s
                break
        
        if server == None:
            server = get_first_done(end_times)
        
        for s in range(total_servers):
            if server == s:
                served_by.append(f"Server {s}")
                service_start_times[s].append(max(arrival_times[i], end_times[s]))
                service_duration_times[s].append(service())
                service_end_times[s].append(service_start_times[s][i] + service_duration_times[s][i])
            else:
                service_start_times[s].append("")
                service_duration_times[s].append("")
                service_end_times[s].append("")

    # simulation results table
    simulation_data = {
        "Customer Number" : np.arange(total_customers + 1),
        "Arrival Time" : arrival_times,
        "Served By" : served_by,
    }

    for s in range(total_servers):
        simulation_data[f"Time Service Begins (Server {s})"] = service_start_times[s]
        simulation_data[f"Service Time (Server {s})"] = service_duration_times[s]
        simulation_data[f"Time Service Ends (Server {s})"] = service_end_times[s]

    simulation_dataframe = pd.DataFrame(simulation_data)
    return simulation_dataframe


def main():
    print(simulate())


if __name__ == '__main__':
    main()
