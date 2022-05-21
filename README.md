Práctica Spark
Los objetivos principales han sido dos, el primero, la realización de análisis descriptivo y estadistico para la base de datos junto con la implementación de un modelo estadistico para predecir el tiempo de viaje. Por otro lado, se ha aplicado machine learning con el modelo de clasificación RandomForest para predecir el grupo de edad del usuario según el uso que haga. Para ello hemos utilizado la librería spark de Python, y para la ejecución en archivos grandes hemos empleado el cluster al que tenemos acceso en esta asignatura. En el notebook de Python LinearRegression.ipynb contamos más detalladamente los procesos que hemos seguido para realizar un primer análisis de los datos, filtrar las variables y la información que nos interesa y por último la realización de una regresión lineal, posteriormente, se realiza otra aproximación a través del machine learning con RandomForest model for binary or multiclass classification.

Ejecución de los programas
Los programas principales de la práctica son:
    • LinearRegression.ipynb
Este jupyter-notebook de Python contiene el proceso de análisis de datos, pero por comodidad y gestión de tiempo solo se ejecuta con tres archivos de prueba. Sería necesario tener estos tres archivos (sample_10e2.json, sample_10e3.json y sample_10e4.json) en la misma ubicación que el notebook.
    • Random Forest
Este jupyter-notebook de Python contiene el proceso de análisis de datos, pero por comodidad y gestión de tiempo solo se ejecuta con tres archivos de prueba. Sería necesario tener estos tres archivos (sample_10e2.json, sample_10e3.json y sample_10e4.json) en la misma ubicación que el notebook.
    • LR_cluster.py
Este archivo de Python es el verdadero programa de la práctica, ya que replica el análisis hecho en el jupyter-notebook, pero esta vez no se limita a los archivos de prueba. Al ejecutar este archivo se ha de utilizar como argumento de entrada un archivo .txt que contenga las direcciones de las bases de datos que utilizaremos para el análisis de datos. En nuestro caso empleamos el archivo bases_de_datos.txt, que esta preparado para ejecutarse en el cluster, donde emplear grandes cantidades de datos es más rápido.

Las imágenes que hay en el repositorio, que estan guardadas en la carpeta 'Archivos', son capturas de pantalla de la ejecución de este archivo .py con bases_de_datos.txt como argumento de entrada.

Datos empleados
Los datos empleados en esta práctica los hemos obtenido de la página web de BiciMat en el enlace: https://opendata.emtmadrid.es/Datos-estaticos/Datos-generales-(1) . Para nuestro análisis hemos empleado los datos desde Enero de 2020 hasta Junio de 2021. Estos archivos los hemos subido a hadoop, y sus direcciones estan guardadas en bases_de_datos.txt (pues leemos este archivo en la ejecución del programa).
Los archivos empleados son:
/user/psaurina/202001_movements.json
/user/psaurina/202002_movements.json
/user/psaurina/202003_movements.json
/user/psaurina/202004_movements.json
/user/psaurina/202005_movements.json
/user/psaurina/202006_movements.json
/user/psaurina/202007_movements.json
/user/psaurina/202008_movements.json
/user/psaurina/202009_movements.json
/user/psaurina/202010_movements.json
/user/psaurina/202011_movements.json
/user/psaurina/202012_movements.json
/user/psaurina/202101_movements.json
/user/psaurina/202102_movements.json
/user/psaurina/202103_movements.json
/user/psaurina/202104_movements.json
/user/psaurina/202105_movements.json
/user/psaurina/202106_movements.json

Resultados y Conclusiones
El análisis llevado a cabo no nos ha proporcionado resultados positivos acerca de la relación entre la variable a predecir y las predictoras, el modelo lineal que hemos diseñado no predice de forma correcta el tiempo de viaje.
La conclusión a la que llegamos es principalmente al hecho de que los grupos de edad, la fecha de inicio del viaje y la hora de inicio del viaje no estan bien correlacionadas con la duración del viaje. Es decir que si quisiéramos predecir la duración de un viaje deberíamos recabar datos distintos para que esta predicción fuera más precisa, sin embargo, a la hora de predecir la variable de edad con las demás si resulta mucho más sencillo ya que hay una cantidad menor de grupos, luego se puede aplicar Machine Learning con RandomForest que realiza una predicción con 73% de acierto en el conjunto test, resultando una cuota de acierto alto y por lo tanto demostrando un método efectivo# PracticaSpark
