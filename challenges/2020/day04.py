import re
from typing import Sequence, Mapping, Callable

from utils import get_input, split_lines

required = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}


def is_valid_part_1(passport: Mapping[str, str]) -> bool:
    if any((r not in passport) for r in required):
        return False
    return True


def is_valid_part_2(passport: Mapping[str, str]) -> bool:
    if any((r not in passport) for r in required):
        return False
    m = re.match(r"^\d{4}$", passport['byr'])
    if not m or int(m.group(0)) < 1920 or int(m.group(0)) > 2002:
        return False
    m = re.match(r"^\d{4}$", passport['iyr'])
    if not m or int(m.group(0)) < 2010 or int(m.group(0)) > 2020:
        return False
    m = re.match(r"^\d{4}$", passport['eyr'])
    if not m or int(m.group(0)) < 2020 or int(m.group(0)) > 2030:
        return False
    m = re.match(r"^(\d+)(cm|in)$", passport['hgt'])
    if not m:
        return False
    if m.group(2) == 'cm' and (int(m.group(1)) < 150 or int(m.group(1)) > 193):
        return False
    if m.group(2) == 'in' and (int(m.group(1)) < 59 or int(m.group(1)) > 76):
        return False
    m = re.match(r"^#[0-9a-f]{6}$", passport['hcl'])
    if not m:
        return False
    m = re.match(r"^(amb|blu|brn|gry|grn|hzl|oth)$", passport['ecl'])
    if not m:
        return False
    m = re.match(r"^[0-9]{9}$", passport['pid'])
    if not m:
        return False
    return True


def solve(passports: Sequence[Sequence[str]], is_valid: Callable[[Mapping], bool]) -> int:
    solution = 0
    for passport in passports:
        passport = {kvp.split(':')[0]: kvp.split(':')[1]
                    for line in passport for kvp in line.split(' ')}
        if is_valid(passport):
            solution += 1
    return solution


passports = split_lines(get_input(year=2020, day=4))
print(solve(passports, is_valid_part_1))
print(solve(passports, is_valid_part_2))
