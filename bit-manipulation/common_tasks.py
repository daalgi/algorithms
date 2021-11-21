"""
CRACKING THE CODING INTERVIEW
Chapter 5 - Bit Manipulation
"""


def get_bit(num: int, i: int) -> bool:
    return num & (1 << i) != 0


def set_bit(num: int, i: int) -> int:
    return num | (1 << i)


def clear_bit(num: int, i: int) -> int:
    mask = ~(1 << i)
    return num & mask


def clear_bit_msb_through_i(num: int, i: int) -> int:
    mask = (1 << i) - 1
    return num & mask


def clear_bits_i_through_0(num: int, i: int) -> int:
    mask = -1 << (i + 1)
    return num & mask


def update_bit(num: int, i: int, bit_is_1: int) -> int:
    value = 1 if bit_is_1 else 0
    mask = ~(1 << i)
    return (num & mask) | (value << i)


def pos_int_to_binary(num: int) -> str:
    res = []
    while num > 0:
        res.append(num & 1)
        num >>= 1
    if not res:
        return "0"
    return "".join(str(i) for i in res[::-1])


if __name__ == "__main__":
    num = 6
    binary_num = pos_int_to_binary(num)
    int_bin_str = f"{num} = {binary_num}"

    print("\n>> Get Bit:")
    print(int_bin_str)
    for i in range(4):
        print(f"get_bit({num}, {i}) =", get_bit(num, i))

    print("\n>> Set Bit:")
    print(int_bin_str)
    for i in range(4):
        print(f"set_bit({num}, {i}) =", set_bit(num, i))

    print("\n>> Clear Bit:")
    print(int_bin_str)
    for i in range(4):
        print(f"clear_bit({num}, {i}) =", clear_bit(num, i))

    print("\n>> Clear Bit (most significant bit through i, inclusive):")
    print(int_bin_str)
    for i in range(4):
        print(f"clear_bit_msb_through_i({num}, {i}) =", clear_bit_msb_through_i(num, i))

    print("\n>> Clear Bit (i through 0, inclusive):")
    print(int_bin_str)
    for i in range(4):
        print(f"clear_bits_i_through_0({num}, {i}) =", clear_bits_i_through_0(num, i))

    print("\n>> Update Bit:")
    print(int_bin_str)
    new_bit = 1
    for i in range(4):
        print(f"update_bit({num}, {i}, {new_bit}) =", update_bit(num, i, new_bit))

    print("\n>> Positive int to binary:")
    for i in range(9):
        print(f"pos_int_to_binary({i}) = {pos_int_to_binary(i):>4}")

    print()
