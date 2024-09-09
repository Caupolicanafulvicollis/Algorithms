def squares(n):
    if 1<=n<=20:
        i=0
        for i in range(n):
            print(i*i)
            i+1

if __name__ == '__main__':
    n = int(input())
    squares(n)
    assert squares(5) == '''
0
1
4
6
16'''
    assert squares(9) == '''
0
1
4
9
16
25
36
49
64
'''