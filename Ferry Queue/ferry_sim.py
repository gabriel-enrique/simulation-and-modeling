import random
import numpy as np
import pandas as pd

def vehicle():
    num = random.randint(1, 100)

    if 1 <= num <= 40:
        return "Car"
    elif 41 <= num <= 95:
        return "Lorries"
    elif 96 <= num <= 100:
        return "Motorcycle"

def car():
    pass

def lorries():
    pass

def motorcycle():
    pass

def generate_queue(queue):
    return queue + [vehicle() for _ in range(10)]