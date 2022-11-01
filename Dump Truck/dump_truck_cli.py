import pandas as pd
import os

from random import choices
from copy import deepcopy
from textwrap import dedent


class Truck:
    def __init__(self, name: str) -> None:
        self.name = name

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return str(self)     


class Event:
    def __init__(self, event_type: str, t: int, truck: Truck) -> None:
        if event_type not in ["ALQ", "FL", "FS"]:
            raise ValueError(f"Invalid event type {event_type}. Must be one of (ALQ, FL, FS).")
        self.type = event_type
        self.time = t
        self.truck = truck
    
    def __lt__(self, other) -> bool:
        if self.time == other.time:
            if self.type == "ALQ":
                return False
            elif self.type == "FL":
                return True if (other.type == "ALQ") else False
            elif self.type == "FS":
                return False if (other.type == "FS") else True
        return self.time < other.time

    def __str__(self) -> str:
        return f"({self.type}, {self.time}, {str(self.truck)})"

    def __repr__(self) -> str:
        return str(self)


def loading():
    minutes = [5, 10, 15]
    prob = [0.30, 0.50, 0.20]

    return choices(minutes, prob)[0]


def scale():
    minutes = [12, 16]
    prob = [0.70, 0.30]

    return choices(minutes, prob)[0]


def travel():
    minutes = [40, 60, 80, 100]
    prob = [0.40, 0.30, 0.20, 0.1]

    return choices(minutes, prob)[0]


def get_imminent_event(fel) -> Event:
    first_to_happen = fel[0]
    index = 0

    for i in range(1, len(fel)):
        if fel[i] < first_to_happen:
            first_to_happen = fel[i]
            index = i

    fel.pop(index)
    return first_to_happen


