# Dump Truck Problem

## Problem Description

A dump truck pipeline system which consists of truck(s), loader(s) and scaler(s) needs to be analysed. A truck will arrive to the system at the loader queue. After the truck is done being loaded, the truck will enter the scaler queue. After done being scaled, the truck will exit the system and travel back to the start of the system, i.e., the loader queue.

## Simulation Model

The simulation model has these components.

### System States

 - `L(t)` - the number of trucks in Loader at time `t`
 - `S(t)` - the number of trucks in Scaler at time `t`
 - `LQ(t)` - the number of trucks in Loader queue at time `t`
 - `LQ(t)` - the number of trucks in Scaler queue at time `t`
 - `T(t)` - the number of trucks Traveling at time `t`

### Entities

The model will have a single entity type: `Truck`. This entity will represent the trucks in the system cycle.

### List

 - **Loader Queue** - using a first come, first served (FIFO) principle
 - **Scaler Queue** - using a first come, first served (FIFO) principle

### Event Notice

 - `(ALQ, t, T)` - truck `T` arrives at the **Loader Queue** at time `t`
 - `(FL, t, T)` - truck `T` finished loading at time `t`
 - `(FS, t, T)` - truck `T` finished scaling at time `t`

### Activities

 - **Loading Time** - the time needed for a truck to be loaded

    | Loading Time | Probability |
    |--------------|-------------|
    | 5            | 0.30        |
    | 10           | 0.50        |
    | 15           | 0.20        |

 - **Scaling Time** - the time needed for a truck to be scaled

    | Scaling Time | Probability |
    |--------------|-------------|
    | 12           | 0.70        |
    | 16           | 0.30        |

 - **Traveling Time** - the time needed for a truck to travel

    | Traveling Time | Probability |
    |----------------|-------------|
    | 40             | 0.40        |
    | 60             | 0.30        |
    | 80             | 0.20        |
    | 100            | 0.10        |

### Delays

 - **Truck Loader Queue Wait Time** - the time a truck spends in the **Loader Queue**
 - **Truck Scaler Queue Wait Time** - the time a truck spends in the **Scaler Queue**

### Initial Condition

All the truck(s) will arrive to the system at clock time `0`.

### Clock

The simulation clock will be in minutes and the simulation will stop when the clock passes the 1440 minute mark. For context, 1440 minutes is 24 hours.

## Running the Simulation

To run the simulation, you only need to run the `dump_truck.py` file.

You can modify the number of trucks, loader and scaler from the `simulate()` arguments.
