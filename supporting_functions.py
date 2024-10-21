import struct
from datetime import datetime

def convert_bytes_to_datetime(byte_tuple):
    # Unpack the bytes as a little-endian unsigned 64-bit integer
    year = struct.unpack('<Q', byte_tuple[0])[0]

    # Create a datetime object using the extracted year
    date = datetime(year=year, month=1, day=1)
    return date
