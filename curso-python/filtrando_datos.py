from sqlite3 import DatabaseError


DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]

def run():

    """
        Consulta para traerme todos los
        trabajadores que dominan el 
        lenguaje de python.
    """
    # all_python_devs = [worker["name"] for worker in DATA if worker["language"]=="python"]

    # usando filter y maps

    # all_python_devs = list(filter(lambda worker: worker["language"] =="python", DATA))
    # all_python_devs = list(map(lambda worker: worker["name"], all_python_devs))

    # for worker in all_python_devs:
    #     print(worker)

    """
        Consulta para traerme todos los
        empleados que trabajen en 
        Platzi.
    """

    # all_platzi_devs = [worker["name"] for worker in DATA if worker["organization"]=="Platzi"]

    # usando filter y maps

    # all_platzi_devs = list(filter(lambda worker: worker["organization"] =="Platzi", DATA))
    # all_platzi_devs = list(map(lambda worker: worker["name"], all_platzi_devs))

    # for worker in all_platzi_devs:
    #     print(worker)

    """
        lista de los adultos que sean 
        mayores a 18 años.
    """

    # all_platzi_devs = [worker["name"] for worker in DATA if worker["age"]>18]

    # Otra forma
    # adults = list(filter(lambda worker: worker["age"] > 18, DATA))
    # adults = list(map(lambda worker: worker["name"], adults))

    # list comprehensions

    # adults = [worker["name"] for worker in DATA if worker["age"] > 18]

    # print(adults)

    """
        Traer los registros donde la persona
        sea mayor a 70 años 

        si es mayor True
        caso contrario False
    """
    # old_people = list(map(lambda worker: worker | {"old": worker["age"] > 70}, DATA))

    # for worker in old_people:
    #     print(worker)

    # list comprehensions

    old_people = [worker["name"] for worker in DATA if worker["age"] > 70]

    print(old_people)

if __name__ == '__main__':
    run()