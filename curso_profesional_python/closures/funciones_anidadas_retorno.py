def main():
    
    a = 1

    def nested():
        print(a)
    return nested
    
my_func = main()
my_func()
