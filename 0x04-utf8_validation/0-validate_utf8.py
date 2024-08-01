#!/usr/bin/python3
"""UTF-8 validation module.
"""


def validUTF8(data):
    """
    Validates if a given data set represents a valid UTF-8 encoding.
    :param data: List of integers representing bytes of data.
    :return: True if data is valid UTF-8 encoding, else False.
    """

    # Number of bytes in the current UTF-8 character
    num_bytes = 0

    # Masks for checking leading bits
    mask1 = 1 << 7  # 10000000
    mask2 = 1 << 6  # 01000000

    for byte in data:
        # Mask to get the least significant 8 bits
        byte = byte & 0xFF

        if num_bytes == 0:
            # Determine number of bytes in this UTF-8 character
            mask = 1 << 7
            while mask & byte:
                num_bytes += 1
                mask >>= 1

            # 1-byte character
            if num_bytes == 0:
                continue

            # Invalid cases
            if num_bytes == 1 or num_bytes > 4:
                return False

        else:
            # Check that the byte starts with '10'
            if not (byte & mask1 and not (byte & mask2)):
                return False

        # Decrease the number of bytes remaining
        num_bytes -= 1

    # If we've used all bytes correctly, num_bytes should be 0
    return num_bytes == 0
