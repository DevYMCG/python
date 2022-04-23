def is_palindromo(String: str)->bool:
    String = String.replace(' ', '').lower()
    return String == String[::-1]

def run():
    print(is_palindromo(1000))


if __name__ == '__main__':
    run()