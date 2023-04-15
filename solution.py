def count_sheep(n):
    count = ''
    for x in range(1, n + 1):
        count = count + "{} sheep...".format(x)
    return count

print(count_sheep(3))