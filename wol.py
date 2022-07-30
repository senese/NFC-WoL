import socket

header = b'\xFF\xFF\xFF\xFF\xFF\xFF'
mac = b'\xE0\xD5\x5E\x64\x1B\xEC'

magic_packet = bytearray()
magic_packet += header
print(magic_packet)
for _ in range (16):
    magic_packet += mac

s = socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect('192;168.0.1')
s.send(magic_packet)
