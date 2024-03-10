# registers binary code

register_to_binary = {
    "x0": "00000",
    "x1": "00001",
    "x2": "00010",
    "x3": "00011",
    "x4": "00100",
    "x5": "00101",
    "x6": "00110",
    "x7": "00111",
    "x8": "01000",
    "x9": "01001",
    "x10": "01010",
    "x11": "01011",
    "x12": "01100",
    "x13": "01101",
    "x14": "01110",
    "x15": "01111",
    "x16": "10000",
    "x17": "10001",
    "x18": "10010",
    "x19": "10011",
    "x20": "10100",
    "x21": "10101",
    "x22": "10110",
    "x23": "10111",
    "x24": "11000",
    "x25": "11001",
    "x26": "11010",
    "x27": "11011",
    "x28": "11100",
    "x29": "11101",
    "x30": "11110",
    "x31": "11111",
}



instruction_dict = {
    "ld": "00100",     # Load
    "st": "00101",     # Store
    "add": "00000",    # Add
    "sub": "00001",    # Subtract
    "mul": "00110",    # Multiply
    "xor": "01010",    # Exclusive OR
    "Or": "01011",     # Logical OR
    "And": "01100",    # Logical AND
    "movi": "00010",   # Move Immediate
    "rsi": "01000",    # Right Shift Immediate
    "lsi": "01001",    # Left Shift Immediate
    "mov": "00011",    # Move
    "div": "00111",    # Divide
    "Not": "01101",    # Logical NOT
    "com": "01110",    # Compare


    "lw": "0000011",    # Load word
    "addi": "0010011",  # Add immediate
    "sltiu": "0010011", # Set less than immediate unsigned
    "jalr": "1100111",  # Jump and link register


    "sw": "0100011",    # Store word


    "beq": "1100011",   # Branch if equal
    "bne": "1100011",   # Branch if not equal
    "blt": "1100011",   # Branch if less than
    "bge": "1100011",   # Branch if greater than or equal
    "bltu": "1100011",  # Branch if less than unsigned
    "bgeu": "1100011",  # Branch if greater than or equal unsigned


    "lui": "0110111",   # Load upper immediate
    "auipc": "0010111", # Add upper immediate to PC

    "jal": "1101111",   # Jump and link
    
}




def add(){



    
}




var = {}


register=['x0', 'x1', 'x2', 'x3', 'x4', 'x5', 'x6', 'x7', 'x8', 'x9', 'x10', 'x11', 'x12', 'x13', 'x14', 'x15', 'x16', 'x17', 'x18', 'x19', 'x20', 'x21', 'x22', 'x23', 'x24', 'x25', 'x26', 'x27', 'x28', 'x29', 'x30', 'x31']




