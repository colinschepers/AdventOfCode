import argparse

from utils import get_solution, get_years, get_days

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-y', '--year', type=int)
    parser.add_argument('-d', '--day', type=int)
    args = parser.parse_args()

    year = args.year or max(get_years())
    day = args.day or max(get_days(year))
    print("\n".join(get_solution(year, day)))
