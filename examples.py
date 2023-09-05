import nure_tools
from pprint import pprint
import time


def custom_sort(item):
    return int(item['start_time'])


def show_schedule():
    group = input('Enter group name (like ПЗПІ-23-2): ')
    first_date = input('Enter first date (like 2023-09-04): ')
    second_date = input('Enter second date (like 2023-09-10): ')

    schedule = nure_tools.get_schedule('group',
                                       nure_tools.get_group_id(group),
                                       first_date,
                                       second_date
                                       )

    schedule = sorted(schedule, key=custom_sort)

    lessons = []
    for lesson in schedule:
        start_time = time.gmtime(int(lesson['start_time']))
        end_time = time.gmtime(int(lesson['end_time']))

        start_time = time.strftime("%m.%d/%H:%M", start_time)
        end_time = time.strftime("%m.%d/%H:%M", end_time)

        start_time = start_time.split('/')

        lessons.append(f"{start_time[0]} - {lesson['subject']['title']}: {start_time[1]} - {end_time}")
    return lessons


def show_groups():
    groups = nure_tools.get_groups()
    groups_names = []
    for group in groups:
        groups_names.append(f"{group['name']} - {group['id']}")

    return groups_names


def show_auditories():
    auditories = nure_tools.get_auditories()
    auditories_names = []
    for aud in auditories:
        auditories_names.append(f"{aud['name']} - {aud['id']}")

    return auditories_names


def show_teachers():
    teachers = nure_tools.get_teachers()
    teachers_names = []
    for teacher in teachers:
        teachers_names.append(f"{teacher['short_name']} - {teacher['id']}")

    return teachers_names


if __name__ == '__main__':

    print(nure_tools.find_group('пзпі-23-2'))
    pprint(nure_tools.find_teacher('Новіков'))
    match(int(input('1 - schedule\n' +
                    '2 - groups\n' +
                    '3 - auditories\n' +
                    '4 - teachers\n'))):
        case 1:
            pprint(show_schedule())
        case 2:
            pprint(show_groups())
        case 3:
            pprint(show_auditories())
        case 4:
            pprint(show_teachers())

