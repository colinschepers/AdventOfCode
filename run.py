from pathlib import Path

challenge_files = Path("challenges/2021").glob("day*.py")
last_challenge_file = next(iter(sorted(challenge_files, reverse=True)))
__import__(f"challenges.2021.{last_challenge_file.stem}")
