from Crypto.Cipher import AES
import base64


def xml2db():
    """
    Read data from xml and upload it to DB
    :return:
    """
    pass

def data2xml(data):
    pass


def crypt_string():
    pass

msg_text = 'test some plain text here'.rjust(32)
secret_key = '1234567890123456' # create new & store somewhere safe

cipher = AES.new(secret_key,AES.MODE_ECB) # never use ECB in strong systems obviously
encoded = base64.b64encode(cipher.encrypt(msg_text))
# ...
decoded = cipher.decrypt(base64.b64decode(encoded))
print decoded.strip()


from cryptography.fernet import Fernet
key = Fernet.generate_key()
cipher_suite = Fernet(key)
cipher_text = cipher_suite.encrypt(b"A really secret message. Not for prying eyes.")
plain_text = cipher_suite.decrypt(cipher_text)