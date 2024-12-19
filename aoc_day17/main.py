import re

with open("t.txt", "r") as f:
    raw = f.read().strip()

registers = []
program = []
split = False

for line in raw.splitlines():
    if line.strip() == "":
        split = True
        continue

    if not split:
        match = re.match(r"Register ([ABC]): (-?\d+)", line)
        if match:
            registers.append(int(match.group(2)))
    else:
        if line.startswith("Program:"):
            program = list(map(int, line.split(":")[-1].strip().split(",")))


def get_operand_value(operand, registers):
    if 0 <= operand <= 3:
        return operand
    if operand == 4:
        return registers[0]
    if operand == 5:
        return registers[1]
    if operand == 6:
        return registers[2]
    raise ValueError("Invalid combo operand")


def process_instruction(opcode, operand, registers, instruction_pointer, output):
    if opcode == 0:
        denominator = 2 ** get_operand_value(operand, registers)
        registers[0] //= denominator
    elif opcode == 1:
        registers[1] ^= operand
    elif opcode == 2:
        value = get_operand_value(operand, registers)
        registers[1] = value % 8
    elif opcode == 3:
        if registers[0] != 0:
            return operand
    elif opcode == 4:
        registers[1] ^= registers[2]
    elif opcode == 5:
        value = get_operand_value(operand, registers) % 8
        output.append(value)
    elif opcode == 6:
        denominator = 2 ** get_operand_value(operand, registers)
        registers[1] = registers[0] // denominator
    elif opcode == 7:
        denominator = 2 ** get_operand_value(operand, registers)
        registers[2] = registers[0] // denominator
    return instruction_pointer + 2


def run(regis):
    pointer = 0
    output = []
    while pointer < len(program):
        opcode = program[pointer]
        operand = program[pointer + 1]
        pointer = process_instruction(opcode, operand, regis, pointer, output)
    return output


def solve():
    while 1:
        out = run(registers.copy())
        if out == program:
            print(registers[0])
            break

        elif out[-13:] == program[-13:]:
            registers[0] += 1
            print(registers[0], out)

        elif out[-10:] == program[-10:]:
            registers[0] += 100
            print(registers[0], out)
        elif out[-7:] == program[-7:]:
            registers[0] += 100_0000
            print(registers[0], out)
        elif out[-3:] == program[-3:]:
            registers[0] += 10_000_000
            print(registers[0], out)
        elif out[-2:] == program[-2:]:
            registers[0] += 1_000_000_000
            print(registers[0], out)
        else:
            registers[0] += 10_000_000_0000

            print(registers[0], out)


# 12 -> 1
# 2 -> 11
# 3 -> 10
# 4 -> 9
# 5
# 6
# 7
#
solve()
