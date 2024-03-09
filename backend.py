import itertools # built-in libraries
from string import ascii_lowercase,ascii_uppercase # built-in libraries

def Reverse_Cipher(text:str) -> str:
    return "".join(list(reversed(text)))

ascii_lowercase_R = list(reversed(ascii_lowercase))
ascii_uppercase_R = list(reversed(ascii_uppercase))
def Atbash_Cipher(text:str) -> str:
    return "".join([
        ascii_lowercase_R[ascii_lowercase.index(letter)]
            if letter in ascii_lowercase else
        ascii_uppercase_R[ascii_uppercase.index(letter)]
            if letter in ascii_uppercase else
        letter 
        for letter in text])

def Caeser_Cipher(text:str,shifts:int) -> str:
    shifts = shifts % 26
    return "".join([
        ascii_lowercase[(ascii_lowercase.index(letter)+shifts) % 26]
            if letter in ascii_lowercase else
        ascii_uppercase[(ascii_uppercase.index(letter)+shifts) % 26]
            if letter in ascii_uppercase else
        letter 
        for letter in text])

def Vigenere_Cipher(text:str,key:str,to_decrypt:bool=False,decryption_key:bool=False) -> tuple[str,str|None]:
    key = "".join(list(itertools.filterfalse(lambda letter: letter not in ascii_uppercase,key.upper())))
    if to_decrypt or decryption_key:
        rev = "".join([ascii_uppercase[-ascii_uppercase.index(r) % 26] for r in key])
        if to_decrypt: key = rev
    key = key[:len(text)] if len(text) <= len(key) else str(key*((len(text)//len(key))+1))[:len(text)]
    return "".join([
        ascii_lowercase[(ascii_lowercase.index(letter)+ascii_uppercase.index(k)) % 26]
            if letter in ascii_lowercase else
        ascii_uppercase[(ascii_uppercase.index(letter)+ascii_uppercase.index(k)) % 26]
            if letter in ascii_uppercase else
        letter 
        for letter,k in zip(text,key)]),(rev if decryption_key else None)

