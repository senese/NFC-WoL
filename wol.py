import socket

ADDR =  ('192.168.0.1', 7)
header = b'\xFF\xFF\xFF\xFF\xFF\xFF'
mac = b'\xE0\xD5\x5E\x64\x1B\xEC'

magic_packet = bytearray()
magic_packet += header
for _ in range (15):
    magic_packet += mac


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(ADDR)
s.send(magic_packet)
