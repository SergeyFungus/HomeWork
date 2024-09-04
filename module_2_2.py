first = int(input())
second = int(input())
third = int(input())
count = 0
if first == second:
    count = count + 1
if first == third:
    count = count + 1
if second == third:
    count = count + 1
print(count)