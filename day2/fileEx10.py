import struct
packed = struct.pack('i', 256)
for b in packed:
    print(b)


unpacked = struct.unpack('i', packed)
print(unpacked)