# kwargs
def sum(**kwargs):
    sum = 0
    for key, value in kwargs.items():
        sum += value
    
    return round(sum, 2)

print(sum(coffee=2.99, cake=4.55, tea=2.99))
