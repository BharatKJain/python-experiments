import struct
import zlib

def compress_column(values):
    # Convert the column values to bytes
    column_data = struct.pack(f"{len(values)}I", *values)

    # Compress the column data using zlib compression
    compressed_data = zlib.compress(column_data)

    return compressed_data

def decompress_column(compressed_data):
    # Decompress the compressed data using zlib decompression
    column_data = zlib.decompress(compressed_data)

    # Unpack the column data into individual values
    values = struct.unpack(f"{len(column_data)//4}I", column_data)

    return values

def write_column_to_disk(column_name, values):
    # Compress the column values
    compressed_data = compress_column(values)

    # Write the compressed data to disk
    with open(f"{column_name}.bin", "wb") as file:
        file.write(compressed_data)

def read_column_from_disk(column_name):
    # Read the compressed data from disk
    with open(f"{column_name}.bin", "rb") as file:
        compressed_data = file.read()

    # Decompress the column values
    values = decompress_column(compressed_data)

    return values

# Example usage
column_name = "product_id"
column_values = [1, 2, 3, 4, 5]

# Write the column to disk
write_column_to_disk(column_name, column_values)

# Read the column from disk
read_values = read_column_from_disk(column_name)

# Verify the data
print(read_values)  # Output: (1, 2, 3, 4, 5)
