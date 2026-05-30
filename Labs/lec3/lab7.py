def generate_ddra_init_function():
    """
    Generates a C function `void DDRA_init(void)` for initializing the DDRA register
    of an ATmega32 microcontroller based on user input for each pin's mode.
    """
    ddra_value = 0
    print("Enter the mode for each pin of Port A (0 for Input, 1 for Output):")

    for i in range(8):
        while True:
            try:
                mode = int(input(f"Pin A{i} mode (0/1): "))
                if mode in [0, 1]:
                    if mode == 1:
                        ddra_value |= (1 << i)  # Set the bit for output
                    break
                else:
                    print("Invalid input. Please enter 0 or 1.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    c_code = []
    c_code.append("void DDRA_init(void)")
    c_code.append("{")
    c_code.append(f"    DDRA = 0b{ddra_value:08b};")
    c_code.append("}")

    print("\nGenerated C Code:")
    for line in c_code:
        print(line)

if __name__ == "__main__":
    generate_ddra_init_function()