from utils import get_input


def is_safe(report: list[int], toleration: int = 0) -> bool:
    if report[0] > report[-1]:
        report = list(reversed(report))

    for i in range(1, len(report)):
        if not (1 <= report[i] - report[i - 1] <= 3):
            return toleration > 0 and (
                is_safe(report[:i - 1] + report[i:], toleration - 1) or
                is_safe(report[:i] + report[i + 1:], toleration - 1)
            )

    return True


reports = [[int(x) for x in line.split()] for line in get_input(2024, 2)]

print(sum(is_safe(report) for report in reports))
print(sum(is_safe(report, toleration=1) for report in reports))
