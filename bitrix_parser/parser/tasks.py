from celery import shared_task
import time


@shared_task
def refresh(driver):
    # здесь код вашей задачи
    print('Task running...')
    driver.refresh()
    time.sleep(10)
    print('Task ended.')
