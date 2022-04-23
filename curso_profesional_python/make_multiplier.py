def make_multipler(x):

    def multipler(n):
        return x * n
    return multipler

times10 = make_multipler(10)
times4 = make_multipler(4)

print(times10(3)) # 10*3 = 30
print(times4(5)) # 4*5 = 20
print(times10(times4(2))) # 10(4*2)=8*10 = 80

