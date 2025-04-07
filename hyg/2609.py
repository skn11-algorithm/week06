def gcd(x,y):
    if x<y:
        temp = y
        y = x
        x = temp
    
    if y==0:
        return x
    else:
        return gcd(y, x%y)

def lcm(x,y,num): 
    return (int((x/num) * num * (y/num)))

a,b = map(int,input().split())

num1 = gcd(a,b)
num2 = lcm(a,b,num1)

print(num1)
print(num2)
