#!/usr/bin/python3
"""
module of python about requests API
"""


import requests


def todo_list_progress(employee_id):
    """Hacer una solicitud get a la API para obetener informacion del empleado"""
    response1 = requests.get("https://jsonplaceholder.typicode.com/users/{}".format(employee_id))
    
    """comprobar si la respuesta fue exitosa"""
    if (response1.status_code != 200):
        print("No se pudo obtener la iformacion del empleado")
        return
    """convertir la respuesta en json"""
    Employe = response1.json();

    """Hacer una solicitud get a la API para obtener las tareas del empleado"""
    response2 = requests.get("https://jsonplaceholder.typicode.com/users/{}/todos".format(employee_id))

    """Comprobar si la respuesta fue exitosa"""
    if (response2.status_code != 200):
        print("No se pudo obtener la iformacion de todos")
        return
    """convertir la respuesta en un formato json"""
    todos = response2.json();

    """Calcular el numero de tareas y de tareas completadas"""
    task = len(todos)
    completed_task = 0
    for todo in todos:
        if (todo['completed']):
            completed_task += 1
    Terminado = completed_task;
    """imprimer las tareas y las tareas completadas del empleado"""
    print("Employee {} is done with tasks({}/{}):".format(Employe['name'],Terminado, task));
    for todo in todos:
        if todo['completed'] == True:
            print('\t', todo['title'])

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        todo_list_progress(int(sys.argv[1]))
