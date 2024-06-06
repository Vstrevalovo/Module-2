first = int(input())
second = int(input())
third = int(input())
if third == second and second == first:
    print(3)
elif third == second or second == first or first == third:
    print (2)
else:
    print(0)