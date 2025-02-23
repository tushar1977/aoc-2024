# Open the input file
with open("t.txt", "r") as raw:
    gates = {}
    for line in raw:
        if line.isspace():
            break
        x, y = line.strip().split(": ")
        gates[x] = int(y)

    logic_gates = {}
    for line in raw:
        x, op, y, _, res = line.strip().split()
        logic_gates[res] = (op, x, y)


def compute_wire(wire):
    if wire in gates:
        return gates[wire]

    op, x, y = logic_gates[wire]

    x_val = compute_wire(x)
    y_val = compute_wire(y)

    if op == "AND":
        gates[wire] = x_val & y_val
    elif op == "OR":
        gates[wire] = x_val | y_val
    elif op == "XOR":
        gates[wire] = x_val ^ y_val

    return gates[wire]


output_wires = sorted(wire for wire in logic_gates if wire.startswith("z"))
outputs = [compute_wire(wire) for wire in output_wires]

binary_number = "".join(map(str, outputs[::-1]))
decimal_number = int(binary_number, 2)

print(decimal_number)
