# `nurejs/api`

> **Warning**
> the library is still under development. i will be happy to receive any feedback, and feel free to improve my code

Simple pyton library for nure-dev API

## Installation

```shell
git clone https://github.com/SoappGuy/nure_tools.git &&
cd nure_git &&
python -m pip install -e .
```

## Usage

```python
import nure_tools
import pprint

pprint.pprint(nure_tools.get_groups())
# for more examples see https://github.com/examples.py
```

## Functions

### Get auditoriums

[Reference](https://nure-dev.pp.ua/#%D0%B7%D0%B0%D0%BF%D0%B8%D1%82-%D0%BD%D0%B0-%D0%B0%D1%83%D0%B4%D0%B8%D1%82%D0%BE%D1%80%D1%96%D1%97)

**Example:**

```python
import nure_tools
import pprint

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


### Get groups

[Reference](https://nure-dev.pp.ua/#%D0%B7%D0%B0%D0%BF%D0%B8%D1%82-%D0%BD%D0%B0-%D0%B3%D1%80%D1%83%D0%BF%D0%B8)

**Example:**

```python
import nure_tools
import pprint

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

### Get a group

**Example:**

```python
import nure_tools

print(nure_tools.get_group_id("пзпі-23-2"))
```

**Output:**

```ts
'10887378'
```

### Get teachers

[Reference](https://nure-dev.pp.ua/#%D0%B7%D0%B0%D0%BF%D0%B8%D1%82-%D0%BD%D0%B0-%D0%B2%D0%B8%D0%BA%D0%BB%D0%B0%D0%B4%D0%B0%D1%87%D1%96%D0%B2)

**Example:**

```python
import nure_tools
import pprint

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


### Get schedule

[Reference](https://nure-dev.pp.ua/#%D0%B7%D0%B0%D0%BF%D0%B8%D1%82-%D0%BD%D0%B0-%D1%80%D0%BE%D0%B7%D0%BA%D0%BB%D0%B0%D0%B4)

**Example:**

```python
import nure_tools

```

**Input:**

```ts
{
  groupName: string,
  startTime: number,
  endTime: number,
}
```

**Output:**

```ts
{
  id: number;
  startTime: number;
  endTime: number;
  auditorium: string;
  numberPair: number;
  type: string;
  updatedAt: Date;
  groups: {
    id: number;
    name: string;
  }[];
  teachers: {
    id: number;
    fullName: string;
    shortName: string;
  }[];
  subject: {
    id: number;
    brief: string;
    title: string;
  };
}[]
```

## Stay in touch

- Author - [Kyrylo Savieliev](https://github.com/OneLiL05)

## Licence

Nurekit is [GNU GPLv3.0 licenced](https://github.com/OneLiL05/nurekit/blob/main/LICENSE)
