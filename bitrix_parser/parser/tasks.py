from bitrix_parser.celery import app

from .service import my_func
from .parser import main


@app.task
def my_func_run(people_login: str, people_password: str, interval_start: int, interval_end: int, stop_words: list):
    main(people_login, people_password, interval_start, interval_end, stop_words)
