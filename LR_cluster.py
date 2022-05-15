from pyspark.sql import SparkSession
import json
from pyspark.ml.regression import LinearRegression
from pyspark.ml.feature import VectorAssembler
from pyspark.sql.functions import *
import sys

spark = SparkSession.builder.getOrCreate()
sc = spark.sparkContext

def get_data(line):
    data = json.loads(line)
    data["_id"] = data["_id"]["$oid"]
#    data['unplug_hourTime'] = datetime.strptime(data['unplug_hourTime']['$date'], "%Y-%m-%dT%H:%M:%S.%f%z")
    return data

dirs = []
with open(sys.argv[1]) as f:
    lines = f.readlines()
    for line in lines:
        dirs.append(line[:-1])

print("INICIO")

dfs = []
for i,a in enumerate(dirs):
    rdd = sc.textFile(a).map(get_data)
    df = spark.createDataFrame(rdd)
    dfs.append(df)
    print(f"leido {i+1}",a)

for i in range(len(dfs)):
    print(f"Length {i+1}:",dfs[i].count())

df = dfs[0]
for i in range(len(dfs)-1):
    df = df.unionAll(dfs[i+1])

print("Merged df length:",df.count())

df = df.drop('_id','user_day_code','zip_code','idplug_base','idunplug_base')
print("Df columns:",df.columns)

df = df.withColumn('year',year(df['unplug_hourTime']))
df = df.withColumn('month',month(df['unplug_hourTime']))
df = df.withColumn('day',dayofmonth(df['unplug_hourTime']))
df = df.withColumn('hour',hour(df['unplug_hourTime']))
df = df.drop('unplug_hourTime')

df = df.withColumn('agrng_0',when(df['ageRange'] == 0, 1).otherwise(0))
df = df.withColumn('agrng_1',when(df['ageRange'] == 1, 1).otherwise(0))
df = df.withColumn('agrng_2',when(df['ageRange'] == 2, 1).otherwise(0))
df = df.withColumn('agrng_3',when(df['ageRange'] == 3, 1).otherwise(0))
df = df.withColumn('agrng_4',when(df['ageRange'] == 4, 1).otherwise(0))
df = df.withColumn('agrng_5',when(df['ageRange'] == 5, 1).otherwise(0))
df = df.withColumn('agrng_6',when(df['ageRange'] == 6, 1).otherwise(0))
df = df.drop('ageRange')

print("Df columns:",df.columns)

print("\nCorrelaciones entre las variables predictoras y la variable a predecir:")
for i in df.columns:
    print("corr entre ",i," y travel_time: ",df.stat.corr('travel_time',i))


columnJoin = VectorAssembler(inputCols = ['year','month','day','hour','agrng_0','agrng_1','agrng_2','agrng_3','agrng_4','agrng_5','agrng_6'],outputCol = 'features')
t_df = columnJoin.transform(df)
t_df = t_df.select(['features','travel_time'])
splits = t_df.randomSplit([0.7, 0.3])
train_df = splits[0]
test_df = splits[1]
lr = LinearRegression(featuresCol = 'features', labelCol='travel_time')
lr_model = lr.fit(train_df)
print("Coefficients: " + str(lr_model.coefficients))
print("Intercept: " + str(lr_model.intercept))
summ = lr_model.summary
print("RMSE",summ.rootMeanSquaredError)
print("r2",summ.r2)

print("\nFIN")