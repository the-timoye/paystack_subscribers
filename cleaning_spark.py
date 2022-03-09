import json
from pyspark.sql import SparkSession
from pyspark.sql.functions import explode, col
from extractions.subscriptions import fetch_plans

spark_session = SparkSession.builder.appName('Random App').getOrCreate()

if __name__ == "__main__":
    plans = spark_session.createDataFrame(fetch_plans())
    # ss = spark_session.createDataFrame(plans['subscriptions'])
    plans.withColumn('sub_amount', col('subscriptions').getItem('amount')).withColumn('subscriber', col('subscriptions').getItem('customer')).withColumn('sub_createdAt', col('subscriptions').getItem('createdAt')).withColumn('sub_id', col('subscriptions').getItem('id')).withColumn(
        'sub_qty', col('subscriptions').getItem('quantity')).withColumn('sub_code', col('subscriptions').getItem('subscription_code')).withColumn('sub_status', col('subscriptions').getItem('status')).withColumn('sub_start_date', col('subscriptions').getItem('start')).show()
