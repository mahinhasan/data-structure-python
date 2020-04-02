"""Stack is LIFO - Last in fast out

Author ->Mehedi Hasan Mahin
        Aiub
        cse 
"""

stack = [1,2,3,4,5]
print("Befor appen(): "+str(stack))
stack.append(6)
print("After append(): "+str(stack))
stack.pop()
print("After pop(): "+str(stack))
stack.pop()
print("After pop(): "+str(stack))