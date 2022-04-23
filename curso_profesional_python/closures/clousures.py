def make_repeater_of(n):
    def repeater(string):
        assert type(string) == str, "solo puedes utilizar cadenas"
        return string * n
    return repeater

def run():
    repeat_5 = make_repeater_of(5)
    repeat_7 = make_repeater_of(7)

    print(repeat_5("hola"))
    print(repeat_7("Yoha"))

if __name__ == '__main__':
    run()