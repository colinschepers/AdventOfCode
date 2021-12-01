from pathlib import Path

challenge_files = Path("challenges").glob("day*.py")
last_challenge_file = next(iter(sorted(challenge_files, reverse=True)))
__import__(f"challenges.{last_challenge_file.stem}")
