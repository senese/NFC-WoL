import socket

ADDR =  ('255.255.255.255', 9)
header = b'\xFF\xFF\xFF\xFF\xFF\xFF'
mac = b'\xE0\xD5\x5E\x64\x1B\xEC'

magic_packet = bytearray()
magic_packet += header
for _ in range (16):
    magic_packet += mac

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
s.connect(ADDR)
s.send(magic_packet)
