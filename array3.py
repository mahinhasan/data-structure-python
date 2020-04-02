number = [155,62,46543,34,566]
#finding maximum number in an array 
#with time 0(N) running time Linear search
maximum = number[0]
for num in number:
    if(num>maximum):
        maximum=num
print(maximum)