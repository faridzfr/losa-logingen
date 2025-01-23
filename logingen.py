#

from cryptography.hazmat.primitives.ciphers import Cipher, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.decrepit.ciphers.algorithms import SEED 

def encode15(plain_text, user_key, nation_type="KOREA", pad_length=8):
    iv = {
        "KOREA": b'\x38\xAA\xFF\x03\x04\x4E\x06\x36\x08\xDE\x0A\x7B\x13\x58\x0E\x01',
        "TAIWAN": b'\x39\xAB\xD7\x1F\x0E\x58\x07\x04\x30\x7A\x1E\x99\x27\x62\x40\x0A'
    }
    iv_bytes = iv[nation_type]

    if len(user_key) > 16 or len(plain_text) > 16:
        raise ValueError("Inputs exceed supported length (16 bytes).")

    padded_plain = plain_text.ljust(pad_length, '\x00').encode('utf-8')
    padded_key = user_key.ljust(16, '\x00').encode('utf-8')

    cipher = Cipher(SEED(padded_key), modes.CFB(iv_bytes), backend=default_backend())
    encryptor = cipher.encryptor()
    cipher_text = encryptor.update(padded_plain)

    return ''.join(f'{b:02x}' for b in cipher_text)

# Collect data
app_name = input("App name without extension(.exe) (default lostsaga): ") or "lostsaga"
local_version = input("local Version (default 119483910): ") or "119483910"
gameserver_id = input("gameserverID (default 38657991157952): ") or "38657991157952"
userencode = input("userencode (default 111111111111111): ") or "111111111111111"
userid = input("user id (default devk): ") or "devk"
agentencode = input("agentencode (default Y9h3Z3u1c0gQF55): ") or "Y9h3Z3u1c0gQF55"
real_ip = input("real ip (default 0.0.0.0): ") or "0.0.0.0"
local_ipv4 = input("local ipv4 (default 127.0.0.1): ") or "127.0.0.1"

# encode
encodefix = encode15(userencode, userencode, pad_length=8)
encidfix = encode15(userid, agentencode, pad_length=6)
encodeipfix = encode15(real_ip, local_ipv4, pad_length=6)
encip = encode15(local_ipv4, agentencode, pad_length=8)

# Login Command
final_command = (
    f"start {app_name}.exe EDEW3940FVDP4950,10,20,30,1,autoupgrade_info.ini,-1,0,1," +
    f"{local_version},?{encodefix}{encidfix}?0?{encodeipfix}{encip}?" +
    f"{gameserver_id}?2010,7,15,1?10201?"
)

print("\nGenerated Command:")
print(final_command)

# lostart.bat
with open("lostart.bat", "w") as bat_file:
    bat_file.write(final_command)
