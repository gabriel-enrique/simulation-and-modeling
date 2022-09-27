# Ferry Queue

## Problem Description

A common problem for river ferry operators is the positioning of vehicles on the ferry deck so that the maximum number of vehicles can be safely parked. Unlike the situation for cross-channel ferries, data about the numbers of cars and lorries will not be known in advance. This means that the river operators do not generally bother to sort out separate areas for cars and lorries but just load up on a FCFS basis.

Using the following data, we want to see how this situation works in practice.

 - The vehicle deck is 32 m long and can take two columns of vehicles side by side.
 - Vehicles arrive at random and form a single queue while waiting for loading instructions.
 - On average, 40% of the vehicles are cars, 55% are lorries, and 5% are motor cycles.
 - The car length varies between 3.5 m and 5.5 m, while the lorry length is between 8.0 m and 10.0 m.

The problem is to work out how many vehicles will be carried, whether they are cars or lorries and how much wasted space there is.

We can think of:

 - Is the next vehicle to board a car or lorry?
 - What is the length of the vehicle?
 - Which of the two parking columns does the vehicle join?
 - Do motor cycles matter?

Random numbers are needed to indicate what sort of vehicle is being loaded, and to indicate the lengths of each vehicle.

## Simulation Model

There are 3 types of vehicles, each with its own distributions.

| Type       | Distribution |
|------------|--------------|
| Car        | 40%          |
| Lorry      | 55%          |
| Motorcycle | 5%           |

The length of each vehicle types, except Motorcycles, varies. We use a normal distribution to indicate the length of each vehicle which lenghts varies. For Motorcycles, we use a uniform length of 2 meters. All length are in meters.

| Vehicle    | Minimum Length | Maximum Length |
|------------|----------------|----------------|
| Car        | 3.5            | 5.5            |
| Lorry      | 8              | 10             |
| Motorcycle | 2              | 2              |

We also consider the width of the vehicle. For Cars and Lorries, their width takes the entire column width. Meanwhile, Motorcycles' width takes half of the column width.

We proposed two boarding methods and two layout methods. In total there are 4 boarding-layout methods combinations that we simulate.

### Boarding Methods

1. Board vehicles to one column at a time. Starting from the first column, then when we can't board anymore vehicle, start boarding to the second column. Once the second column is full then stop.
1. Board vehicles to the column with less vehicle in terms of length. If both column have the same length of vehicles, then board to the first column. Stop when we cant board anymore vehicles.

### Layout Methods

1. We treat Motorcycles as any other vehicle, allocating the entire column width for one Motorcycle. Note that we can actually fit two Motorcycle at the cost of one Motorcycle length due to the fact that a Motorcycle's width is half of the column's width.
1. When we are trying to board a Motorcycle, we search 10 places back from the start of the queue for another Motorcycle. If we found one, we can fit those two Motorcycles at the cost of one Motorcycle length. If we don't find any Motorcycle within the first 10 vehicles from the start of the queue, then we treat that single Motorcycle like any other vehicle (Layout Method 1).

## Running the Simulation

To run the simulation, you only need to run the `ferry_sim.py` file.

The results for each boarding-layout method simulation will show you the vehicle lineup for each column, total vehicles boarded, column length used, and the wasted space.
