import random as rnd
nombres = ['alba', 'alberto', 'alejandro', 'alicia', 'álvaro', 'ana', 'andrés', 'antonio', 'carla', 'carlos', 'carmen', 'cristina', 'daniel', 'david', 'eduardo', 'enrique', 'esther', 'eva', 'felipe', 'gabriel', 'hector', 'helena', 'hugo', 'isabel',
           'iván', 'javier', 'jesus', 'jorge', 'juan', 'laura', 'lucas', 'lucía', 'luis', 'manuel', 'mar', 'margarita', 'maría', 'marta', 'martina', 'miguel', 'patricia', 'paula', 'pilar', 'raquel', 'raúl', 'rocío', 'samuel', 'sara', 'sonia', 'teresa']
apellidos = ['alonso', 'álvarez', 'blanco', 'cano', 'castillo', 'castro', 'cortes', 'delgado', 'diaz', 'dominguez', 'fernandez', 'garcía', 'garrido', 'gil', 'gomez', 'gonzalez', 'guerrero', 'gutierrez', 'hernandez', 'iglesias', 'jimenez', 'lopez', 'lozano', 'marin',
             'martin', 'martinez', 'medina', 'mendez', 'molina', 'morales', 'moreno', 'muñoz', 'navarro', 'nuñez', 'ortega', 'ortiz', 'perez', 'ramirez', 'ramos', 'rodriguez', 'romero', 'rubio', 'ruiz', 'sanchez', 'santos', 'sanz', 'serrano', 'suarez', 'torres', 'vazquez']


def capitalize():
    nombre, apellido = rnd.choice(nombres).capitalize(), rnd.choice(apellidos).capitalize()
    return nombre, apellido


print(*capitalize())
