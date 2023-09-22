# `nure_tools python library`

> **Warning**
> The library is still under development. I will be happy to receive any feedback, and you can feel free to improve my code

> Simple pyton library for nure-cist API

> You can also check out [NodeJS library](https://github.com/OneLiL05/nurekit) made by OneLil05

> And don't forget to star [nure-cist-api](https://github.com/nure-dev/nure-cist-api)

****************************************************************

# Installation

> (Python 3.10+)
 
### using bash/zsh/fish/etc (for linux)

> **Warning**
> If you using arch-based distro you may need to set venv first and use pip from that place.
> PyCharm will make it automatically, just type following command in PyCharm terminal.

```shell
git clone https://github.com/SoappGuy/nure_tools.git && cd ./nure_tools && python -m pip install -e .

```

### using PowerShell (for windows)
```shell
git clone https://github.com/SoappGuy/nure_tools.git ; cd ./nure_tools ; python -m pip install -e .
```
****************************************************************

# Examples
> for more examples see [examples.py file](https://github.com/SoappGuy/nure_tools/blob/master/examples.py)


## Functions

### Get auditoriums

> [Reference](https://nure-dev.pp.ua/#%D0%B7%D0%B0%D0%BF%D0%B8%D1%82-%D0%BD%D0%B0-%D0%B0%D1%83%D0%B4%D0%B8%D1%82%D0%BE%D1%80%D1%96%D1%97)

**Example:**

```python
import nure_tools
from pprint import pprint

auditories = nure_tools.get_auditories()
pprint(auditories)    
```

**Output:**

```ts
[{'id': '172', 'name': '___0'},
 {'id': '3931027', 'name': '285'},
 {'id': '97', 'name': '287'},
 ...
 ...
  {'id': '169', 'name': '165-6'},
 {'id': '1675427', 'name': '166вц'},
 {'id': '170', 'name': '167вц'}]
```

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
[{'id': '6949796', 'name': 'ЕЕК-18-1'},
 {'id': '7310687', 'name': 'ЕЕКи-18-1'},
 ...
 ...
 {'id': '10486626', 'name': 'ЕЕКі-22-1'},
 {'id': '11106524', 'name': 'ЕЕКі-23-1'}]
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
{'id': '10887378', 'name': 'ПЗПІ-23-2'}
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
[{'full_name': 'Боцюра Олеся Анатоліївна', 'id': '5343992', 'short_name': 'Боцюра О. А.'},
 {'full_name': 'Бутенко Ніна Семенівна', 'id': '1810189', 'short_name': 'Бутенко Н. С.'},
 ...
 ...
 {'full_name': 'Бабкова Н І', 'id': '7605119', 'short_name': 'Бабкова Н. І.'},
 {'full_name': 'Карпенко К І', 'id': '8769045', 'short_name': 'Карпенко К. І.'}]
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
[{'full_name': 'Новіков Олексій Валентинович',
  'id': '7278549',
  'short_name': 'Новіков О. В.'},
 {'full_name': 'Новіков Юрій Сергійович',
  'id': '2145721',
  'short_name': 'Новіков Ю. С.'}]
```

****************************************************************

### Get schedule

> [Reference](https://nure-dev.pp.ua/#%D0%B7%D0%B0%D0%BF%D0%B8%D1%82-%D0%BD%D0%B0-%D1%80%D0%BE%D0%B7%D0%BA%D0%BB%D0%B0%D0%B4)

**Example:**

```python
import nure_tools
from pprint import pprint

schedule = nure_tools.get_schedule('group',
                                    nure_tools.find_group("пзпі-23-2")["id"],
                                    "2023-09-25",
                                    "2023-09-26"
                                    )


pprint(schedule)

```

**Output:**

```ts
[{'auditory': 'спорт',
  'end_time': '1695642300',
  'groups': [{'id': '10887378', 'name': 'ПЗПІ-23-2'}],
  'id': '64031',
  'number_pair': 4,
  'start_time': '1695636600',
  'subject': {'brief': 'ФВ',
              'id': '8051836',
              'title': 'Фізичне виховання (за рахунок вільного часу '
                       'студентів)'},
  'teachers': [],
  'type': 'Пз',
  'updatedAt': '2023-09-22T17:10:31.354Z'},
 {'auditory': '324і',
  'end_time': '1695635400',
  'groups': [{'id': '10887378', 'name': 'ПЗПІ-23-2'}],
  'id': '64030',
  'number_pair': 3,
  'start_time': '1695629700',
  'subject': {'brief': 'ІМ', 'id': '1021424', 'title': 'Іноземна мова'},
  'teachers': [{'full_name': 'Новіков Олексій Валентинович',
                'id': '7278549',
                'short_name': 'Новіков О. В.'}],
  'type': 'Пз',
  'updatedAt': '2023-09-22T17:10:31.347Z'},
 {'auditory': 'спорт',
  'end_time': '1695642300',
  'groups': [{'id': '10887378', 'name': 'ПЗПІ-23-2'}],
  'id': '63852',
  'number_pair': 4,
  'start_time': '1695636600',
  'subject': {'brief': 'ФВ',
              'id': '8051836',
              'title': 'Фізичне виховання (за рахунок вільного часу '
                       'студентів)'},
  'teachers': [],
  'type': 'Пз',
  'updatedAt': '2023-09-22T17:07:03.133Z'},
 {'auditory': '324і',
  'end_time': '1695635400',
  'groups': [{'id': '10887378', 'name': 'ПЗПІ-23-2'}],
  'id': '63851',
  'number_pair': 3,
  'start_time': '1695629700',
  'subject': {'brief': 'ІМ', 'id': '1021424', 'title': 'Іноземна мова'},
  'teachers': [{'full_name': 'Новіков Олексій Валентинович',
                'id': '7278549',
                'short_name': 'Новіков О. В.'}],
  'type': 'Пз',
  'updatedAt': '2023-09-22T17:07:03.126Z'},
 {'auditory': 'спорт',
  'end_time': '1695642300',
  'groups': [{'id': '10887378', 'name': 'ПЗПІ-23-2'}],
  'id': '6651',
  'number_pair': 4,
  'start_time': '1695636600',
  'subject': {'brief': 'ФВ',
              'id': '8051836',
              'title': 'Фізичне виховання (за рахунок вільного часу '
                       'студентів)'},
  'teachers': [],
  'type': 'Пз',
  'updatedAt': '2023-09-18T16:30:21.540Z'},
 {'auditory': '324і',
  'end_time': '1695635400',
  'groups': [{'id': '10887378', 'name': 'ПЗПІ-23-2'}],
  'id': '6650',
  'number_pair': 3,
  'start_time': '1695629700',
  'subject': {'brief': 'ІМ', 'id': '1021424', 'title': 'Іноземна мова'},
  'teachers': [{'full_name': 'Новіков Олексій Валентинович',
                'id': '7278549',
                'short_name': 'Новіков О. В.'}],
  'type': 'Пз',
  'updatedAt': '2023-09-18T16:30:21.533Z'}]
```

****************************************************************

## Licence

nure_tools is [GNU GPLv3.0 licenced](https://github.com/SoappGuy/nure_tools/blob/master/LICENSE)