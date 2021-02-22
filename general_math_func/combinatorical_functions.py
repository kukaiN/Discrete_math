import fractions
import math
import numpy as np

def multinomial(list_of_elements):
    current_product = 1
    num_factorial = sum(list_of_elements)
    for elem in list_of_elements:
        for i in range(1, elem+1):
            current_product *= fractions.Fraction(num_factorial, i)
            num_factorial-=1
    return current_product

def choose(n,k):
    current_product = 1
    for frac in [fractions.Fraction(n-i, i+1) for i in range(k)]:
        current_product*=frac
    return int(current_product)

def binomial_coeffiecent(n, return_type="int", str_len = 10):
    if return_type == "int":
        return [choose(n,k) for k in range(n+1)]
    elif return_type == "str":
        return [str(choose(n,k)).rjust(str_len) for k in range(n+1)]
    print("not a valid return type")
    return 0

def factorial(n):
    # use math.factorial if you can because thats implimented in C and it's faster
    curr_product = 1
    for i in range(1, n+1):
        curr_product*=i
    return curr_product

def derangement(n):
    # make sure that the n elements are unique
    # the mathematical notation is !n
    if n < 1:
        print(n, "is not a valid parameter for checking derangement")
        return 0
    if n > 30:
        return int(math.factorial(n)/math.e + 0.5)
    else:
        return int(math.factorial(n) * e_pow_x(n))


def e_pow_x(nth_term):
    val_list = np.zeros(nth_term+1)
    for i in range(nth_term+1):
        temp = -1 if i&1 else 1
        val_list[i] = temp/math.factorial(i)
    return sum(val_list)

def power(n, a):
    # dont use this for non-integers
    if a == 0: return 1
    return_val = 1
    while a:
        if a&1:
            return_val *= n
            a-=1
        elif ~(a&1):
            n = n*n
            a = int(a/2)
    return return_val

def stirling_formula(n):
    # returns a good aproximation of n factorial
    running_product, n_over_e = 1, n/math.e
    for _ in range(n):
        running_product*= n_over_e
    return int( (math.sqrt(2*math.pi*n)*running_product) + 0.5)

def main():

    prob = 0
    # this is for 10 days
    trials = 320
    total_char = 500
    total_mmvalue = 88901
    default_keys = 0
    destination_key = 6
    ave_val = total_mmvalue/total_char
    char_val = 1394
    roll_frequency = 4

    mudae_play_time = 360
    ave_showup = mudae_play_time/roll_frequency

    char_ranking_multi = char_val / ave_val
    for i in range(6, trials-default_keys):
        prob += choose(500, i) * ((1/total_char)**i) * (((total_char-1)/total_char)**(trials-i))

    print(prob)
    char_val += (6*(char_val * (0.1)))
    print(char_val, char_ranking_multi)

    additive_value = (char_val * (0.1))
    value = char_val
    for i in range(int(ave_showup)):

        value += char_val* prob
        char_val *= 1.1
        #char_val+=additive_value

    print(value)
    #print(multinomial([1, 1, 1]))
    #for i in [n*n for n in range(10)]:
    #    #print(i, choose(i, 5))


if __name__ == "__main__":
    main()