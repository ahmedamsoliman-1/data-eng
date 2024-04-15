##import required libraries
import pyspark

##create spark session
spark = pyspark.sql.SparkSession \
   .builder \
   .appName("Python Spark SQL basic example") \
   .config('spark.driver.extraClassPath', "/Users/ahmed.soliman/workspace/ahmed/personal/data-eng/jar/postgresql-42.7.3.jar") \
   .getOrCreate()


print("=======")
print("=======")
print("=======")
print("=======")


movies_df = spark.read \
   .format("jdbc") \
   .option("url", "jdbc:postgresql://localhost:5432/postgres") \
   .option("dbtable", "movies") \
   .option("user", "postgres") \
   .option("password", "postgres") \
   .option("driver", "org.postgresql.Driver") \
   .load()

users_df = spark.read \
   .format("jdbc") \
   .option("url", "jdbc:postgresql://localhost:5432/postgres") \
   .option("dbtable", "users") \
   .option("user", "postgres") \
   .option("password", "postgres") \
   .option("driver", "org.postgresql.Driver") \
   .load()




print(movies_df.show())
print("=======")
print("=======")
print("=======")
print("=======")
print(users_df.show())



