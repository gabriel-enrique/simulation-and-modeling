# Gas Station Prices

## Problem Description

A common occurrence in retailing is competition between rival establishments over which shop can claim most of the market/customers. The most straightforward price war situation occur in supermarkets (like Indomaret, Alphamart, etc.) or in gas-stations (like Pertamina, Shell, BP, etc.)

Two gas stations operate from adjacent main road sites and vie with one another for business. Competition is also stiff from other gas stations not far away and profit margins from the sale of gasoline/petrol are very sensitive to suddent changes in demand.

On the other hand, the market is very large, and although both gas stations have regular customers, they realise that many of their sales are to ‘casual’ drivers.

If one day, one of the gas stations suddenly drops the price per litre as advertised to attract more of the market, what would the second gas station do to have a sales strategy so that, in altering the gasoline price, earnings will be as high as possible?

It is crucial to be able to predict how the second gas station market share will be affected by the sudden price drop by the first gas station.

## Simulation Model

There are 3 types of vehicles, each with its own distributions. We approximate the distribution of vehicle types based on our observation on an actual gas station.

| Type       | Distribution |
|------------|--------------|
| Motorcycle | 50%          |
| Car        | 40%          |
| Truck      | 10%          |

There are 6 types of fuel. Each type is based on the [Octane Rating](https://en.wikipedia.org/wiki/Octane_rating) (for Gasoline) and [Cetane Rating](https://en.wikipedia.org/wiki/Cetane_number) (for Diesel) ratings.

1. RON 90
1. RON 92
1. RON 98
1. CN 48
1. CN 51
1. CN 53

The probability distribution of fuel choice depends on the vehicle type. Again, we aporximate these distributions based on our observations.

| Vehicle    | Fuel Choice | Distribution |
|------------|-------------|--------------|
| Motorcycle | RON 90      | 100%         |
| Car        | RON 90      | 40%          |
| Car        | RON 92      | 30%          |
| Car        | RON 98      | 10%          |
| Car        | CN 51       | 5%           |
| Car        | CN 53       | 15%          |
| Truck      | CN 48       | 20%          |
| Truck      | CN 51       | 70%          |
| Truck      | CN 53       | 10%          |

The ranges of liters purchased also depends on the vehicle type. Here we use a uniform distribution. We did a research on the fuel tank capacity of each vehicle type to determine the maximum liters purhcased cap.

| Vehicle    | Minimum Liters | Maximum Liters |
|------------|----------------|----------------|
| Motorcycle | 1              | 4              |
| Car        | 1              | 45             |
| Truck      | 1              | 100            |

We choose [Pertamina](https://en.wikipedia.org/wiki/Pertamina) and [Shell](https://en.wikipedia.org/wiki/Shell_plc) as our gas stations. The prices of their fuel are obtained from their official websites and other sources. All prices are in Indonesian Rupiah.

> Some of Shell's fuel type are not available anymore in Indonesia, hence we don't know the actual price. For those types of fuel, we use approximation.

For a customer (vehicle) to choose which gas station to go to, the gasoline/diesel price of their choice will be the determining factor. So say that a `Car` wants to buy `RON 92` fuel, then only the prices of `RON 92` fuel from Pertamina and Shell will be the determining factor.

```py
def choose(pertamina_price, shell_price):
    delta = pertamina_price - shell_price
    delta /= 100 # scale down (normalize)
    middle = int(50 - delta) # round to int

    num = randint(1, 100) 

    if 1 <= num <= middle:
        return "Pertamina"
    elif (middle + 1) <= num <= 100:
        return "Shell"
```

Normally, if the fuel prices are the same, then they will both have a uniform distribution. However, if one of the prices is lower than the other, then the probability will favor the cheaper-fuel gas station more.

## Running the Simulation

To run the simulation, you only need to run the `gas_station_sim.py` file.

> We use [pandas](https://pandas.pydata.org/) and [NumPy](https://numpy.org/) library, so make sure you have those libraries installed.

The results will show you the simulation results table, total sales for both gas stations, and the distribution of vehicles.

You can change the fuel prices to see how the change of fuel prices affects both gas stations in terms of gross revenue.

## Results, Analysis, and Discussion

Here are some of the simulation results:

 - Normal prices
 ```
 Total Pertamina Sales    :        1,272,121,100
 Total Shell Sales        :          911,486,170
 ```

 - Shell drops `RON 90` prices
 ```
 Total Pertamina Sales    :        1,098,466,100
 Total Shell Sales        :          990,102,590
 ```

 - Shell drops `RON 90` and `CN 51` prices
 ```
 Total Pertamina Sales    :        1,032,937,900
 Total Shell Sales        :        1,072,629,220
 ```

 - Shell drops all prices
 ```
 Total Pertamina Sales    :        1,062,487,900
 Total Shell Sales        :        1,048,995,930
 ```

 - Pertamina and Shell drops `RON 90` and `CN 51` prices
 ```
 Total Pertamina Sales    :        1,013,362,600
 Total Shell Sales        :        1,020,096,400
 ```

 - Shel drops `RON 92`, `RON 98`, `CN 48`, and `CN 53` prices
 ```
 Total Pertamina Sales    :        1,143,909,200
 Total Shell Sales        :          959,722,460
 ```

When we see the distributions table, we can see that the most common fuel types are `RON 90` and `CN 51`. Droping either or both prices will surely affect a large pecentage of gross revenue.

However, if we drop the less-popular fuel types, the changes in the difference of gross revenue is not signifficant.

Hence, if one of the gas stations drops the price(s) of the popular fuel types, the competitor might want to consider droping their prices as well in order to maintain that gross revenue as high as possible.
