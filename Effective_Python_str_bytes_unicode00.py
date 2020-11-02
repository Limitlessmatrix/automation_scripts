#Written in Python 3
#list of short cuts and scripts covered in Effective Python

#helper functions converting strings and unicode

def to_str(bytes_or_str):
    if isinstance(bytes_or_str, bytes):
        value = bytes_or_str.decode('utf-8')
    else:
        value = bytes_or_str
    return value #instance of str

#helper function that takes string, or bytes and returns bytes
def to_bytes(bytes_or_str):
    if isinstance(bytes_or_str, str):
        value = bytes_or_str.encode('utf-8')
    else:
        value = bytes_or_str
    return vlaue #instance of bytes

with open('random.bin', 'wb') as f:
    f.write(os.urandom(10))
