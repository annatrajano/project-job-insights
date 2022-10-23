from src.sorting import sort_by

import pytest


@pytest.fixture
def jobs():
    return [
        {"title": "Dev Front-End", "min_salary": 3000, "max_salary": 6500,
            "date_posted": '2022-08-22'},
        {"title": "Dev Back-End", "min_salary": 3500, "max_salary": 7000,
            "date_posted": '2022-08-23'},
        {"title": "Dev FullStack", "min_salary": 4000, "max_salary": 8500,
            "date_posted": '2022-08-24'},
    ]


def test_sort_by_criteria(jobs):
    sort_by(jobs, "min_salary")
    assert jobs[0]["min_salary"] == 3000
    sort_by(jobs, "max_salary")
    assert jobs[0]["max_salary"] == 8500
    sort_by(jobs, "min_salary")
    assert jobs[0]["date_posted"] == '2022-08-22'
