numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for i in numbers:
    for k in numbers:
        if i != 1:
            if k < i:
                if k != 1 and k != i:
                    if i % k == 0:
                        not_primes.append(i) #4, 6, 8, 9
                        break
                elif k == 1:
                    continue
            elif k == i:
                primes.append(i)



print(primes)
print(not_primes)