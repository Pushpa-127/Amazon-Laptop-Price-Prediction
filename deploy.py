from prefect.deployments import Deployment
from flows.train_model_flow import ml_training_flow
from prefect.server.schemas.schedules import CronSchedule

deployment = Deployment.build_from_flow(
    flow=ml_training_flow,
    name="daily-laptop-price-training",
    schedule=CronSchedule(cron="0 18 * * *", timezone="Asia/Kolkata"),  # every day 6:00 PM
    work_queue_name="default"
)

deployment.apply()
