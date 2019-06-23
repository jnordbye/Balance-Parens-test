
def ParenCheckList( inputStr ):
    rightParen = [ ')' , ']', '}']
    leftParen = ['(', '[', '{']
    parenList = []
    
    for char in inputStr:
        if char in leftParen:
            parenList.append(char)
        elif char in rightParen:
            if len(parenList) == 0 or parenList[-1] != leftParen[rightParen.index(char)]:
                return False
            else:
                parenList.pop()
    
    if len(parenList) == 0:
        return True
    else:
        return False

    
    
inputStr = input('Enter string to test:')

if ParenCheckList( inputStr ):
    print(" Parenthesis balanced")
else:
    print(' Parenthesis not balanced')
    
    
    
    
    
    
    
