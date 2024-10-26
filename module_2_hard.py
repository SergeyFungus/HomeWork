num = int(input())
answer = ""
for i in range(1,num+1):
    for j in range(i,num+1):
        if num % (i + j) == 0:
            answer = answer + str(i) + str(j)

print(answer)