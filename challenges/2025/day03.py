from utils import argmax, get_input


def get_max_joltage(bank: str, battery_count: int) -> int:
    joltage = ""
    for batteries_remaining in range(battery_count - 1, -1, -1):
        idx = argmax(bank[:len(bank) - batteries_remaining])
        joltage += bank[idx]
        bank = bank[idx + 1:]
    return int(joltage)


banks = get_input(2025, 3)
print(sum(get_max_joltage(bank, battery_count=2) for bank in banks))
print(sum(get_max_joltage(bank, battery_count=12) for bank in banks))
