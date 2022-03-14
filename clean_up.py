
from pyspark.sql import SparkSession
from extractions.subscriptions import fetch_plans
from utilities.helpers import rename_columns
from utilities.constants import name_changes

spark_session = SparkSession.builder.appName('Random App Name').getOrCreate()


def clean_data():
    try:
        plans = spark_session.createDataFrame(fetch_plans())
        plans = rename_columns(name_changes, plans)
        plans.printSchema()
        plans.show()
    except Exception as e:
        print(e)


if __name__ == "__main__":
    clean_data()
