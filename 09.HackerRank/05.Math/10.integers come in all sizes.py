def all_sizes(a,b,c,d):
    if 1<=a<=1000 and 1<=b<=1000 and 1<=c<=1000 and 1<=d<=1000:
        return a**b+c**d
    
if __name__ == "__main__":
    a=int(input())
    b=int(input())
    c=int(input())
    d=int(input())
    print(all_sizes(a,b,c,d))