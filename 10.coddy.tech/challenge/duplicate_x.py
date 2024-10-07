def duplicate_until_x(string):
    # Write code here 
    letters=list(string)
    for i in range(string):
        if string[i]=="x":
            letters.append(string[i])
        else:
            break