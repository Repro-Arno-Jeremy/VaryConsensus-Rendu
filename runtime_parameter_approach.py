# Exploring combination of variability factors with runtime parameters (without CLI)

import random
import numpy as np
from decimal import Decimal, getcontext
import csv

def check_property(operation1, operation2, randomGenerator, repetitions, precision, decimal_use = True):
    if decimal_use:
        getcontext().prec = precision

    correct_count = repetitions
    for _ in range(repetitions):
        x = eval(randomGenerator)
        y = eval(randomGenerator)
        z = eval(randomGenerator)
        if decimal_use:
            x = Decimal(x)
            y = Decimal(y)
            z = Decimal(z)

        # Dynamically evaluate the operations
        result1 = eval(operation1)
        result2 = eval(operation2)

        if result1 != result2:
            correct_count -= 1

    print(f"Percentage of correct trials : {round(correct_count/repetitions*100, 3)}, number of repetitions :  {repetitions} trials")
    return round(correct_count/repetitions*100, 3)

# Define possible combinations of operations and repetition counts
operations = [
    {"operation1": "(x + y) + z", "operation2": "x + (y + z)"},  # Associativity
    {"operation1": "(x * y) * z", "operation2": "x * (y * z)"},  # Associativity (multiplication)
]

# Define different repetition counts
repetitions_list = [1000, 2000, 5000]

# Defining different precision levels for addition
# Over 55 the accuracy for addition is 100 %
addition_precision_list = [50, 53, 60]

# Defining different precision levels for multiplication
# Over 110 the accuracy for addition is 100 %
multiplication_precision_list = [105, 110]

# Seed the random number generator
randomGenerator = ["np.random.rand()", "random.random()"]

csv_filename = "/app/output/results.csv"

with open(csv_filename, "w") as csvfile:
    # Defining the fieldnames for the CSV file
    fieldnames = ['operation1', 'operation2', 'repetitions', 'random_generator', 'precision', 'decimal_use', 'percentage_correct']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    # Writing the header of the CSV file
    writer.writeheader()

    # Looping through all combinations of repetitions and generator for addition
    operation_1 = operations[0]['operation1']
    operation_2 = operations[0]['operation2']
    for reps in repetitions_list:
        for randGen in randomGenerator:
            for prec in addition_precision_list:
                print(f"\nChecking addition, repetitions : {reps} , float generating method : {randGen}, precision : {prec}")
                percentage = check_property(operation_1, operation_2, randGen, reps, prec)
                writer.writerow({
                    'operation1': operation_1,
                    'operation2': operation_2,
                    'repetitions': reps,
                    'random_generator': randGen,
                    'precision': prec,
                    'decimal_use': True,
                    'percentage_correct': percentage
                })

    # Looping through all combinations of repetitions and generator for multiplication
    operation_1 = operations[1]['operation1']
    operation_2 = operations[1]['operation2']
    for reps in repetitions_list:
        for randGen in randomGenerator:
            for prec in multiplication_precision_list:
                print(f"\nChecking multiplication, repetitions : {reps} , float generating method : {randGen}, precision : {prec}")
                percentage = check_property(operation_1, operation_2, randGen, reps, prec)
                writer.writerow({
                    'operation1': operation_1,
                    'operation2': operation_2,
                    'repetitions': reps,
                    'random_generator': randGen,
                       'precision': prec,
                    'decimal_use': True,
                    'percentage_correct': percentage
                })

    # Checking both operations without adding precision
    for op in operations:
        operation_1 = op['operation1']
        operation_2 = op['operation2']
        for reps in repetitions_list:
            for randGen in randomGenerator:
                print(f"\nChecking {operation_1}, repetitions : {reps} , float generating method : {randGen}, precision : False")
                percentage = check_property(operation_1, operation_2, randGen, reps, 50, False)
                writer.writerow({
                    'operation1': operation_1,
                    'operation2': operation_2,
                    'repetitions': reps,
                    'random_generator': randGen,
                    'precision': 0,
                    'decimal_use': False,
                    'percentage_correct': percentage
                })