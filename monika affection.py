import pymem

def get_user_input():
    try:
        change_value = float(input("Enter how much affection u want: "))
        return change_value
    except ValueError:
        print("please enter a number.")
        return get_user_input()

def float_to_unsigned(value):
    if value < 0:
        return int(value + 2**32)
    return int(value)

def change_affection_value(pm, addresses, value):
    for address in addresses:
        pm.write_int(address, value)

def main():
    change_value = get_user_input()
    unsigned_value = float_to_unsigned(change_value)

    addresses = [
        0x02B48AD8, 0x0318C134, 0x0690CCB4, 0x0728B470, 0x072AAF44, 0x07D1DFBC,
        0x07D45664, 0x07F55CD0, 0x07F5A38C, 0x07F6DFF4, 0x07F7C35C, 0x083AA108,
        0x083C3BE8, 0x08C0AE88, 0x08E05E28, 0x09104ED4, 0x0C53DC18, 0x0F8B6424,
        0x245BB234, 0x245BB4B8, 0x260183EC, 0x2DD46428, 0x35A46358, 0x35A4636C,
        0x35A46380, 0x35A46394, 0x35A463A8, 0x35A463BC
    ]

    try:
        pm = pymem.Pymem('DDLC.exe')

        for address in addresses:
            pm.write_int(address, unsigned_value)

        print("Changed affection successfully.")
    except pymem.exception.ProcessNotFound:
        print("Process DDLC.exe was not found.")
    except Exception as e:
        print(f"Error (please report to the developer: {e}")

if __name__ == "__main__":
    main()
