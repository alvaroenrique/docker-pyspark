from pyspark import SparkContext
from pyspark.sql import SQLContext


def main():
    sc = SparkContext("local", "Analisis_Peliculas")
    sqlContext = SQLContext(sc)
    rddPeliculas = sqlContext.read.csv("movie_metadata.csv", header=True).rdd
    rddkv = rddPeliculas.map(lambda x: (x[1], (int(x[8]), 1) if x[8] != None and x[8] != "" else (
        0, 1)))  # -> [ ("direct1", (200, 1)), ("direct2", 300), ("direct1", 100) ]
    #arr = rddkv.take(4)
    # print(arr)
    rddReducido = rddkv.reduceByKey(lambda x, y: (x[0] + y[0],  x[1] + y[1]))
    arr = rddReducido.take(4)
    print(arr)
    #rddOrdenado = rddReducido.sortBy(lambda x : x[1], ascending=False)

    # arr = rddOrdenado.take(1) # Action que obtiene un listado local de 1 valor
    # print(arr)


if __name__ == "__main__":
    main()
