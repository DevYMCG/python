# [1, 1 , 2 , 2 , 4] -> [1, 2, 4]
def remove_duplicates(some_set):
    return list(set(some_set))

if __name__ == "__main__":

    random_set = [1, 1 , 2 , 2 , 4]
    print(remove_duplicates(random_set))