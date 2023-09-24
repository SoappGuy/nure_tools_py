# `nure_tools python library`

> **Warning**
> The library is still under development. I will be happy to receive any feedback, and you can feel free to improve my code

> Simple pyton library for nure-cist API

> You can also check out [NodeJS library](https://github.com/OneLiL05/nurekit) made by OneLil05

> And don't forget to star [nure-cist-api](https://github.com/nure-dev/nure-cist-api)

****************************************************************
# PyPi
> [Project page on PyPi](https://pypi.org/project/nure_tools/)


# Installation

> (Python 3.10+)

> **Warning**
> If you are using arch-based distro you may need to set venv first and use pip from that place.
> PyCharm will make it automatically, just type following command in PyCharm terminal.

```shell
pip install nure_tools

```

****************************************************************

## Functions

### Get auditoriums

> [Reference](https://nure-dev.pp.ua/#%D0%B7%D0%B0%D0%BF%D0%B8%D1%82-%D0%BD%D0%B0-%D0%B0%D1%83%D0%B4%D0%B8%D1%82%D0%BE%D1%80%D1%96%D1%97)

**Example:**

```python
import nure_tools
from pprint import pprint

auditoriums = nure_tools.get_auditoriums()
pprint(auditoriums)    

```

**Output:**

```ts
 [{'id': 167, 'name': '165-3'},
 {'id': 168, 'name': '165-5'},
 {'id': 169, 'name': '165-6'},
 ...
 {'id': 1675427, 'name': '166вц'},
 {'id': 170, 'name': '167вц'},
 {'id': 97, 'name': '287'}]
```

### Find an auditorium

**Example:**

```python
import nure_tools

print(nure_tools.find_auditorium("165-1"))
```

**Output:**

```ts
{'id': 165, 'name': '165-1'}
```

****************************************************************
****************************************************************

### Get groups

> [Reference](https://nure-dev.pp.ua/#%D0%B7%D0%B0%D0%BF%D0%B8%D1%82-%D0%BD%D0%B0-%D0%B3%D1%80%D1%83%D0%BF%D0%B8)

**Example:**

```python
import nure_tools
from pprint import pprint

groups = nure_tools.get_groups()
pprint(groups)
```

**Output:**

```ts
[{'id': 10887382, 'name': 'ПЗПІ-23-3'},
 {'id': 10284397, 'name': 'ЕЕПСу-22-1'},
 {'id': 10307166, 'name': 'КУІБ-22-1'},
 ...
 {'id': 10307432, 'name': 'ІСТ-22-1'},
 {'id': 10887104, 'name': 'КІУКІ-23-7'},
 {'id': 10887108, 'name': 'КІУКІу-23-1'}]
```

****************************************************************

### Find a group

**Example:**

```python
import nure_tools

print(nure_tools.find_group("пзпі-23-2"))
```

**Output:**

```ts
{'id': 10887378, 'name': 'ПЗПІ-23-2'}
```

****************************************************************

### Get teachers

> [Reference](https://nure-dev.pp.ua/#%D0%B7%D0%B0%D0%BF%D0%B8%D1%82-%D0%BD%D0%B0-%D0%B2%D0%B8%D0%BA%D0%BB%D0%B0%D0%B4%D0%B0%D1%87%D1%96%D0%B2)

**Example:**

```python
import nure_tools
from pprint import pprint

teachers = nure_tools.get_teachers()
pprint(teachers)

```

**Output:**

```ts
 [{'full_name': 'Богатов Євген Олегович',
  'id': 7067189,
  'short_name': 'Богатов Є. О.'},
 {'full_name': 'Демчук Вадим Геннадійович',
  'id': 11127911,
  'short_name': 'Демчук В. Г.'},
  ...
 {'full_name': 'Новіков Юрій Сергійович',
  'id': 2145721,
  'short_name': 'Новіков Ю. С.'},
 {'full_name': 'Новіков Олексій Валентинович',
  'id': 7278549,
  'short_name': 'Новіков О. В.'}]
```

****************************************************************

### Find a teacher

**Example:**

```python
import nure_tools
from pprint import pprint

pprint(nure_tools.find_teacher("Новіков"))
```

**Output:**

```ts
[{'full_name': 'Новіков Юрій Сергійович',
  'id': 2145721,
  'short_name': 'Новіков Ю. С.'},
 {'full_name': 'Новіков Олексій Валентинович',
  'id': 7278549,
  'short_name': 'Новіков О. В.'}]
```

****************************************************************

### Get schedule

> [Reference](https://nure-dev.pp.ua/#%D0%B7%D0%B0%D0%BF%D0%B8%D1%82-%D0%BD%D0%B0-%D1%80%D0%BE%D0%B7%D0%BA%D0%BB%D0%B0%D0%B4)

**Example:**

```python
import nure_tools
from pprint import pprint

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


pprint(schedule_group)
pprint(schedule_teacher)
pprint(schedule_auditorium)

```

**Output:**

```ts
[{'auditory': '324і',
  'end_time': 1695635400,
  'groups': [{'id': 10887378, 'name': 'ПЗПІ-23-2'}],
  'id': 78260,
  'number_pair': 3,
  'start_time': 1695629700,
  'subject': {'brief': 'ІМ', 'id': 1021424, 'title': 'Іноземна мова'},
  'teachers': [{'full_name': 'Новіков Олексій Валентинович',
                'id': 7278549,
                'short_name': 'Новіков О. В.'}],
  'type': 'Пз',
  'updatedAt': '2023-09-24T03:15:06.251Z'}
]

[{'auditory': '287',
  'end_time': 1695728700,
  'groups': [{'id': 10284309, 'name': 'ПЗПІ-22-2'}],
  'id': '78422',
  'number_pair': 4,
  'start_time': 1695723000,
  'subject': {'brief': 'ВдоIT',
              'id': 5682810,
              'title': 'Введення до IT-бізнесу'},
  'teachers': [],
  'type': 'Пз',
  'updatedAt': '2023-09-24T08:13:39.459Z'},

.........

 {'auditory': '287',
  'end_time': 1695635400,
  'groups': [{'id': 8476408, 'name': 'ПЗПІ-20-8'},
             {'id': 8744039, 'name': 'ПЗПІ-20-5'},
             {'id': 8476364, 'name': 'ПЗПІ-20-7'},
             {'id': 8476572, 'name': 'ПЗПІ-20-9'},
             {'id': 8744041, 'name': 'ПЗПІ-20-10'}],
  'id': 78421,
  'number_pair': 3,
  'start_time': 1695629700,
  'subject': {'brief': '*ОКР',
              'id': 10888509,
              'title': '*Основи колективної роботи над проектом'},
  'teachers': [],
  'type': 'Пз',
  'updatedAt': '2023-09-24T08:13:39.439Z'}
] 

[{'auditory': '287',
  'end_time': 1695629100,
  'groups': [{'id': 9291678, 'name': 'ПЗПІ-21-6'}],
  'id': '78420',
  'number_pair': 2,
  'start_time': '1695623400',
  'subject': {'brief': 'ПарП',
              'id': 1989780,
              'title': 'Паралельне програмування'},
  'teachers': [{'full_name': 'Кравець Наталя Сергіївна',
                'id': 7063375,
                'short_name': 'Кравець Н. С.'}],
  'type': 'Лб',
  'updatedAt': '2023-09-24T08:13:39.429Z'},

.........

 {'auditory': '287',
  'end_time': 1695622800,
  'groups': [{'id': 9291678, 'name': 'ПЗПІ-21-6'}],
  'id': 78419,
  'number_pair': 1,
  'start_time': 1695617100,
  'subject': {'brief': 'ПарП',
              'id': 1989780,
              'title': 'Паралельне програмування'},
  'teachers': [{'full_name': 'Кравець Наталя Сергіївна',
                'id': 7063375,
                'short_name': 'Кравець Н. С.'}],
  'type': 'Лб',
  'updatedAt': '2023-09-24T08:13:39.420Z'}
] 

```

****************************************************************

## Licence

nure_tools is [GNU GPLv3.0 licenced](https://github.com/SoappGuy/nure_tools/blob/master/LICENSE)