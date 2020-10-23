import airflow
from airflow import AirflowException
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.providers.greatexpectations.operators.greatexpectations import GreatExpectationsOperator

default_args = {
    "owner": "Airflow",
    "start_date": airflow.utils.dates.days_ago(1)
}

dag = DAG(
    dag_id='ge_dag',
    default_args=default_args
)

ge_checkpoint_fail = GreatExpectationsOperator(
    task_id='ge_checkpoint_fail',
    run_id='ge_airflow_run',
    checkpoint_name='taxi.fail.chk',
    dag=dag
)

ge_checkpoint_pass = GreatExpectationsOperator(
    task_id='ge_checkpoint_pass',
    run_id='ge_airflow_run',
    checkpoint_name='taxi.pass.chk',
    dag=dag
)

ge_batch_kwargs_pass = GreatExpectationsOperator(
    task_id='ge_batch_kwargs_pass',
    expectation_suite_name='taxi.demo',
    batch_kwargs={
        'path': '/Users/sam/code/ge_demo/data/yellow_tripdata_sample_2019-01.csv',
        'datasource': 'data__dir'
    },
    dag=dag
)
