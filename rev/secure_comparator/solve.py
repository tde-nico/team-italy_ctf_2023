from Crypto.Cipher import ARC4

with open('checker.bin', 'rb') as f:
	data = f.read()

key_offset = 0x4700
key_length = 32 - 16
key = data[key_offset:key_offset + key_length]
# print(key.hex())

flag_offset = 0x47F0 + 16
flag_length = 80 - 16
flag = data[flag_offset:flag_offset + flag_length]
# print(flag.hex())

cipher = ARC4.new(key)
decrypted = cipher.decrypt(flag)
# print(decrypted.hex())
print(decrypted)

# flag{Why_is_rc4_so_common_in_rev?_Anyways_I_hope_you_had_fun}
