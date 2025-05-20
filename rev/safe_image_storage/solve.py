example = '6465766700D285511F93AD43A5FCE0462AB3FB4A390008666C61672E706E670CA644C5'
example = bytes.fromhex(example)
print(example)

protocol = [
	example[0:4], # magic: "devg"
	bytes([example[4]]), # version
	example[5:21], # slice_16
	example[21:23], # fname_len: 8
	example[23:31], # fname: "flag.png"
	example[31:35], # checksum: hash_crc32_ChecksumIEEE
]

print(protocol)

from zlib import crc32

protocol = bytearray(b''.join(protocol[:-1]))
protocol[4] = 3
protocol += crc32(protocol).to_bytes(4, 'big')
print(example)
print(bytes(protocol))

print(protocol.hex())

from websocket import create_connection, WebSocket, ABNF

ws: WebSocket = create_connection("ws://safeimagestorage.challs.olicyber.it")
ws.send(protocol, opcode=ABNF.OPCODE_BINARY)

data = ws.recv()
with open('flag.png', 'wb') as f:
	f.write(data[4:])

ws.close()

# flag{s0M3_cRYpt0_D03s_n0T_hUrT}
