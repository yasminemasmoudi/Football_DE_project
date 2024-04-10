import os 
import sys
from airflow import DAG
from datetime import datetime
from airflow.operators.python import PythonOperator
# This line of code adds a directory to the Python module search path.
sys.path.insert(0,os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from pipelines.wikipedia_pipeline import extract_wikipedia_data


dag = DAG(
    dag_id='wikipedia_flow',
    default_args={
        "owner": "Yasmine Masmoudi",
        "start_date": datetime(2024, 4, 1),
    },
    schedule_interval=None,
    catchup=False
)


#Extraction from WIKIPEDIA 
extract_data_from_wikipedia = PythonOperator(
    task_id = "extract_data_from_wikipedia",
    python_callable = extract_wikipedia_data,
    provide_context = True,
    op_kwargs = {
        "url" : "https://en.wikipedia.org/wiki/List_of_association_football_stadiums_by_capacity"
    },
    dag = dag
)
#Preprocessing
#Writing to Azure