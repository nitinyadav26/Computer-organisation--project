# registers binary code
line_counter = 0
list_output = []
label_names = {}
label_collection = []
list_of_errors = []
instructions = []




# Corrected instruction dictionary
instruction_dict = {
    "add": "R",    # Add
    "sub": "R",    # Subtract
    "sll": "R",    # Shift Left Logical
    "srl": "R",    # Shift Right Logical
    "slt": "R",    # Set Less Than
    "sltu": "R",   # Set Less Than Unsigned
    "xor": "R",    # Exclusive OR
    "or": "R",     # Logical OR (changed from "Or")
    "and": "R",    # Logical AND (changed from "And")

    "lw": "I",     # Load Word
    "addi": "I",   # Add Immediate
    "sltiu": "I",  # Set Less Than Immediate Unsigned
    "jalr": "I",   # Jump and Link Register

    "jal": "J",

    "lui": "U",
    "auipc": "U",

    "beq": "B",
    "bne": "B",
    "blt": "B",
    "bge": "B",
    "bltu": "B",
    "bgeu": "B",

    "sw": "S",
}

    





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
R = {

    "add": "0110011",    # Add
    "sub": "0110011",    # Subtract
    "sll": "0110011",    # Shift Left Logical
    "srl": "0110011",    # Shift Right Logical
    "slt": "0110011",    # Set Less Than
    "sltu": "0110011",   # Set Less Than Unsigned
    "xor": "0110011",    # Exclusive OR
    "Or": "0110011",     # Logical OR
    "And": "0110011",    # Logical AND

}
I = {

    "lw": "0000011",     # Load Word
    "addi": "0010011",   # Add Immediate
    "sltiu": "0010011",  # Set Less Than Immediate Unsigned
    "jalr": "1100111",   # Jump and Link Register
}
J = {

    "jal":"1101111",
}

U = {

    "lui":"0110111",
    "auipc":"0010111",
}
B = {


    "beq":"1100011",
    "bne":"1100011",
    "blt":"1100011",
    "bge":"1100011",
    "bltu":"1100011",
    "bgeu":"1100011",

}
S={
    "sw":"0100011"
}

    # Instructions for Bonus part to be done later
    # "mul": "0000000",
    # "rst": "0000000",
    # "halt": "0000000",
    # "rvrs": "0000000",


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

    "beq":"000",
    "bne":"001",
    "blt":"100",
    "bge":"101",
    "bltu":"110",
    "bgeu":"111",
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

    if instruct[0] not in function7 or instruct[0] not in function3 or instruct[0] not in R:
        # Handle unrecognized instruction
        print(f"Unrecognized instruction: {instruct[0]}")
        return

    s += function7[instruct[0]]
    s += register_to_binary[instruct[3]]
    s += register_to_binary[instruct[2]]
    s += function3[instruct[0]]
    s += register_to_binary[instruct[1]]
    s += R[instruct[0]]

    list_output.append(s)

def decimal_to_12bit_binary(decimal_number):
    # Check if the number is within the representable range for 12 bits
    if decimal_number < -2**11 or decimal_number > 2**11 - 1:
        raise ValueError("Input number is outside the representable range for 12 bits")

    # Convert negative numbers to their 2's complement form
    if decimal_number < 0:
        binary_representation = bin(decimal_number & int("1"*12, 2))[2:]
    else:
        binary_representation = bin(decimal_number)[2:]

    # Pad with zeros to make it a 12-bit binary representation
    binary_representation = binary_representation.zfill(12)

    return binary_representation

def type_I(instruct, list_output):
    numeric_value_str = instruct[2]  # Remove the comma from the numeric value
    s = decimal_to_12bit_binary(int(numeric_value_str))  # Convert the numeric value to binary

    if instruct[0] not in function3 or instruct[0] not in I:
        # Handle unrecognized instruction
        print(f"Unrecognized instruction: {instruct[0]}")
        return

    register_name = instruct[3]  # Remove the comma from the register name
    s += register_to_binary.get(register_name, "")
    s += function3.get(instruct[0], "")
    s += register_to_binary.get(instruct[1], "")
    s += I.get(instruct[0], "")

    list_output.append(s)


