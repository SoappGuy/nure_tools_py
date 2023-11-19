import nure_tools
from pprint import pprint
from icecream import ic

groups = nure_tools.get_groups()
teachers = nure_tools.get_teachers()
auditoriums = nure_tools.get_auditoriums()

group = nure_tools.find_group("пзпі-23-2")
teacher = nure_tools.find_teacher("новіков")
auditorium = nure_tools.find_auditorium("165-1")


# get_schedule use "%Y-%m-%d %H:%M" date/time pattern by default, but you can change it providing pattern argument
# like in example below

schedule_group = nure_tools.get_schedule('group',
                                         nure_tools.find_group("пзпі-23-2")["id"],
                                         "2023-09-25",
                                         "2023-09-26",
                                         pattern="%Y-%m-%d"
                                         )
schedule_teacher = nure_tools.get_schedule('teacher',
                                           nure_tools.find_teacher("Новіков О. В.")[0]["id"],
                                           "2023-09-25 00:00",
                                           "2023-09-26 16:30"
                                           )
schedule_auditorium = nure_tools.get_schedule('auditory',
                                              nure_tools.find_auditorium("287")["id"],
                                              "2023-09-25 00:00",
                                              "2023-09-26 16:30"
                                              )
