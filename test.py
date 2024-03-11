# registers binary code
line_counter = 0
list_output = []
label_names = {}
label_collection = []
list_of_errors = []
instructions = []

register_to_binary = {
    "zero": "00000",
    "ra": "00001",
    "sp": "00010",
    "gp": "00011",
    "tp": "00100",
    "t0": "00101",
    "t1": "00110",
    "t2": "00111",
    "s0": "01000",
    "fp": "01000",
    "s1": "01001",
    "a0": "01010",
    "a1": "01011",
    "a2": "01100",
    "a3": "01101",
    "a4": "01110",
    "a5": "01111",
    "a6": "10000",
    "a7": "10001",
    "s2": "10010",
    "s3": "10011",
    "s4": "10100",
    "s5": "10101",
    "s6": "10110",
    "s7": "10111",
    "s8": "11000",
    "s9": "11001",
    "s10": "11010",
    "s11": "11011",
    "t3": "11100",
    "t4": "11101",
    "t5": "11110",
    "t6": "11111",
}

instruction_dict = {
    "add": "0110011",    # Add
    "sub": "0110011",    # Subtract
    "sll": "0110011",
    "srl": "0110011",
    "slt": "0110011",
    "sltu": "0110011",
    "xor": "0110011",    # Exclusive OR
    "Or": "0110011",     # Logical OR
    "And": "0110011",    # Logical AND

    "lw":"0000011",
    "addi":"0010011",
    "sltiu":"0010011",
    "jalr":"1100111",

}

function3 = {
    "add": "000",    # Add
    "sub": "000",    # Subtract
    "sll": "001",
    "srl": "101",
    "slt": "010",
    "sltu": "011",
    "xor": "100",    # Exclusive OR
    "Or": "110",     # Logical OR
    "And": "111",    # Logical AND

    "lw":"010",
    "addi":"000",
    "sltiu":"011",
    "jalr":"000",


}

function7 = {
    "add": "0000000",    # Add
    "sub": "0100000",    # Subtract
    "sll": "0000000",
    "srl": "0000000",
    "slt": "0000000",
    "sltu": "0000000",
    "xor": "0000000",    # Exclusive OR
    "Or": "0000000",     # Logical OR
    "And": "0000000",    # Logical AND
}

def decimal_to_12bit_binary(decimal_num):
    # Ensure the input is a non-negative integer
    if not isinstance(decimal_num, int) or decimal_num < 0:
        raise ValueError("Input must be a non-negative integer")

    # Convert decimal to binary and format as 12 bits
    binary_representation = format(decimal_num, '012b')

    return binary_representation




def type_R(instruct, list_output):
    s = ""

    if instruct[0] not in function7 or instruct[0] not in function3 or instruct[0] not in instruction_dict:
        # Handle unrecognized instruction
        print(f"Unrecognized instruction: {instruct[0]}")
        return

    s += instruction_dict.get(instruct[0], "")
    s += register_to_binary.get(instruct[3], "")
    s += register_to_binary.get(instruct[2], "")
    s += register_to_binary.get(instruct[1], "")
    s += function3.get(instruct[0], "")
    s += register_to_binary.get(instruct[0], "")
    s += function7.get(instruct[0], "")

    list_output.append(s)


def type_I(instruct, list_output):
    s = ""

    if instruct[0] not in function3 or instruct[0] not in instruction_dict:
        # Handle unrecognized instruction
        print(f"Unrecognized instruction: {instruct[0]}")
        return

    s += instruction_dict.get(instruct[0], "")
    s += register_to_binary.get(instruct[2], "")
    s += register_to_binary.get(instruct[1], "")
    s += decimal_to_12bit_binary(int(instruct[3]))  # Convert the immediate value to binary
    list_output.append(s)


instruct = ["addi", "rd", "rs", "5"]
type_I(instruct, list_output)

for i in list_output:
    print(i)
