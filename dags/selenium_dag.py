from airflow.models import DAG
from airflow.operators.selenium_plugin import SeleniumOperator
from airflow.operators.dummy_operator import DummyOperator
from selenium_scripts import strava_commands
from datetime import datetime, timedelta

default_args = {
    'owner': 'harry_daniels',
    'wait_for_downstream': True,
    'start_date': datetime(2019, 7, 3),
    'end_date': datetime(2019, 7, 4),
    'retries': 3,
    'retries_delay': timedelta(minutes=5)
    }

dag = DAG('imap_example_dag',
          schedule_interval='@daily',
          default_args=default_args)

start = DummyOperator(
    task_id='start',
    dag=dag)

get_tdf_gpx = SeleniumOperator(
    script='',
    script_args='',
    task_id='get_tdf_gpx',
    dag=dag
)

end = DummyOperator(
    task_id='end',
    dag=dag)