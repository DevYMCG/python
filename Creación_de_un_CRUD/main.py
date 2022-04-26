clients = 'Pablo,Ricardo,'

def create_client(client_name):
    """definimos la variable global para poder usar la variable"""
    global clients

    clients += client_name
    _add_coma()


def list_client():
    global clients

    print(clients)

def _add_coma():
    global clients

    clients += ', '


if __name__ == '__main__':
    list_client()
    create_client('David')
    list_client()
    