def simulate(num_trucks, num_loader, num_scaler, output_filename):
    # snapshots
    snapshots_clock = []
    snapshots_trucks_in_loader = []
    snapshots_trucks_in_scaler = []
    snapshots_trucks_in_loader_queue = []
    snapshots_trucks_in_scaler_queue = []
    snapshots_trucks_traveling = []
    snapshots_loader_queue = []
    snapshots_scaler_queue = []
    snapshots_fel = []
    snapshots_total_loader_busy_time = []
    snapshots_total_scaler_busy_time = []
    snapshots_total_loader_wait_time = []
    snapshots_total_scaler_wait_time = []
    snapshots_total_wait_time = []
    snapshots_total_service_time = []
    snapshots_total_system_time = []
    snapshots_total_loaded_count = []
    snapshots_total_scaled_count = []
    snapshots_total_service_count = []
    
    # clock
    clock = 0

    # system states
    trucks_in_loader = 0
    trucks_in_scaler = 0
    trucks_in_loader_queue = 0
    trucks_in_scaler_queue = 0
    trucks_traveling = 0

    # lists
    loader_queue = []
    scaler_queue = []

    # future event list
    fel = []

    # cumulative statistics
    total_loader_busy_time = 0
    total_scaler_busy_time = 0
    total_loader_wait_time = 0
    total_scaler_wait_time = 0
    total_wait_time = 0
    total_service_time = 0
    total_system_time = 0
    total_loaded_count = 0
    total_scaled_count = 0
    total_service_count = 0

    # initial conditions
    for i in range(num_trucks):
        fel.append(Event("ALQ", 0, Truck(f"Truck {i+1}")))
    trucks_traveling = num_trucks

    # simulation runs
    while (clock <= 1440): # 24 hours = 1440 minutes
        prev_clock = clock
        event = get_imminent_event(fel)
        clock = event.time

        total_loader_busy_time += (trucks_in_loader * (clock - prev_clock))
        total_scaler_busy_time += (trucks_in_scaler * (clock - prev_clock))
        total_loader_wait_time += (trucks_in_loader_queue * (clock - prev_clock))
        total_scaler_wait_time += (trucks_in_scaler_queue * (clock - prev_clock))
        total_wait_time = total_loader_wait_time + total_scaler_wait_time
        total_service_time = total_loader_busy_time + total_scaler_busy_time
        total_system_time = total_wait_time + total_service_time

        if event.type == "ALQ":
            trucks_traveling -= 1
            trucks_in_loader_queue += 1
            loader_queue.append(event.truck)
        elif event.type == "FL":
            trucks_in_loader -= 1
            total_loaded_count += 1
            trucks_in_scaler_queue += 1
            scaler_queue.append(event.truck)
        elif event.type == "FS":
            trucks_in_scaler -= 1
            total_scaled_count += 1
            total_service_count += 1
            trucks_traveling += 1
            fel.append(Event("ALQ", clock + travel(), event.truck))

        if (trucks_in_scaler < num_scaler) and (trucks_in_scaler_queue > 0):
            trucks_in_scaler_queue -= 1
            truck = scaler_queue.pop(0)
            trucks_in_scaler += 1
            fel.append(Event("FS", clock + scale(), truck))

        if (trucks_in_loader < num_loader) and (trucks_in_loader_queue > 0):
            trucks_in_loader_queue -= 1
            truck = loader_queue.pop(0)
            trucks_in_loader += 1
            fel.append(Event("FL", clock + loading(), truck))
        
        snapshots_clock.append(clock)
        snapshots_trucks_in_loader.append(trucks_in_loader)
        snapshots_trucks_in_scaler.append(trucks_in_scaler)
        snapshots_trucks_in_loader_queue.append(trucks_in_loader_queue)
        snapshots_trucks_in_scaler_queue.append(trucks_in_scaler_queue)
        snapshots_trucks_traveling.append(trucks_traveling)
        snapshots_loader_queue.append(deepcopy(loader_queue))
        snapshots_scaler_queue.append(deepcopy(scaler_queue))
        snapshots_fel.append(deepcopy(fel))
        snapshots_total_loader_busy_time.append(total_loader_busy_time)
        snapshots_total_scaler_busy_time.append(total_scaler_busy_time)
        snapshots_total_loader_wait_time.append(total_loader_wait_time)
        snapshots_total_scaler_wait_time.append(total_scaler_wait_time)
        snapshots_total_wait_time.append(total_wait_time)
        snapshots_total_service_time.append(total_service_time)
        snapshots_total_system_time.append(total_system_time)
        snapshots_total_loaded_count.append(total_loaded_count)
        snapshots_total_scaled_count.append(total_scaled_count)
        snapshots_total_service_count.append(total_service_count)
    
    # simulation results table
    simulation_data = {
        "Clock (t)" : snapshots_clock,
        "L(t)" : snapshots_trucks_in_loader,
        "S(t)" : snapshots_trucks_in_scaler,
        "LQ(t)" : snapshots_trucks_in_loader_queue,
        "LQ(t)" : snapshots_trucks_in_scaler_queue,
        "T(t)" : snapshots_trucks_traveling,
        "Loader Queue" : snapshots_loader_queue,
        "Scaler Queue" : snapshots_scaler_queue,
        "Future Event List" : snapshots_fel,
        "Lb" : snapshots_total_loader_busy_time,
        "Sb" : snapshots_total_scaler_busy_time,
        "Lw" : snapshots_total_loader_wait_time,
        "Sw" : snapshots_total_scaler_wait_time,
        "TotQ" : snapshots_total_wait_time,
        "TotServ" : snapshots_total_service_time,
        "TotSys" : snapshots_total_system_time,
        "CountL" : snapshots_total_loaded_count,
        "CountS" : snapshots_total_scaled_count,
        "CountServ" : snapshots_total_service_count,
    }
    
    simulation_dataframe = pd.DataFrame(simulation_data)
    simulation_dataframe.to_csv(output_filename, index=False)
    print(simulation_dataframe)
    print()

    # simulation statistics
    print("{:<35}: {:>6} %".format("Loader utilization", round(((total_loader_busy_time / num_loader) / clock) * 100, 2)))
    print("{:<35}: {:>6} %".format("Scaler utilization", round(((total_scaler_busy_time / num_scaler) / clock) * 100, 2)))
    print("{:<35}: {:>6} minute(s)".format("Average time truck in Loader queue", round(total_loader_wait_time / total_loaded_count, 2)))
    print("{:<35}: {:>6} minute(s)".format("Average time truck in Scaler queue", round(total_scaler_wait_time / total_scaled_count, 2)))
    print("{:<35}: {:>6} minute(s)".format("Average time truck in system", round(total_system_time / total_service_count, 2)))
    print("{:<35}: {:>6} %".format("Trucks waiting percentage", round(((total_wait_time / num_trucks) / clock) * 100, 2)))
    print("{:<35}: {:>6} %".format("Trucks in system percentage", round(((total_system_time / num_trucks) / clock) * 100, 2)))


def main():
    try:
        num_trucks = int(input("Number of Truck(s): "))
        num_loader = int(input("Number of Loader(s): "))
        num_scaler = int(input("Number of Scaler(s): "))
    except ValueError:
        print("Value must be an integer!")
        exit()
    
    output_filename = input("Output file (leave blank to use default simulation_table.csv): ") or "simulation_table.csv"

    simulate(
        num_trucks=num_trucks, 
        num_loader=num_loader, 
        num_scaler=num_scaler, 
        output_filename=output_filename
    )

    print(dedent("""
    ===== Legend =====
    L(t) : # of trucks in Loader
    S(t) : # of trucks in Scaler
    LQ(t) : # of trucks in Loader queue
    LQ(t) : # of trucks in Scaler queue
    T(t) : # of trucks Traveling
    Lb : total loader busy time
    Sb : total scaler busy time
    Lw : total loader queue wait time
    Sw : total scaler queue wait time
    TotQ : total time waiting in queue
    TotServ : total time serviced (loader and scaler)
    TotSys : total time in system
    CountL : # of trucks loaded
    CountS : # of trucks scaled
    CountServ : # of trucks fully serviced  
    """))
    print()

    input("Press ENTER to exit the progam")


if __name__ == "__main__":
    main()
