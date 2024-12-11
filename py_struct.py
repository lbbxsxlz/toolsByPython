import struct

class myStruct:
    def __init__(self, elem1, elem2, *args):
        if len(args) != 6:
            raise ValueError("Exactly 6 additional arguments are required")
        self.data = struct.pack('<2I6Q', elem1, elem2, *args) + b'\x00' * (256 - (2 * 4 + 6 * 8))

    def get_data(self):
        return self.data

def append_struct_to_file(struct_obj, filename):
    try:
        with open(filename, 'ab') as f:
            f.write(struct_obj.get_data())
        print(f"Struct data has been appended to {filename}.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Length 196352 / 16
custom_struct = myStruct(0x401000, 12272, 0, 0, 0, 0, 0, 0)

append_struct_to_file(custom_struct, 'custom_struct_data.bin')
