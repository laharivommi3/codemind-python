def sum_digits(str1):
    sum_digit=0
    for x in str1:
        if x.isdigit()==True:
            z=int(x)
            sum_digit=sum_digit+z
    return sum_digit
str1=input()
print(sum_digits(str1))