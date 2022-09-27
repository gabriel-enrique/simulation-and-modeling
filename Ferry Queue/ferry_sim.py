from random import choices, random


class Queue:
    def __init__(self, size=50):
        self.queue = []
        self.__generate(size)

    def __generate(self, size):
        self.queue += [self.__vehicle() for _ in range(size)]

    def __vehicle(self):
        vehicle_type = [Car(), Lorry(), Motorcycle()]
        prob = [0.4, 0.55, 0.05]
        return choices(vehicle_type, prob)[0]
    
    def first(self):
        return self.queue[0]

    def dequeue(self):
        self.__generate(1)
        return self.queue.pop(0)

    def find_next_motorcycle(self, search_length=10):
        self.__generate(max(0, search_length - len(self.queue)))
        for i in range(search_length):
            if type(self.queue[i]) == Motorcycle:
                return self.queue.pop(i)
        return None


class Car:
    def __init__(self):
        self.length = self.__length()

    def __length(self):
        return round(3.5 + 2*random(), 2)

    def __str__(self):
        return f"Car ({self.length} m)"


class Lorry:
    def __init__(self):
        self.length = self.__length()

    def __length(self):
        return round(8 + 2*random(), 2)

    def __str__(self):
        return f"Lorry ({self.length} m)"


class Motorcycle:
    def __init__(self):
        self.length = self.__length()

    def __length(self):
        return 2

    def __str__(self):
        return f"Motorcycle ({self.length} m)"


