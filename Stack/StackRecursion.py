# Python program to reverse a 
# stack using recursion

# Recursive funtion that
# inserts an element
# at the bottom of a stack.
def insertAtBottom(stack, item):
    if isEmpty(stack):
        push(stack, item)
    else:
        value = pop(stack)
        insertAtBottom(stack, item)
        push(stack, value)

# Below is the function that
# reverses the given stack
# using insertAtBottom()
def reverse(stack):
    if not isEmpty(stack):
        value = pop(stack)
        reverse(stack)
        insertAtBottom(stack, value)

# Function to create a stack.
# It initializes size of a stack as 0
def createStack():
    stack = []
    return stack

# Function to check if
# the stack is empty
def isEmpty(stack):
    return len(stack) == 0

# Function to push an
# item to stack
def push(stack, item):
    stack.append(item)

# Function to pop an 
# item from stack
def pop(stack):
    # if stack is empty
    # then error
    if(isEmpty(stack)):
        print("Stack Underflow!")
        exit(1)
    
    return stack.pop()

# Function to print the stack
def prints(stack):
    for i in range(len(stack) - 1, -1, -1):
        print(stack[i], end = ' ')

stack = createStack()
push( stack, str(4) )
push( stack, str(3) )
push( stack, str(2) )
push( stack, str(1) )
print("Original Stack ")
prints(stack)
  
reverse(stack)
  
print("Reversed Stack \n")
prints(stack)