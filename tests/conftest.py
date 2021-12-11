from unittest import mock

from utils import get_input_from_file


def pytest_sessionstart(session):
    patched = mock.patch(
        'utils.get_input',
        side_effect=lambda day: get_input_from_file(f"tests/inputs/day{day:02d}.txt")
    )
    patched.start()
