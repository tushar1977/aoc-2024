with open("t.txt", "r") as f:
    raw = f.read().splitlines()

new_disk = []

id = 0
for line in raw:
    for i, data in enumerate(line):
        if i % 2 == 0:
            for j in range(int(data)):
                new_disk.append(id)
            id += 1
        elif i % 2 != 0:
            for k in range(int(data)):
                new_disk.append(".")


def find_free_spans(disk):
    spans = []
    start = -1

    for i in range(len(disk)):
        if disk[i] == ".":
            if start == -1:
                start = i
        else:
            if start != -1:
                spans.append((start, i - 1))
                start = -1

    if start != -1:
        spans.append((start, len(disk) - 1))

    return spans


def find_files(disk):
    files = {}
    i = 0

    while i < len(disk):
        if disk[i] != ".":
            file_id = disk[i]
            start = i
            while i < len(disk) and disk[i] == file_id:
                i += 1
            files[file_id] = (start, i - 1)
        else:
            i += 1

    return sorted(files.items(), key=lambda x: -int(x[0]))


def move_file(disk, start, end, new_start):
    file_size = end - start + 1
    for i in range(file_size):
        disk[new_start + i] = disk[start + i]

    for i in range(start, end + 1):
        disk[i] = "."


def part_2(disk):
    files = find_files(disk)

    for file_id, (start, end) in files:
        free_spans = find_free_spans(disk)

        file_size = end - start + 1
        for free_start, free_end in free_spans:
            if free_end - free_start + 1 >= file_size and free_end < start:
                move_file(disk, start, end, free_start)
                break

    return disk


def part_1(disk):
    i = 0
    j = len(disk) - 1
    while i < j:
        if disk[i] == "." and disk[j] != ".":
            disk[i], disk[j] = disk[j], disk[i]
            j -= 1
        if disk[i] != ".":
            i += 1
        if disk[j] == ".":
            j -= 1


def calc(disk):
    cnt = 0
    for i, d in enumerate(disk):
        if d != ".":
            cnt += i * int(d)
    print(cnt)


# disk_part_1 = part_1(new_disk)

# calc(disk_part_1)

disk_part_2 = part_2(new_disk)
calc(disk_part_2)
