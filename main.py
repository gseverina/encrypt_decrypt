# This exercise should take no more than 45 minutes
#
# We want to be able to encrypt and decrypt messages.
# Original messages to be encrypted do not contain numbers.
# We encrypt by a simple protocol that is based on character mapping as shown below.
# Encryption and decryption happens by replacing vowels by numbers and viceversa
#
# example: codes = {'a': 1, 'e': 2, 'i': 3, 'o': 4, 'u': 5}
#
# Your tasks are:
#   - based on the criteria explained above, write a function that encrypt/decrypt messages.
#   - provide some tests to verify that the function works as expected.
#   - mention any assumption you make to solve the problem.
#
# examples of input/output:
# input = "t3s 3s 1 m2ss1g2."
# output = "this is a message."
#
# input = "another message here!"
# output = "1n4th2r m2ss1g2 h2r2!"


CODES_ENCRYPT = {'a': '1', 'e': '2', 'i': '3', 'o': '4', 'u': '5'}
CODES_DECRYPT = {'1': 'a', '2': 'e', '3': 'i', '4': 'o', '5': 'u'}
VOWELS = 'aeiou'
NUMBERS = '12345'


def __encrypt(message):
    for x in VOWELS:
        if x in message:
            message = message.replace(x, CODES_ENCRYPT[x])
    return message


def __decrypt(message):
    for x in NUMBERS:
        if x in message:
            message = message.replace(x, CODES_DECRYPT[x])
    return message


def encrypt_decrypt(message, encrypt=True):
    """
    Returns an encrypted/decrypted string

    Params:
    - message: String to encrypt/decrypt
    - encrypt: if True will encrypt the string, if False will decrypt the string

    Assumptions:
    - Vowels upper/lower case insensitive, this is: 'a' or 'A' will be '1'
    - If message is None will return None
    - If message is '' (empty string) return ''
    """
    if message is None:
        return None

    if encrypt:
        return __encrypt(message.lower())
    return __decrypt(message)


if __name__ == "__main__":
    # Tests:
    assert encrypt_decrypt("another message here!") == "1n4th2r m2ss1g2 h2r2!"
    assert encrypt_decrypt("1n4th2r m2ss1g2 h2r2!", False) == "another message here!"
    assert encrypt_decrypt("AnOthEr messagE here!") == "1n4th2r m2ss1g2 h2r2!"
    assert encrypt_decrypt("1n4th2r m2ss1g2 h2r2!", False) == "AnOthEr messagE here!".lower()
    assert encrypt_decrypt("th3s 3s 1 m2ss1g2.", False) == "this is a message."
    assert encrypt_decrypt('') == ''
    assert encrypt_decrypt('', False) == ''
    assert encrypt_decrypt(None) is None
    assert encrypt_decrypt(None, False) is None



