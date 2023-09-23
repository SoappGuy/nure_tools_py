# `nure_tools python library`

> **Warning**
> The library is still under development. I will be happy to receive any feedback, and you can feel free to improve my code

> Simple pyton library for nure-cist API

> You can also check out [NodeJS library](https://github.com/OneLiL05/nurekit) made by OneLil05

> And don't forget to star [nure-cist-api](https://github.com/nure-dev/nure-cist-api)

****************************************************************

# Installation

> (Python 3.10+)

> **Warning**
> If you using arch-based distro you may need to set venv first and use pip from that place.
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
 [Auditorium(id='10', name='каф.СІ'),
  Auditorium(id='156', name='151-1'),
  Auditorium(id='157', name='151-2'),
  ...
  Auditorium(id='169', name='165-6'),
  Auditorium(id='1675427', name='166вц'),
  Auditorium(id='170', name='167вц')]
```

### Find an auditorium

**Example:**

```python
import nure_tools

print(nure_tools.find_auditorium("165-1"))
```

**Output:**

```ts
  Auditorium(id='165', name='165-1')
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
[Group(id='11128338', name='ПЗПІиз-23-1'),
 Group(id='10304333', name='КІУКІ-22-7'),
 Group(id='10307432', name='ІСТ-22-1'),
 ...
 Group(id='11103296', name='ПЗПІ-23-5'),
 Group(id='10887382', name='ПЗПІ-23-3'),
 Group(id='10307166', name='КУІБ-22-1')]
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
  Group(id='10887378', name='ПЗПІ-23-2')
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
 [Teacher(id='7067189',
         short_name='Богатов Є. О.',
         full_name='Богатов Євген Олегович'),
  Teacher(id='11127911',
         short_name='Демчук В. Г.',
         full_name='Демчук Вадим Геннадійович'),
  ...
  Teacher(id='7278549',
         short_name='Новіков О. В.',
         full_name='Новіков Олексій Валентинович'),
  Teacher(id='2145721',
         short_name='Новіков Ю. С.',
         full_name='Новіков Юрій Сергійович')]
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
[Teacher(id='7278549',
         short_name='Новіков О. В.',
         full_name='Новіков Олексій Валентинович'),
 Teacher(id='2145721',
         short_name='Новіков Ю. С.',
         full_name='Новіков Юрій Сергійович')]
```

****************************************************************

### Get schedule

> [Reference](https://nure-dev.pp.ua/#%D0%B7%D0%B0%D0%BF%D0%B8%D1%82-%D0%BD%D0%B0-%D1%80%D0%BE%D0%B7%D0%BA%D0%BB%D0%B0%D0%B4)

**Example:**

```python
import nure_tools
from pprint import pprint

schedule_group = nure_tools.get_schedule('group',
                                         nure_tools.find_group("пзпі-23-2").id,
                                         "2023-09-25",
                                         "2023-09-26"
                                         )

schedule_teacher = nure_tools.get_schedule('teacher',
                                           nure_tools.find_teacher("Новіков О. В.")[0].id,
                                           "2023-09-25",
                                           "2023-09-26"
                                           )

schedule_auditorium = nure_tools.get_schedule('auditory',
                                              nure_tools.find_auditorium("287").id,
                                              "2023-09-25",
                                              "2023-09-26"
                                              )


pprint(schedule_group)


```

**Output:**

```ts
[Lesson(id='69425',
        type='Пз',
        auditorium=Auditorium(id='-4', name='спорт'),
        number_pair=4,
        start_time='1695636600',
        end_time='1695642300',
        groups=[Group(id='10887378', name='ПЗПІ-23-2')],
        updated_at='2023-09-23T08:35:40.450Z',
        subject=Subject(id='8051836',
                        brief='ФВ',
                        title='Фізичне виховання (за рахунок вільного часу '
                              'студентів)'),
        teachers=[]),
 Lesson(id='69424',
        type='Пз',
        auditorium=Auditorium(id='6139762', name='324і'),
        number_pair=3,
        start_time='1695629700',
        end_time='1695635400',
        groups=[Group(id='10887378', name='ПЗПІ-23-2')],
        updated_at='2023-09-23T08:35:40.443Z',
        subject=Subject(id='1021424', brief='ІМ', title='Іноземна мова'),
        teachers=[Teacher(id='7278549',
                          short_name='Новіков О. В.',
                          full_name='Новіков Олексій Валентинович')])
]

[Lesson(id='69424',
        type='Пз',
        auditorium=Auditorium(id='6139762', name='324і'),
        number_pair=3,
        start_time='1695629700',
        end_time='1695635400',
        groups=[Group(id='10887378', name='ПЗПІ-23-2')],
        updated_at='2023-09-23T08:35:40.443Z',
        subject=Subject(id='1021424', brief='ІМ', title='Іноземна мова'),
        teachers=[Teacher(id='7278549',
                          short_name='Новіков О. В.',
                          full_name='Новіков Олексій Валентинович')])
]
                          
[Lesson(id='69613',
        type='Пз',
        auditorium=Auditorium(id='97', name='287'),
        number_pair=3,
        start_time='1695629700',
        end_time='1695635400',
        groups=[Group(id='8476408', name='ПЗПІ-20-8'),
                Group(id='8744039', name='ПЗПІ-20-5'),
                Group(id='8744041', name='ПЗПІ-20-10'),
                Group(id='8476364', name='ПЗПІ-20-7'),
                Group(id='8476572', name='ПЗПІ-20-9')],
        updated_at='2023-09-23T09:03:34.022Z',
        subject=Subject(id='10888509',
                        brief='*ОКР',
                        title='*Основи колективної роботи над проектом'),
        teachers=[Teacher(id='3204550',
                          short_name='Голян Н. В.',
                          full_name='Голян Наталія Вікторівна')]),
 
 ....
 
 Lesson(id='69611',
        type='Лб',
        auditorium=Auditorium(id='97', name='287'),
        number_pair=1,
        start_time='1695617100',
        end_time='1695622800',
        groups=[Group(id='9291678', name='ПЗПІ-21-6')],
        updated_at='2023-09-23T09:03:33.995Z',
        subject=Subject(id='1989780',
                        brief='ПарП',
                        title='Паралельне програмування'),
        teachers=[Teacher(id='7063375',
                          short_name='Кравець Н. С.',
                          full_name='Кравець Наталя Сергіївна')])
 ]                          

```

****************************************************************

## Licence

nure_tools is [GNU GPLv3.0 licenced](https://github.com/SoappGuy/nure_tools/blob/master/LICENSE)