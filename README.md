```avega: Para arrancar la aplicación y poder usar postman (carpeta ./docs) directamente ejecutar :```

```docker build -t club . && docker run -it --rm -p8000:8000 club```

```Al tratarse de un examen y no de una aplicación productiva se ha primado la facilidad de corrección y por ello se incluye preconfigurada una base de datos sqlite al proyecto con credenciales por defecto usuario:password -> operator:alphabeta12```


OBJETIVO.
Realizar una mini-aplicación con la tecnología que prefieras API Rest que gestione clubes, jugadores y entrenadores.

DESCRIPCIÓN.
Sobre estos modelos (clubes, jugadores y entrenadores) se deberán de poder realizar las siguientes operaciones:
CLUBES
— Dar de alta un club.
— Dar de alta un jugador en el club.
— Dar de alta un entrenador en el club.
— Modificar el presupuesto de un club.
— Dar de baja un jugador del club.
— Dar de baja un entrenador del club.
— Listar jugadores de un club con posibilidad de filtrar por una de las propiedades
(por ejemplo nombre) y con paginación.

```avega: Completado, se puede filtrar por el campo "friendly_name" añadiendo como parámetro de query "?friendly_name__contains=vor" a cualquier endpoint```

JUGADORES
— Dar de alta un jugador sin pertenecer a un club.

```avega: Completado```

ENTRENADORES
— Dar de alta un entrenador sin pertenecer a un club.
Cada club deberá de tener un presupuesto, este presupuesto se asignará en el alta del club.

```avega: Completado```


Prueba técnica backend julio 2023
Al dar de alta un jugador/entrenador a un club se deberá especificar el salario del jugador/entrenador para ese club, ese salario debe de salir del presupuesto del club y el presupuesto nunca puede ser menor que cero.

```avega: Completado, si al actualizar o crear un jugador o entrenador la propiedad "club" está a null pesé a indicar un club, significará que no es posible asignar esa entidad al club por salario. Se ha hecho así por brevedad del examen debiendo utilizar los códigos de estado y un mensaje en el respuesta json adecuados en una aplicación productiva.```

Al modificar el presupuesto de un club se tiene que tener en cuenta los salarios actuales de ese club.

```avega: No se especifica en el examen el comportamiento en el caso de disminuir el presupuesto por debajo de la masa salaria actual. El modelo del "club" dispone de un método "committed_budget" que devuelve la masa salarial actual, es trivial entonces determinar qué acción realizar disponiendo de ese dato.```

Un jugador/entrenador no podrá estar dado de alta en más de un club.

```avega: Por diseño no es posible asignar jugadores o entrenadores a más de un club```

Cada vez que se de alta o baja a un jugador/entrenador tendrá que ser notificado
por email(en un futuro se está pensando en pueda ser notificado por otras vías
(sms, whatsapp...) por lo tanto lo tendremos que dejar abierta esta posibilidad sin
ser implementada actualmente).

```avega: Se han utilizado señales de django para desacoplar la futura lógica del los modelos. Ver archivo ./infra/club/signals.py```

REQUERIMIENTOS
— Instrucciones de instalación (añadirlas al README.md).
```Completado```

— Symfony 4.4 o superior.
```No aplica```

— Se deberá utilizar Doctrine como ORM.
```No aplica```

— Se pueden utilizar bundles de terceros (excepto API Platform).
```Se ha utilizado django rest framework, aunque para aplicaciones que no utilicen django personalmente prefiero utilizar FastAPi```

— El tipo de contenido siempre debe ser application/json.
```Completado```

— Entregar un dump de la DB con datos de prueba.
```Se incluye por defecto la base de datos sqlite en ./infra/db.sqlite3```

— Se valorará muy positivamente una colección de Postman.
```Includa en el directorio /docs```

— Se valorará muy positivamente el uso de docker.
```Implementado```

— Se valorará muy positivamente la estructura y limpieza del código, tests unitarios, el uso de “Patrones de diseño”, el uso de los verbos REST y las buenas prácticas de Symfony.
```Se han aplicado las convenciones de django al proyecto, usado los verbos REST adecuados, y se ha utilizado herencia en la definición de los modelos con la finalidad de simplicarlos y evitar duplicación de código. El enunciado no permite realizar tests unitarios técnicamente hablando aunque podrían realizarse tests de integración realizando un mock de la base de datos para el algoritmo de cálculo de la masa salarial.```

