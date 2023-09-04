import nure_tools

if __name__ == '__main__':
    schedule = nure_tools.get_schedule('group',
                            nure_tools.get_group_id("ПЗПІ-23-2"),
                            "2023-09-4",
                            "2023-09-10")

    for lesson in schedule:
        print(lesson["subject"])

