#######################################################
#                                                     #
#                 Calculator Program                  #
#                                                     #
#######################################################

def add(a, b):
    if isinstance(a, (int, float)):
        if isinstance(b, (int, float)):
            return a + b

    print("ERROR: Please input a number!")

def subtract(a, b):
    if isinstance(a, (int, float)):
            if isinstance(b, (int, float)):
                return a - b

    print("ERROR: Please input a number!")

def divide(a, b):
    if isinstance(a, (int, float)):
            if isinstance(b, (int, float)):
                return a / b

    print("ERROR: Please input a number!")
