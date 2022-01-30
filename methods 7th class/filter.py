def is_even(x):
    if x%2==0:
        return True
    else:
        return False    


lst = [10,56,89,42,36,58,32,16, 23,25,63]

lst1 = list(filter(is_even, lst))

print(lst1)


if __name__ == "__main__":


# to be discussed
# decor function and special variable
