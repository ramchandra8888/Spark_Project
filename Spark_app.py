from pyspark.sql import SparkSession
from pyspark.sql.functions import round


spark = SparkSession.builder.appName("TIPS_Application").getOrCreate()

# a)
data = spark.read.csv("tips.csv", header=True, inferSchema=True)
data.show(10)

# b)
percentage_data = data.withColumn("Tip_Percentage", round((data.tip / data.total_bill) * 100, 2))
percentage_data.show()

# c)
percentage_data.createOrReplaceTempView("tips")

# d) 
total_average = spark.sql("SELECT day, AVG(total_bill) AS Average_total_bill FROM tips GROUP BY day")
total_average.show()

max_tip = spark.sql("SELECT gender, MAX(tip) AS Max_Tip FROM tips GROUP BY gender")
max_tip.show()

tip_percentage_gt_20 = spark.sql("SELECT * FROM tips WHERE Tip_Percentage > 20")
print("Rows with Tip_Percentage > 20:")
tip_percentage_gt_20.show()

# e)
output_path = "tips.parquet"
percentage_data.write.mode("overwrite").parquet(output_path)
print(f"Data written to {output_path}")

spark.stop()