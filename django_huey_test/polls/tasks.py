import time
import math

# from huey.contrib.djhuey import db_task, task
from django_huey import task, db_task

from .models import Beans, Counter, NotBeanCounts


@db_task(queue='process')
def save_bean_counts(num):
    bean = Beans(count=num)
    math.factorial(1000000 + num)
    bean.save()
    return num

@db_task(queue='process')
def wasteful_count_beans(counter_id: int, num: int):
    c = Counter.objects.get(pk=counter_id)

    not_bean_count = math.factorial(100000 + num)

    nb = NotBeanCounts(num=str(not_bean_count))
    nb.save()

    return not_bean_count


@db_task(queue='process')
def count_beans(counter_id: int, num: int):
    c = Counter.objects.get(pk=counter_id)

    print(f'-- starting to count {num} beans --')

    result = wasteful_count_beans(counter_id, num)
    not_bean_count = result.get(blocking=True)

    c.succeeded = True
    c.save()

    print(f'-- finished counting {num} beans --')

    return not_bean_count


def count(nums: list[int]):
    c = Counter()
    c.save()

    for num in nums:
        count_beans(c.id, num)
    # count_beans.map(counter_id=c.id)


@task()
def basic_bean_counter(num):
    print(f'-- counted {num} basic beans --')


@db_task()
def count_beans_db(num):
    print(f'-- counted {num} db beans --')
