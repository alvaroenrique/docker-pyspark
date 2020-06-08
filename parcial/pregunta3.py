from pyspark import SparkContext
from pyspark.sql import SQLContext


def filterNone(x):
    if (x[5] == None):
        return False
    return True


def formatDate(d):
    intDate = int(d)
    if(intDate < 18):
        return "Menores de 18"
    if(intDate >= 18 and intDate <= 30):
        return "Entre 18 y 30"
    if(intDate >= 31 and intDate <= 40):
        return "Entre 31 y 40"
    if(intDate >= 41 and intDate <= 50):
        return "Entre 41 y 50"
    if(intDate >= 51 and intDate <= 60):
        return "Entre 51 y 60"
    if(intDate >= 61 and intDate <= 70):
        return "Entre 61 y 70"
    if(intDate > 70):
        return "Más de 70"
    return d


def main():
    sc = SparkContext("local", "Data")
    sqlContext = SQLContext(sc)
    rdd = sqlContext.read.csv("data.csv", header=True).rdd

    formated_data = rdd.filter(filterNone).map(lambda x: (formatDate(x[5]), 1)).reduceByKey(
        lambda x, y: x + y).sortBy(lambda x: x[1], ascending=False)

    for data in formated_data.collect():
        print(f'{data[0]} {data[1]}')


if __name__ == "__main__":
    main()
