import os
import random


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


def customer():
    return arrival()


def simulate():
    # simulation parameters
    total_customers = 20

    # simulation data
    arrival_times = []
    service_start_times = []
    service_times = []
    service_end_times = []

    # first customer
    arrival_time = customer()
    arrival_times.append(arrival_time)

    # rest of the customers
    for i in range(total_customers - 1):
        arrival_time = customer()
        arrival_times.append(arrival_times[i] + arrival_time)

    # simulation starts
    clock = 0
    customer_served = 0
    ali_ready = True
    badu_ready = True
    serviced_by_ali = []
    while customer_served < total_customers:
        # ali ready to service and customer in queue
        if ali_ready and (arrival_times[customer_served] <= clock):
            ali_ready = False
            serviced_by_ali.append(customer_served)
            service_times.append(service_ali())
            service_start_times.append(clock)
            service_end_times.append(clock + service_times[customer_served])

        # ali ready to service and customer in queue
        elif badu_ready and (arrival_times[customer_served] <= clock):
            badu_ready = False
            service_times.append(service_badu())
            service_start_times.append(clock)
            service_end_times.append(clock + service_times[customer_served])

        # ali finished servicing
        elif (not ali_ready) and (clock == service_end_times[customer_served]):
            

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
