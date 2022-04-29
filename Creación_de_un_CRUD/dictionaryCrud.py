clients = [
    {
        'name': 'pablo',
        'company': 'Google',
        'email': 'pablo@google.com',
        'position': 'Software engineer'
    },
    {
        'name': 'Ricardo',
        'company': 'Facebook',
        'email': 'Ricardo@facebook.com',
        'position': 'Data engineer'
    }
]

def create_client(client):
    global clients

    if client not in clients:
        clients.append(client)
    else:
        print('Client already is in the client\'s list')

def list_clients():
    for idx, client in enumerate(clients):
        print('{uid} | {name} | {company} | {email} | {position}'.format(
            uid = idx, 
            name = client['name'],
            company = client['company'],
            email = client['email'],
            position = client['position']))


def update_client(index, client):
    if len(clients)-1 >= client_id:
        clients[index] = client
    else:
        print('Client is not in clients list')

def delete_client(index):
    if len(clients)-1 >= client_id:
        clients.pop(index)
    else:
        print('Client is not in client list')

def search_client(client_name):

    for client in clients:
        if client['name'] != client_name:
            continue
        else:
            return True

def _print_welcome():
    print('WELCOME TO PLATZI VENTAS')
    print('*' * 50)
    print('What would you like to do today?')
    print('[C]reate client')
    print('[U]pdate client')
    print('[D]elete client')
    print('[S]earch client')

def _get_client_field(field_name):
    field = None

    while not field:
        field = input('What is the client {}?'.format(field_name))
    
    return field

def _get_client_from_user():
    client = {
        'name': _get_client_field('name'),
        'company': _get_client_field('company'),
        'email': _get_client_field('email'),
        'position': _get_client_field('position'),
    }

    return client
    
if __name__ == '__main__':
    _print_welcome()

    command = input()
    command = command.upper()

    if command == 'C':
        client = _get_client_from_user()
        create_client(client)
        list_clients()
    elif command == 'D':
        client_id = int(_get_client_field('id'))
        delete_client(client_id)
        list_clients()
    elif command == 'U':
        client_id = int(_get_client_field('id'))
        client = _get_client_from_user()
        update_client(client_id, client)
        list_clients()
    elif command == 'S':
        client_name = _get_client_field('name')
        found = search_client(client_name)

        if found:
            print('The client is in the client\'s list')
        else:
            print('The client: {} is not in our client\'s list'.format(client_name))
    else:
        print('Invalid command')