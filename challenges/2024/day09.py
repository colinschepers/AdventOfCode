from collections.abc import Sequence
from dataclasses import dataclass

from utils import get_input


@dataclass
class Block:
    position: int
    length: int
    file_id: int | None = None


def checksum_1(disk_map: Sequence[int]) -> int:
    flattened = []
    for i, length in enumerate(disk_map):
        file_id = i // 2 if i % 2 == 0 else None
        flattened.extend(file_id for _ in range(length))

    free_space_idx = 0
    for file_idx in range(len(flattened) - 1, -1, -1):
        if flattened[file_idx] is None:
            continue
        while free_space_idx <= file_idx and flattened[free_space_idx] is not None:
            free_space_idx += 1
        if file_idx <= free_space_idx:
            break

        flattened[free_space_idx] = flattened[file_idx]
        flattened[file_idx] = None

    return sum(i * (file_id or 0) for i, file_id in enumerate(flattened))


def checksum_2(disk_map: Sequence[int]) -> int:
    blocks: list[Block] = []
    position = 0
    for i, length in enumerate(disk_map):
        blocks.append(Block(position, length, file_id=i // 2 if i % 2 == 0 else None))
        position += length

    for i in range(len(blocks) - 1, -1, -2):
        file = blocks[i]
        free_space_before_file = blocks[i - 1]
        for j in range(1, i, 2):
            free_space = blocks[j]

            if file.length <= free_space.length:
                file.position = free_space.position
                free_space_before_file.length += file.length
                free_space.position += file.length
                free_space.length -= file.length
                break

    return sum(
        (block.position + i) * (block.file_id or 0)
        for block in sorted(blocks, key=lambda x: x.position)
        for i in range(block.length)
    )


disk_map = [int(char) for char in get_input(2024, 9)[0]]

print(checksum_1(disk_map))
print(checksum_2(disk_map))
