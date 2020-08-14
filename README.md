# Outstandings Players Classifier

Este clasificacor se encarga de determinar, dadas determinadas estadísticas de jugadores de béisbol en un juego, si estos tuvieron un desempeño destacado en este encuentro.

El conjunto de datos de prueba para el entrenamiento del algoritmo de clasificación fue construido a partir de datos extraidos de las páginas baseball-reference.com y espndeportes.espn.com.

Por cada juego de béisbol, el sitio de baseball-reference.com nos brinda estadísticas de los jugadores implicados en dicho encuentro. Para el entrenamiento del algoritmo, se seleccionaron tres estadísticas genéricas tanto para lanzadores como para bateadores. Estas son la probabilidad de victoria añadida, el promedio de los índices de influencia y la expectativa de carreras. Estas son estadísticas que nos dan una medida de cuánto contribuyó cada jugador a la victoria de su equipo.

El sitio de ESPN nos brinda información acerca de cuáles fueron los jugadores más destacados en cada juego. Luego juntando esta información con las estadísticas extraidas de Baseball Reference, se conforma el conjunto de entrenamiento.

La idea principal del algoritmo de clasificación es poder determinar los jugadores destacados también atendiendo a la nacionalidad de los jugadores que se desean analizar. Esto no lo tiene en cuenta el sitio de ESPN, el cual determina, de forma manual, los jugadores destacados por cada juego independientemente de su nacionalidad.