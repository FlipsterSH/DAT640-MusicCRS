import struct
from datetime import datetime

def convert_bytes_to_datetime(byte_tuple):
    # Unpack the bytes as a little-endian unsigned 64-bit integer
    year = struct.unpack('<Q', byte_tuple[0])[0]

    # Create a datetime object using the extracted year
    date = datetime(year=year, month=1, day=1)
    return date

def convert_bytes_to_year(byte_data):
    # Unpack the first two bytes as a little-endian unsigned short (year)
    year = struct.unpack('<H', byte_data[:2])[0]
    return year