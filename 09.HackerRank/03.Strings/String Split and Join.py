def split_and_join(a):
    # write your code here
    line=a.split(' ')
    line='-'.join(line)
    return line

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)