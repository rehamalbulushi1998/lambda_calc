import json
from adder import add
from divider import divide
from multiplyer import multiply
from subtractor import subtract
print('Loading the calculator function')


def lambda_handler(event, context):
    print("Received event: " + json.dumps(event, indent=2))
    x = event['x']
    y = event['y']
    op = event['op']
    if op == "add":
        print("the sum of {x} and {y} is {add(x,y)}") 

    elif op == "divide":
        print("the sum of {x} and {y} is {divide(x,y)}") 

    elif op == "multiply":
        print("the sum of {x} and {y} is {multiply(x,y)}")

    else op == "subtract":
        print("the sum of {x} and {y} is {subtract(x,y)}")   

