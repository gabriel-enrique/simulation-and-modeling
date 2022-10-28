# Ferry Queue

## Problem Description

A common problem for river ferry operators is the positioning of vehicles on the ferry deck so that the maximum number of vehicles can be safely parked. Unlike the situation for cross-channel ferries, data about the numbers of cars and lorries will not be known in advance. This means that the river operators do not generally bother to sort out separate areas for cars and lorries but just load up on a FCFS basis.

Using the following data, we want to see how this situation works in practice.

 - The vehicle deck is 32 m long and can take two columns of vehicles side by side.
 - Vehicles arrive at random and form a single queue while waiting for loading instructions.
 - On average, 40% of the vehicles are cars, 55% are lorries, and 5% are motorcycles.
 - The car length varies between 3.5 m and 5.5 m, while the lorry length is between 8.0 m and 10.0 m.

The problem is to work out how many vehicles will be carried, whether they are cars or lorries and how much wasted space there is.

We can think of:

 - Is the next vehicle to board a car or lorry?
 - What is the length of the vehicle?
 - Which of the two parking columns does the vehicle join?
 - Do motorcycles matter?

Random numbers are needed to indicate what sort of vehicle is being loaded, and to indicate the lengths of each vehicle.

## Simulation Model

There are 3 types of vehicles, each with its own distributions.

| Type       | Distribution |
|------------|--------------|
| Car        | 40%          |
| Lorry      | 55%          |
| Motorcycle | 5%           |

The length of each vehicle types, except Motorcycles, varies. We use a normal distribution to indicate the length of each vehicle which lengths varies. For Motorcycles, we use a uniform length of 2 meters. All lengths are in meters.

| Vehicle    | Minimum Length | Maximum Length |
|------------|----------------|----------------|
| Car        | 3.5            | 5.5            |
| Lorry      | 8              | 10             |
| Motorcycle | 2              | 2              |

We also consider the width of the vehicle. For Cars and Lorries, their width takes the entire column width. Meanwhile, Motorcycles' width takes half of the column width.

We proposed two boarding methods and two layout methods. In total there are 4 boarding-layout methods combinations that we simulate.

### Boarding Methods

1. Board vehicles to one column at a time. Starting from the first column, then when we can't board anymore vehicle, start boarding to the second column. Once the second column is full then stop.
1. Board vehicles to the column with less vehicle in terms of length. If both columns have the same length of vehicles, then board to the first column. Stop when we can’t board anymore vehicles.

### Layout Methods

1. We treat Motorcycles as any other vehicle, allocating the entire column width for one Motorcycle. Note that we can actually fit two Motorcycle at the cost of one Motorcycle length due to the fact that a Motorcycle's width is half of the column's width.
1. When we are trying to board a Motorcycle, we search 10 places back from the start of the queue for another Motorcycle. If we found one, we can fit those two Motorcycles at the cost of one Motorcycle length. If we don't find any Motorcycle within the first 10 vehicles from the start of the queue, then we treat that single Motorcycle like any other vehicle (Layout Method 1).

## Running the Simulation

To run the simulation, you only need to run the `ferry_sim.py` file.

The results for each boarding-layout method simulation will show you the vehicle line-up for each column, total vehicles boarded, column length used, and the wasted space.

## Results, Analysis, and Discussion

Here are the simulation results:

```
====================
      Method 1      
====================
=== Vehicles ===
Column 1: Lorry (8.69 m) -> Lorry (9.85 m) -> Car (3.54 m) -> Car (4.91 m)
Column 2: Lorry (8.61 m) -> Car (5.25 m) -> Lorry (9.01 m) -> Lorry (8.95 m)
Total Vehicles :  8

=== Deck Length Used ===
Deck Length          :    32 m
Column 1 Length Used : 26.99 m (84.34 %)
Column 2 Length Used : 31.82 m (99.44 %)

=== Deck Area ===
Total Used Area : 58.81 m^2
Deck Total Area :    64 m^2
Wasted Area     :     8 %


====================
      Method 2
====================
=== Vehicles ===
Column 1: Car (5.14 m) -> Lorry (9.77 m) -> Car (4.81 m) -> Lorry (9.26 m)
Column 2: Lorry (8.12 m) -> Car (4.24 m) -> Lorry (9.51 m) -> Lorry (9.81 m)
Total Vehicles :  8

=== Deck Length Used ===
Deck Length          :    32 m
Column 1 Length Used : 28.98 m (90.56 %)
Column 2 Length Used : 31.68 m ( 99.0 %)

=== Deck Area ===
Total Used Area : 60.66 m^2
Deck Total Area :    64 m^2
Wasted Area     :     5 %

====================
      Method 3
====================
=== Vehicles ===
Column 1: Lorry (9.9 m) -> Lorry (8.72 m) -> Lorry (9.52 m)
Column 2: Car (4.07 m) -> Lorry (9.13 m) -> Lorry (9.15 m) -> Lorry (9.16 m)
Total Vehicles :  7

=== Deck Length Used ===
Deck Length          :    32 m
Column 1 Length Used : 28.14 m (87.94 %)
Column 2 Length Used : 31.51 m (98.47 %)

=== Deck Area ===
Total Used Area : 59.65 m^2
Deck Total Area :    64 m^2
Wasted Area     :     7 %


====================
      Method 4
====================
=== Vehicles ===
Column 1: Car (5.04 m) -> Lorry (9.17 m) -> Lorry (9.53 m)
Column 2: Car (4.82 m) -> Lorry (8.56 m) -> Lorry (9.64 m) -> Car (3.85 m)
Total Vehicles :  7

=== Deck Length Used ===
Deck Length          :    32 m
Column 1 Length Used : 23.74 m (74.19 %)
Column 2 Length Used : 26.87 m (83.97 %)

=== Deck Area ===
Total Used Area : 50.61 m^2
Deck Total Area :    64 m^2
Wasted Area     :    21 %
```

As we can see, the Total Vehicles and Wasted Area from different methods of boarding-layout combinations does not seem to form a pattern.

This might happen because our layout methods are composed based on the fact that we want to optimize the boarding of Motorcycles. However, because the distribution of Motorcycles is low, those different methods does not make any significant changes to the Total Vehicles and/or Wasted Area.

The results from Method 4 are worse than the other methods, especially the Wasted Area (`21 %`). We suspect that this is not because of the different boarding-layout method. Rather, it is more likely to happen because there are so many Lorries that are boarded. The fact that Method 4 does not contain any Motorcycles shows that, in this specific results, Method 4 is just a "bad luck" case of Method 2; as they share the same boarding method.

Generally speaking, Boarding Method 2 is better than Boarding Methods 1 because it utilizes available spaces more efficiently.

We would still recommend Method 4 as the go-to method, as it will make better use of the Deck Total Area in courtesy of Layout Method 2, and the use of Deck Length in courtesy of Boarding Method 2. Despite that, choosing any method given above will still yield similar results; considering the distribution of vehicles stays the same.
