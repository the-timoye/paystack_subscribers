
from pyspark.sql import SparkSession
from pyspark.sql.functions import explode, col
from extraction import fetch_plans
from utilities.helpers import rename_columns
from utilities.constants import name_changes

spark_session = SparkSession.builder.appName('Random App Name').getOrCreate()

if __name__ == "__main__":
    try:
        plans = spark_session.createDataFrame(fetch_plans())
        plans = rename_columns(name_changes, plans)
        plans.printSchema()
        plans.show()
    except Exception as e:
        print(e)