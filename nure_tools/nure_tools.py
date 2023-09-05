import requests
import time


def convert_time(time_toconvert):
    if type(time_toconvert) is int:
        try:
            time.strptime(time.ctime(time_toconvert))
            return time_toconvert
        except ValueError:
            raise ValueError(f"Invalid timestamp was given: {time_toconvert}")
    elif type(time_toconvert) is str:
        try:
            timestamp = int(time.mktime(time.strptime(time_toconvert, "%Y-%m-%d")))
            return timestamp
        except ValueError:
            raise ValueError("Unable to parse the input time string.\nBe sure to write time in format like '2023-09-27")
    else:
        raise ValueError("Invalid input type was given.")


def get_groups():
    groups = requests.get('https://nure-dev.pp.ua/api/groups')

    if groups.status_code == 200:
        return groups.json()
    else:
        return f'Error: {groups.status_code}'


def get_teachers():
    teachers = requests.get('https://nure-dev.pp.ua/api/teachers')

    if teachers.status_code == 200:
        return teachers.json()
    else:
        return f'Error: {teachers.status_code}'


def get_auditories():
    auditories = requests.get('https://nure-dev.pp.ua/api/auditories')

    if auditories.status_code == 200:
        return auditories.json()
    else:
        return f'Error: {auditories.status_code}'


def get_schedule(request_type, request_id, start_time, end_time):
    start_time = convert_time(start_time)
    end_time = convert_time(end_time)

    schedule = requests.get(
        f'https://nure-dev.pp.ua/api/schedule?type={request_type}&id={request_id}&start_time={start_time}&end_time={end_time}')

    if schedule.status_code == 200:
        return schedule.json()
    else:
        return f'Error: {schedule.status_code}'


def find_group(group_name):
    groups = get_groups()
    for group in groups:
        if group["name"] == group_name.upper():
            return group
    raise ValueError(f"Couldn\'t find group \"{group_name}\"")

def find_teacher(teacher_name):

    teacher_name = teacher_name.lower()
    teachers = get_teachers()

    result = []
    for teacher in teachers:
        if teacher_name[-1] == '.':
            if teacher["short_name"].lower() == teacher_name:
                result.append(teacher)
                return result
        else:
            if teacher_name in teacher["short_name"].lower():
                result.append(teacher)

    if len(result) != 0:
        return result

    raise ValueError(f"Couldn\'t find teacher \"{teacher_name}\", make shour that you wrote name correctly (for example \"Саманцов О. О.\" or \"Саманцов\")")
