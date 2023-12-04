"""Simple pyton library for nure-cist API"""

__version__ = '1.7.0'

import requests
import time
from typing import Literal



def convert_time(time_toconvert: str | int, pattern: str) -> int:
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


def get_groups() -> list:
    groups_respond = requests.get('https://api.mindenit.tech/groups')

    if groups_respond.status_code == 200:
        respond = []
        for group in groups_respond.json():
            group["id"] = int(group["id"])
            respond.append(group)
        return respond
    else:
        groups_respond.raise_for_status()


def get_teachers() -> list:
    teachers_respond = requests.get('https://api.mindenit.tech/teachers')

    if teachers_respond.status_code == 200:
        respond = []
        for teacher in teachers_respond.json():
            teacher["id"] = int(teacher["id"])
            respond.append(teacher)
        return respond
    else:
        teachers_respond.raise_for_status()


def get_auditoriums() -> list:
    auditoriums_respond = requests.get('https://api.mindenit.tech/auditories')

    if auditoriums_respond.status_code == 200:
        respond = []
        for auditorium in auditoriums_respond.json():
            auditorium["id"] = int(auditorium["id"])
            respond.append(auditorium)
        return respond
    else:
        auditoriums_respond.raise_for_status()


def get_schedule(request_type: Literal['group', 'teacher', 'auditory'],
                 request_id: int,
                 start_time: str,
                 end_time: str,
                 pattern: str = "%Y-%m-%d %H:%M"
                 ) -> list:
    start_time = convert_time(start_time, pattern)
    end_time = convert_time(end_time, pattern)

    if request_type not in ['group', 'teacher', 'auditory']:
        raise ValueError('Invalid request type')

    schedule_respond = requests.get(
        f'https://api.mindenit.tech/schedule?type={request_type}&id={request_id}&start_time={start_time}&end_time={end_time}')

    if schedule_respond.status_code == 200:
        respond = []
        for lesson in schedule_respond.json():
            lesson["startTime"] = int(lesson["startTime"])
            lesson["endTime"] = int(lesson["endTime"])
            lesson["subject"]["id"] = int(lesson["subject"]["id"])

            teachers = []
            for teacher in lesson["teachers"]:
                teacher["id"] = int(teacher["id"])
                teachers.append(teacher)
            lesson["teachers"] = teachers

            groups = []
            for group in lesson["groups"]:
                group["id"] = int(group["id"])
                groups.append(group)
            lesson["groups"] = groups

            respond.append(lesson)

        return respond
    else:
        schedule_respond.raise_for_status()


def find_group(group_name: str) -> list:
    groups = get_groups()
    for group in groups:
        if group["name"].lower() == group_name.lower():
            return group
    raise ValueError(f"Couldn\'t find group \"{group_name}\"")


def find_teacher(teacher_name: str) -> list:

    teacher_name = teacher_name.lower()
    teachers = get_teachers()

    result = []
    for teacher in teachers:
        if teacher_name[-1] == '.':
            if teacher["shortName"].lower() == teacher_name:
                result.append(teacher)
                return result
        else:
            if teacher_name in teacher["shortName"].lower():
                result.append(teacher)

    if len(result) != 0:
        return result

    raise ValueError(f"Couldn\'t find teacher \"{teacher_name}\", make shour that you wrote name correctly (for example \"Саманцов О. О.\" or \"Саманцов\")")


def find_auditorium(auditorium_name: str) -> list:
    auditoriums = get_auditoriums()
    for auditorium in auditoriums:
        if auditorium["name"] == auditorium_name:
            return auditorium
    raise ValueError(f"Couldn\'t find group \"{auditorium_name}\"")
