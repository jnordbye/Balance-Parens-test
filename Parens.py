myStack = []
openParen = [ '(' , '[' , '{']

closeParen = [')' , ']' , '}']

test = input ( " Please enter a string to check")


for char in test:
    if char in openParen:
        myStack.append( char)
    elif char in closeParen:
        if len(myStack) == 0 or myStack[-1] != openParen[ closeParen.index(char)]:
            myStack.append(char)
            break
        else:
            myStack.pop()


if len(myStack) > 0:
    print( "Unbalanced " )
else:
    print( " Balanced ")
