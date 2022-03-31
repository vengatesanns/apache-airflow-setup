
from airflow.models import DAG
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator


from datetime import datetime

default_args = {
    'start_date': datetime(2022, 1, 1)
}

with DAG('irctc_railway_train_schedules', schedule_interval='@daily', 
        default_args=default_args, catchup=False) as dag:
    # Task 1 - Flattening the JSON to ORC file
    flattening_data_spark_submit_task = SparkSubmitOperator(
        task_id = 'flattening_data_spark_submit_task',
        conn_id='spark_submit_connection',
        java_class= 'com.hackprotech.railways.RailwaysDataFlatteningUsingDF',
        application="/home/vengat/big_data/projects/spark_jars/spark-realtime-projects-assembly-2.1.0.jar",
        
    )