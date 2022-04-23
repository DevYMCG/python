def make_division_by(n):
    def division(m):
        assert type(m) == int, "solo puedes utilizar números"
        return m / n
    return division

def run():
    division_by_3 = make_division_by(3)

    print(division_by_3(18))

if __name__ == '__main__':
    run()