def decimal_to_20bit_twos_complement(decimal_number):
    # Check if the decimal number is within the valid range for a 20-bit 2's complement representation
    if decimal_number < -2**19 or decimal_number >= 2**19:
        raise ValueError("Decimal number out of range for a 20-bit 2's complement representation")

    # Handle negative numbers
    if decimal_number < 0:
        binary_representation = bin(decimal_number + 2**20)[2:]
    else:
        binary_representation = bin(decimal_number)[2:]

    # Pad the binary representation with zeros to make it 20 bits long
    padded_binary = binary_representation.zfill(20)

    return padded_binary





def type_J(instruct, list_output):
    numeric_value_str = instruct[2]  # Remove the comma from the numeric value
    k = decimal_to_20bit_twos_complement(int(numeric_value_str))  # Convert the numeric value to binary
    
    # Extract the bits from the binary representation for the J-type instruction
    s = k[-12:-1]
    s += k[0:9]

    if instruct[0] not in J:
        # Handle unrecognized instruction
        print(f"Unrecognized instruction: {instruct[0]}")
        return
    
    # Add opcode and register bits to the binary representation
    s += register_to_binary[instruct[1]]
    s += "1101111"

    # Append the binary representation to the output list
    list_output.append(s)

def type_U(instruct, list_output):
    numeric_value_str = instruct[2]
    k = decimal_to_20bit_twos_complement(int(numeric_value_str))    # Convert the numeric value to binary

    # Extract the bits from the binary representation for the U-type instruction
    s = k[0:20]

    if instruct[0] not in U:
        # Handle unrecognized instruction
        print(f"Unrecognized instruction: {instruct[0]}")
        return

    # Add opcode and register bits to the binary representation
    s += register_to_binary[instruct[1]]
    s += U[instruct[0]]

    # Append the binary representation to the output list
    list_output.append(s)









def type_S(instruct, list_output):
    k = decimal_to_12bit_binary(int(instruct[2]))
    s = k[:7]
    s += register_to_binary[instruct[1]]
    s += register_to_binary[instruct[3]]
    s += "010"
    s += k[7:]
    s += "0100011"
    list_output.append(s)
    








def type_B(instruct, list_output):
    numeric_value_str = instruct[3]
    k = decimal_to_12bit_binary(int(numeric_value_str))    # Convert the numeric value to binary
    s = k[:7]



    s += register_to_binary[instruct[2]]
    s += register_to_binary[instruct[1]]
    s += function3.get(instruct[0], "")
    s += k[7:]
    s += B[instruct[0]]


    # Append the binary representation to the output list
    list_output.append(s)












# def process_instruction(line):
#     # Split the line into components
#     components = line.split()

#     # Check if the instruction type is recognized
#     if components[0] in R:
#         instruction_type = "R"
#     elif components[0] in I:
#         instruction_type = "I"
#     elif components[0] in J:
#         instruction_type = "J"
#     elif components[0] in U:
#         instruction_type = "U"
#     elif components[0] in S:
#         instruction_type = "S"
#     elif components[0] in B:
#         instruction_type = "B"
#     else:
#         # Handle unrecognized instruction
#         print(f"Unrecognized instruction: {components[0]}")
#         return

#     # Print the original instruction
#     print(f"Original instruction: {line}")

#     # Check if there are enough elements in components
#     if len(components) < 3:
#         print(f"Insufficient components for instruction: {line}")
#         return

#     # Split the third element using commas
#     operands = components[2].split(',')

#     # Check if there are enough operands
#     if len(operands) < 3:
#         print(f"Insufficient operands for instruction: {line}")
#         return

#     components[2:] = operands

#     # Call the appropriate function based on the instruction type
#     if instruction_type == "R":
#         type_R(components, list_output)
#     elif instruction_type == "I":
#         type_I(components, list_output)
#     elif instruction_type == "J":
#         type_J(components, list_output)
#     elif instruction_type == "U":
#         type_U(components, list_output)
#     elif instruction_type == "S":
#         type_S(components, list_output)
#     elif instruction_type == "B":
#         type_B(components, list_output)




# # Open the file and read its contents
# with open("automatedTesting/tests/assembly/simpleBin/test1.txt", 'r') as f:
#     # Read lines from the file
#     v = f.readlines()
# # Process each line and append to list_output
# for i in range(len(v)):
#     line = v[i].strip()  # Remove leading/trailing whitespaces
#     process_instruction(line)

# # Print the binary representations in the list
# for binary_representation in list_output:
#     print(binary_representation)


