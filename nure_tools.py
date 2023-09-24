"""Simple pyton library for nure-cist API"""

__version__ = '1.2'

import requests
import time


def convert_time(time_toconvert, pattern):
    if type(time_toconvert) is int:
        try:
            time.strptime(time.ctime(time_toconvert))
            return time_toconvert
        except ValueError:
            raise ValueError(f"Invalid timestamp was given: {time_toconvert}")
    elif type(time_toconvert) is str:
        try:
            timestamp = int(time.mktime(time.strptime(time_toconvert, pattern)))
            return timestamp
        except ValueError:
            raise ValueError(f"Unable to parse the input time string.\nBe sure to write time in format like {pattern}")
    else:
        raise ValueError("Invalid input type was given.")


def get_groups():
    groups_respond = requests.get('https://nure-dev.pp.ua/api/groups')

    if groups_respond.status_code == 200:
        return groups_respond.json()
    else:
        return f'Error: {groups_respond.status_code}'


def get_teachers():
    teachers_respond = requests.get('https://nure-dev.pp.ua/api/teachers')

    if teachers_respond.status_code == 200:
        return teachers_respond.json()
    else:
        return f'Error: {teachers_respond.status_code}'


def get_auditoriums():
    auditoriums_respond = requests.get('https://nure-dev.pp.ua/api/auditories')

    if auditoriums_respond.status_code == 200:
        return auditoriums_respond.json()
    else:
        return f'Error: {auditoriums_respond.status_code}'


def get_schedule(request_type, request_id, start_time, end_time, pattern="%Y-%m-%d %H:%M"):
    start_time = convert_time(start_time, pattern)
    end_time = convert_time(end_time, pattern)

    if request_type not in ['group', 'teacher', 'auditory']:
        raise ValueError('Invalid request type')

    schedule_respond = requests.get(
        f'https://nure-dev.pp.ua/api/schedule?type={request_type}&id={request_id}&start_time={start_time}&end_time={end_time}')

    if schedule_respond.status_code == 200:
        return schedule_respond.json()
    else:
        return f'Error: {schedule_respond.status_code}'


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


def find_auditorium(auditorium_name):
    auditoriums = get_auditoriums()
    for auditorium in auditoriums:
        if auditorium["name"] == auditorium_name:
            return auditorium
    raise ValueError(f"Couldn\'t find group \"{auditorium_name}\"")
