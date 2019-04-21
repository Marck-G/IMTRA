from Crypto.Cipher import AES


def aes_key():
    return '6pú2BÑq9pfI.Ú'


def api_key():
    suit = AES.new(key=aes_key())
    with open('api_key.k', "rb") as f:
        key = f.read()
        return suit.decrypt(key).decode('utf-8')


API_KEY = api_key()
