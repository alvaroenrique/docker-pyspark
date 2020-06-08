from pyspark import SparkContext
from pyspark.sql import SQLContext

def filterNullData(x):
    if (x[0] == "EN INVESTIGACIÓN" or x[0] == "EN INVESTIGACIÓN"):
        return False
    return True


def main():
    sc = SparkContext("local", "Data")
    sqlContext = SQLContext(sc)
    rdd = sqlContext.read.csv("data.csv", header=True).rdd

    formated_data = rdd.map(lambda x: (x[1], x[2], 1)).filter(
        filterNullData).map(lambda x: (x[0], 1)).reduceByKey(lambda x, y: x + y)

    for data in formated_data.collect():
        print(f'{data[0]} {data[1]}')

    print("ññññññññ")


if __name__ == "__main__":
    main()
