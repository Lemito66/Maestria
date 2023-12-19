<h1>Proyecto de fin de Módulo</h1>

Explorar un conjunto de datos y crear modelos para efectuar regresión y/o clasificación de una variable respuesta sobre un conjunto de variables predictoras.

Documenten el proyecto y su análisis, comentarios y código fuente, en un notebook.

Me interesa leer la metodología y la línea de razonamiento que siguen durante el análisis de datos y de los modelos creados.  

Sugerencia: Tomen como referencias el código fuente usado en los laboratorios 3, 4, 5 (y 7 si desean incluir modelos aditivos generales).

Preguntas: ahernan@shinshu-u.ac.jp

Los pasos recomendados a seguir y los puntos más relevantes son los siguientes:

1) Seleccionar el conjunto de datos. 
El conjunto de datos puede ser uno de los que se incluyen en el libro de texto usado en el curso o uno de interés suyo.

2) Describir brevemente el conjunto de datos seleccionado con sus características (qué datos contiene).

3) Definir que clase de modelo desean explorar: regresión, clasificación o ambos

4) Explorar relaciones entre los datos, calculando correlaciones entre pares de variables y graficando las variables en pares.

Por ejemplo, suponiendo que el conjunto de datos se leyó en Python como un pandas Dataframe y se ha asignado a la variable denominada datos,

La correlación se puede calcular con
    datos.corr()

Los gráficos de pares de variables se pueden hacer usando la librería seaborne
    import seaborn as sns
    sns.pairplot(datos)
    plt.show()

5) Comentar sobre posibles relaciones entre variables de interés.

6) Determinar una variable de respuesta y los predictores candidatos iniciales.

7) Modelar la regresión y/o clasificación de manera incremental:

Preparar los datos X, y para el modelo particular, crear el modelo, ajustarlo y reportar los resultados del ajuste
Comentar si los coeficientes de los predictores obtenidos del ajuste contribuyen a la respuesta. Es decir, si estadísticamente son diferentes de cero. Para ello usen la información sobre los errores estándares de los coeficientes, la estadística t (o z) y los valores-p.
8) Con base en lo observado sobre los coeficientes y las posibles relaciones identificadas de la correlación de variables y los gráficos en pares, refinar el modelo. Es decir, repetir el paso anterior las veces que crean convenientes para hacer las modificaciones tendientes a mejorar el modelo. 

Por ejemplo,
Añadir o quitar predictores.
Incluir no linealidades (por ejemplo, usar polinomios)
Incluir interacciones entre predictores
9) Reporten tanto la estadística R^2 como los errores obtenidos tanto en el entrenamiento como en las pruebas.  Se recomienda usar validación cruzada.  Si no les es posible, usar al menos un conjunto de entrenamiento y un conjunto de prueba.

10) Decidan cuál es el mejor modelo con base en el error sobre los datos de prueba. Comenten sobre el R^2 de este modelo.

11) Traten de explicar el modelo.