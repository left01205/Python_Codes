"""
    Calculates the expected value given a list of probabilities and corresponding values.
    Parameters:
    prob (list): A list of probabilities.
    values (list): A list of corresponding values.
    Returns:
    float: The expected value.
    Raises:
    ValueError: If the number of probabilities and values are not the same.
"""
def calculate_exp_val(prob, values):
    if len(prob) != len(values):
        raise ValueError("The number of prob and values should be the same.")
    
    exp_val = 0
    for i in range(len(prob)):
        exp_val += prob[i] * values[i]
    
    return exp_val
# Example usage
'''
prob = [0.166,0.166,0.166,0.166,0.166,0.166]
values = [1,2,3,4,5,6]
'''
prob = eval(input("Enter the probabilities in list format : "))
values = eval(input("Enter the values in list format : "))
exp_val = calculate_exp_val(prob, values)
print("Expected Value:", exp_val)
