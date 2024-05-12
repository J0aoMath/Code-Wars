#Square(n) Sum
def square_sum(numbers):
    sum = 0
    for each in numbers:
        a = (each*each)
        sum+=a
    return(sum)
