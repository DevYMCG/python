def main():
    
    a = 1

    def nested():
        print(a)
    return nested
    
my_func = main()
print(my_func())


if __name__ == '__main__':
    main()