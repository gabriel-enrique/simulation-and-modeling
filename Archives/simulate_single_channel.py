import os
import random


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


def customer():
    return arrival(), service()


def simulate():
    # simulation parameters
    total_customers = 20

    # simulation data
    arrival_times = []
    service_start_times = []
    service_times = []
    service_end_times = []

    # first customer
    arrival_time, service_time = customer()
    arrival_times.append(arrival_time)
    service_times.append(service_time)

    # rest of the customers
    for i in range(total_customers - 1):
        arrival_time, service_time = customer()
        arrival_times.append(arrival_times[i] + arrival_time)
        service_times.append(service_time)

    # simulation starts
    clock = 0
    customer_served = 0
    is_ready = True
    while customer_served < total_customers:
        # ready to service and customer in queue
        if is_ready and (arrival_times[customer_served] <= clock):
            is_ready = False # start servicing
            service_start_times.append(clock)
            service_end_times.append(clock + service_times[customer_served])
        
        # finished servicing
        elif (not is_ready) and (clock == service_end_times[customer_served]):
            is_ready = True
            customer_served += 1

            # theres another customer in queue
            if (customer_served < total_customers) and (arrival_times[customer_served] <= clock):
                is_ready = False # start servicing
                service_start_times.append(clock)
                service_end_times.append(clock + service_times[customer_served])

        clock += 1

    # simulation results table
    table_header = [
        'Customer Number',
        'Arrival Time',
        'Time Service Begins',
        'Service Time',
        'Time Service Ends',
    ]

    print("{:<20} | {:<20} | {:<20} | {:<20} | {:<20}".format(
        table_header[0],
        table_header[1],
        table_header[2],
        table_header[3],
        table_header[4]
    ))

    print("-" * ((5*20) + (3*4)))

    for i in range(total_customers):
        print ("{:<20} | {:<20} | {:<20} | {:<20} | {:<20}".format(
            i+1,
            arrival_times[i],
            service_start_times[i],
            service_times[i],
            service_end_times[i]
        ))

    # simulation analization
    average_waiting_time = sum(list(map(lambda x, y : y - x, arrival_times, service_start_times))) / customer_served
    print(f"Average Waiting Time: {average_waiting_time}")

    total_idle_time = 0
    for i in range(1, total_customers):
        total_idle_time += service_start_times[i] - service_end_times[i-1]
    idle_time_percentage = (total_idle_time / (clock - 1)) * 100
    print(f"Idle Time (Percentage): {round(idle_time_percentage, 2)} %")


def main():
    simulate()
    while input("Press 'Enter' to simulate again. 'N' to stop. ").lower() == "":
        os.system('cls')
        simulate()


if __name__ == '__main__':
    main()
