from src.jobs import read


def get_unique_job_types(path):
    all_jobs = read(path)
    jobs_type = [job["job_type"] for job in all_jobs]
    return list(set(jobs_type))


def filter_by_job_type(jobs, job_type):
    job_type_list = []
    for job in jobs:
        if job['job_type'] == job_type:
            job_type_list.append(job)
    return job_type_list


def get_unique_industries(path):
    all_jobs = read(path)
    jobs_industries = [job["industry"] for job in all_jobs]
    return list(filter(None, set(jobs_industries)))


def filter_by_industry(jobs, industry):
    job_industries_list = []
    for job in jobs:
        if job['industry'] == industry:
            job_industries_list.append(job)
    return job_industries_list


def get_max_salary(path):
    all_jobs = read(path)
    salaries = set() 
    for job in all_jobs:
        if job['max_salary'].isnumeric():
            salaries.add(int(job['max_salary']))
    return max(salaries)


def get_min_salary(path):
    all_jobs = read(path)
    salaries = set() 
    for job in all_jobs:
        if job['min_salary'].isnumeric():
            salaries.add(int(job['min_salary']))
    return min(salaries)


def matches_salary_range(job, salary):
    if ("min_salary" or "max_salary") not in job:
        raise ValueError('min_salary or max_salary doesnt exists')
    elif type(job["min_salary"] or job["max_salary"] or salary) != int:
        raise ValueError('min_salary or max_salary arent valid integers')
    elif (job["min_salary"] > job["max_salary"]):
        raise ValueError('min_salary is greather than max_salary')
    elif (job["min_salary"] <= salary <= job["max_salary"]):
        return True
    return False
    

def filter_by_salary_range(jobs, salary):
    job_salary_list = []
    for job in jobs:
        try:
            if isinstance(salary, int) and matches_salary_range(job, salary):
                job_salary_list.append(job)
        except ValueError:
            pass
    return job_salary_list