class Simulations:
    def run(self):
        self.method_1()
        print()

        self.method_2()
        print()

        self.method_3()
        print()

        self.method_4()
        print()
        

    def method_1(self):
        '''
         - Fill up one column at a time
         - Motorcycles are allocated one column width (actual half)
        '''
        # simulation parameters
        column_length = 32
        column_width = 1
        total_area = 2 * (column_width * column_length)

        # simulation data
        column_1 = []
        column_2 = []
        column_1_used = 0
        column_2_used = 0
        area_used = 0
        vehicles_count = 0

        queue = Queue()

        column_1_available = True
        while column_1_available:
            if (column_1_used + queue.first().length) <= column_length:
                vehicle = queue.dequeue()
                column_1.append(vehicle)
                column_1_used += vehicle.length
                area_used += (((column_width / 2) if type(vehicle) == Motorcycle else column_width) * vehicle.length)
                vehicles_count += 1
            else:
                column_1_available = False

        column_2_available = True
        while column_2_available:
            if (column_2_used + queue.first().length) <= column_length:
                vehicle = queue.dequeue()
                column_2.append(vehicle)
                column_2_used += vehicle.length
                area_used += (((column_width / 2) if type(vehicle) == Motorcycle else column_width) * vehicle.length)
                vehicles_count += 1
            else:
                column_2_available = False

        # simulation results
        print("====================")
        print("      Method 1      ")
        print("====================")
        
        print("=== Vehicles ===")
        print("Column 1: ", end="")
        print(" -> ".join(list(map(str, column_1))), end="\n")
        print("Column 2: ", end="")
        print(" -> ".join(list(map(str, column_2))), end="\n")
        print("Total Vehicles : {:>2}".format(vehicles_count))
        print()

        print("=== Deck Length Used ===")
        print("Deck Length          : {:>5} m".format(column_length))
        print("Column 1 Length Used : {:>5} m ({:>5} %)".format(round(column_1_used, 2), round((column_1_used / column_length) * 100, 2)))
        print("Column 2 Length Used : {:>5} m ({:>5} %)".format(round(column_2_used, 2), round((column_2_used / column_length) * 100, 2)))
        print()

        print("=== Deck Area ===")
        print("Total Used Area : {:>5} m^2".format(round(area_used, 2)))
        print("Deck Total Area : {:>5} m^2".format(total_area))
        print("Wasted Area     : {:>5} %".format(100 - round((area_used / total_area) * 100), 2))
        print()


    def method_2(self):
        '''
         - Fill up column with less vehicle first (shortest)
         - Motorcycles are allocated one column width (actual half)
        '''
        # simulation parameters
        column_length = 32
        column_width = 1
        total_area = 2 * (column_width * column_length)

        # simulation data
        column_1 = []
        column_2 = []
        column_1_used = 0
        column_2_used = 0
        area_used = 0
        vehicles_count = 0

        queue = Queue()

        while True:
            if (column_1_used <= column_2_used) and ((column_1_used + queue.first().length) <= column_length):
                vehicle = queue.dequeue()
                column_1.append(vehicle)
                column_1_used += vehicle.length
                area_used += (((column_width / 2) if type(vehicle) == Motorcycle else column_width) * vehicle.length)
                vehicles_count += 1
            elif (column_2_used + queue.first().length) <= column_length:
                vehicle = queue.dequeue()
                column_2.append(vehicle)
                column_2_used += vehicle.length
                area_used += (((column_width / 2) if type(vehicle) == Motorcycle else column_width) * vehicle.length)
                vehicles_count += 1
            else:
                break
        
        # simulation results
        print("====================")
        print("      Method 2      ")
        print("====================")

        print("=== Vehicles ===")
        print("Column 1: ", end="")
        print(" -> ".join(list(map(str, column_1))), end="\n")
        print("Column 2: ", end="")
        print(" -> ".join(list(map(str, column_2))), end="\n")
        print("Total Vehicles : {:>2}".format(vehicles_count))
        print()

        print("=== Deck Length Used ===")
        print("Deck Length          : {:>5} m".format(column_length))
        print("Column 1 Length Used : {:>5} m ({:>5} %)".format(round(column_1_used, 2), round((column_1_used / column_length) * 100, 2)))
        print("Column 2 Length Used : {:>5} m ({:>5} %)".format(round(column_2_used, 2), round((column_2_used / column_length) * 100, 2)))
        print()

        print("=== Deck Area ===")
        print("Total Used Area : {:>5} m^2".format(round(area_used, 2)))
        print("Deck Total Area : {:>5} m^2".format(total_area))
        print("Wasted Area     : {:>5} %".format(100 - round((area_used / total_area) * 100), 2))


    def method_3(self):
        '''
         - Fill up one column at a time
         - Motorcycles are allocated half of column width (will try to put 2 motorcycle together side-by-side)
        '''
        # simulation parameters
        column_length = 32
        column_width = 1
        total_area = 2 * (column_width * column_length)

        # simulation data
        column_1 = []
        column_2 = []
        column_1_used = 0
        column_2_used = 0
        area_used = 0
        vehicles_count = 0

        queue = Queue()

        column_1_available = True
        while column_1_available:
            if (column_1_used + queue.first().length) <= column_length:
                vehicle = queue.dequeue()
                if type(vehicle) == Motorcycle:
                    next_motorcycle = queue.find_next_motorcycle()
                    if next_motorcycle:
                        column_1.append((vehicle, next_motorcycle))
                        column_1_used += vehicle.length
                        area_used += (column_width * vehicle.length)
                        vehicles_count += 2
                        continue
                column_1.append(vehicle)
                column_1_used += vehicle.length
                area_used += (((column_width / 2) if type(vehicle) == Motorcycle else column_width) * vehicle.length)
                vehicles_count += 1
            else:
                column_1_available = False

        column_2_available = True
        while column_2_available:
            if (column_2_used + queue.first().length) <= column_length:
                vehicle = queue.dequeue()
                if type(vehicle) == Motorcycle:
                    next_motorcycle = queue.find_next_motorcycle()
                    if next_motorcycle:
                        column_2.append((vehicle, next_motorcycle))
                        column_2_used += vehicle.length
                        area_used += (column_width * vehicle.length)
                        vehicles_count += 2
                        continue
                column_2.append(vehicle)
                column_2_used += vehicle.length
                area_used += (((column_width / 2) if type(vehicle) == Motorcycle else column_width) * vehicle.length)
                vehicles_count += 1
            else:
                column_2_available = False

        # simulation results
        print("====================")
        print("      Method 3      ")
        print("====================")
        
        print("=== Vehicles ===")
        print("Column 1: ", end="")
        print(" -> ".join(list(map(lambda x : f"({str(x[0])}, {str(x[1])})" if type(x) == tuple else str(x), column_1))), end="\n")
        print("Column 2: ", end="")
        print(" -> ".join(list(map(lambda x : f"({str(x[0])}, {str(x[1])})" if type(x) == tuple else str(x), column_2))), end="\n")
        print("Total Vehicles : {:>2}".format(vehicles_count))
        print()

        print("=== Deck Length Used ===")
        print("Deck Length          : {:>5} m".format(column_length))
        print("Column 1 Length Used : {:>5} m ({:>5} %)".format(round(column_1_used, 2), round((column_1_used / column_length) * 100, 2)))
        print("Column 2 Length Used : {:>5} m ({:>5} %)".format(round(column_2_used, 2), round((column_2_used / column_length) * 100, 2)))
        print()

        print("=== Deck Area ===")
        print("Total Used Area : {:>5} m^2".format(round(area_used, 2)))
        print("Deck Total Area : {:>5} m^2".format(total_area))
        print("Wasted Area     : {:>5} %".format(100 - round((area_used / total_area) * 100), 2))
        print()
        

    def method_4(self):
        '''
         - Fill up column with less vehicle first (shortest)
         - Motorcycles are allocated half of column width (will try to put 2 motorcycle together side-by-side)
        '''
        # simulation parameters
        column_length = 32
        column_width = 1
        total_area = 2 * (column_width * column_length)

        # simulation data
        column_1 = []
        column_2 = []
        column_1_used = 0
        column_2_used = 0
        area_used = 0
        vehicles_count = 0

        queue = Queue()

        while True:
            if (column_1_used <= column_2_used) and ((column_1_used + queue.first().length) <= column_length):
                vehicle = queue.dequeue()
                if type(vehicle) == Motorcycle:
                    next_motorcycle = queue.find_next_motorcycle()
                    if next_motorcycle:
                        column_1.append((vehicle, next_motorcycle))
                        column_1_used += vehicle.length
                        area_used += (column_width * vehicle.length)
                        vehicles_count += 2
                        continue
                column_1.append(vehicle)
                column_1_used += vehicle.length
                area_used += (((column_width / 2) if type(vehicle) == Motorcycle else column_width) * vehicle.length)
                vehicles_count += 1
            elif (column_2_used + queue.first().length) <= column_length:
                vehicle = queue.dequeue()
                if type(vehicle) == Motorcycle:
                    next_motorcycle = queue.find_next_motorcycle()
                    if next_motorcycle:
                        column_2.append((vehicle, next_motorcycle))
                        column_2_used += vehicle.length
                        area_used += (column_width * vehicle.length)
                        vehicles_count += 2
                        continue
                column_2.append(vehicle)
                column_2_used += vehicle.length
                area_used += (((column_width / 2) if type(vehicle) == Motorcycle else column_width) * vehicle.length)
                vehicles_count += 1
            else:
                break

        # simulation results
        print("====================")
        print("      Method 4      ")
        print("====================")
        
        print("=== Vehicles ===")
        print("Column 1: ", end="")
        print(" -> ".join(list(map(lambda x : f"({str(x[0])}, {str(x[1])})" if type(x) == tuple else str(x), column_1))), end="\n")
        print("Column 2: ", end="")
        print(" -> ".join(list(map(lambda x : f"({str(x[0])}, {str(x[1])})" if type(x) == tuple else str(x), column_2))), end="\n")
        print("Total Vehicles : {:>2}".format(vehicles_count))
        print()

        print("=== Deck Length Used ===")
        print("Deck Length          : {:>5} m".format(column_length))
        print("Column 1 Length Used : {:>5} m ({:>5} %)".format(round(column_1_used, 2), round((column_1_used / column_length) * 100, 2)))
        print("Column 2 Length Used : {:>5} m ({:>5} %)".format(round(column_2_used, 2), round((column_2_used / column_length) * 100, 2)))
        print()

        print("=== Deck Area ===")
        print("Total Used Area : {:>5} m^2".format(round(area_used, 2)))
        print("Deck Total Area : {:>5} m^2".format(total_area))
        print("Wasted Area     : {:>5} %".format(100 - round((area_used / total_area) * 100), 2))
        print()
        

def main():
    Simulations().run()


if __name__ == "__main__":
    main()
