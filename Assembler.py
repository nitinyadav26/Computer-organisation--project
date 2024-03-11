# registers binary code
line_counter = 0
list_output = []
label_names = {}
label_collection = []
list_of_errors = []
instructions = []

# Dictionary mapping register names to their binary representations
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

# Dictionary mapping instructions to their binary opcodes
# Dictionary mapping instructions to their binary opcodes
instruction_dict = {
    "add": "0110011",    # Add
    "sub": "0110011",    # Subtract
    "sll": "0110011",    # Shift Left Logical
    "srl": "0110011",    # Shift Right Logical
    "slt": "0110011",    # Set Less Than
    "sltu": "0110011",   # Set Less Than Unsigned
    "xor": "0110011",    # Exclusive OR
    "Or": "0110011",     # Logical OR
    "And": "0110011",    # Logical AND

    "lw": "0000011",     # Load Word
    "addi": "0010011",   # Add Immediate
    "sltiu": "0010011",  # Set Less Than Immediate Unsigned
    "jalr": "1100111",   # Jump and Link Register

    # Instructions for Bonus part to be done later
    # "mul": "0000000",
    # "rst": "0000000",
    # "halt": "0000000",
    # "rvrs": "0000000",
}

# Dictionary mapping instructions to their function3 values
function3 = {
    "add": "000",    # Add
    "sub": "000",    # Subtract
    "sll": "001",    # Shift Left Logical
    "srl": "101",    # Shift Right Logical
    "slt": "010",    # Set Less Than
    "sltu": "011",   # Set Less Than Unsigned
    "xor": "100",    # Exclusive OR
    "Or": "110",     # Logical OR
    "And": "111",    # Logical AND

    "lw": "010",     # Load Word
    "addi": "000",   # Add Immediate
    "sltiu": "011",  # Set Less Than Immediate Unsigned
    "jalr": "000",   # Jump and Link Register
}

# Dictionary mapping instructions to their function7 values
function7 = {
    "add": "0000000",    # Add
    "sub": "0100000",    # Subtract
    "sll": "0000000",    # Shift Left Logical
    "srl": "0000000",    # Shift Right Logical
    "slt": "0000000",    # Set Less Than
    "sltu": "0000000",   # Set Less Than Unsigned
    "xor": "0000000",    # Exclusive OR
    "Or": "0000000",     # Logical OR
    "And": "0000000",    # Logical AND
}


def type_R(instruct, list_output):
    s = ""

    if instruct[0] not in function7 or instruct[0] not in function3 or instruct[0] not in instruction_dict:
        # Handle unrecognized instruction
        print(f"Unrecognized instruction: {instruct[0]}")
        return

    s += function7[instruct[0]]
    s += register_to_binary[instruct[3]]
    s += register_to_binary[instruct[2]]
    s += function3[instruct[0]]
    s += register_to_binary[instruct[1]]
    s += instruction_dict[instruct[0]]

    list_output.append(s)

def decimal_to_12bit_binary(decimal_num):
    # Ensure the input is a non-negative integer or 0
    if not isinstance(decimal_num, int) or decimal_num < 0:
        raise ValueError("Input must be a non-negative integer or 0")

    # Convert decimal to binary and format as 12 bits
    binary_representation = format(decimal_num, '012b')

    return binary_representation

def type_I(instruct, list_output):
    numeric_value_str = instruct[2]  # Remove the comma from the numeric value
    s = decimal_to_12bit_binary(int(numeric_value_str))  # Convert the numeric value to binary

    if instruct[0] not in function3 or instruct[0] not in instruction_dict:
        # Handle unrecognized instruction
        print(f"Unrecognized instruction: {instruct[0]}")
        return

    register_name = instruct[3]  # Remove the comma from the register name
    s += register_to_binary.get(register_name, "")
    s += function3.get(instruct[0], "")
    s += register_to_binary.get(instruct[1], "")
    s += instruction_dict.get(instruct[0], "")

    list_output.append(s)

instruct = ["addi", "zero", "0", "zero"]
type_I(instruct, list_output)

for i in list_output:
    print(i)
