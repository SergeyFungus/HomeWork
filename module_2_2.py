first = int(input())
second = int(input())
third = int(input())
if first == second and first == third and second == third:
    count = 3
elif first == third or first == third or second == third :
    count = 2
else:
    count = 0
print(count)