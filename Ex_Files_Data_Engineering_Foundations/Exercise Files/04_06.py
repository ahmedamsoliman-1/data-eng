##import required libraries
import pyspark.sql


##create spark session
spark = pyspark.sql.SparkSession \
    .builder \
    .appName("Python Spark SQL basic example") \
    .config('spark.driver.extraClassPath', "/Users/ahmed.soliman/workspace/ahmed/personal/data-eng/jar/postgresql-42.7.3.jar") \
    .getOrCreate()

##read movies table from db using spark
movies_df = spark.read \
    .format("jdbc") \
    .option("url", "jdbc:postgresql://localhost:5432/etl_pipeline") \
    .option("dbtable", "movies") \
    .option("user", "<username>") \
    .option("password", "<password>") \
    .option("driver", "org.postgresql.Driver") \
    .load()

##read users table from db using spark
users_df = spark.read \
    .format("jdbc") \
    .option("url", "jdbc:postgresql://localhost:5432/etl_pipeline") \
    .option("dbtable", "users") \
    .option("user", "<username>") \
    .option("password", "<password>") \
    .option("driver", "org.postgresql.Driver") \
    .load()


# Use groupBy and mean to aggregate the column
avg_rating = users_df.____('____').____('____')

# Join the tables using the film_id column
df = movies_df.join(
    avg_rating,
    movies_df.___==avg_rating____
)


##print the final dataframe
print(_____)





