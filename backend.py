import itertools # built-in library
from string import ascii_lowercase,ascii_uppercase # built-in library


def backwardify(text:str) -> str:
    return text[::-1] # Uses string slicing

def Reverse_Cipher(text:str) -> str:
    return backwardify(text)

Atbash_Mapping_Table = str.maketrans(ascii_lowercase+ascii_uppercase,backwardify(ascii_lowercase)+backwardify(ascii_uppercase))
def Atbash_Cipher(text:str) -> str:
    return text.translate(Atbash_Mapping_Table)

Caesar_Mapping_Tables = [
    str.maketrans(
        ascii_lowercase+
        ascii_uppercase,
        ascii_lowercase[i:]+ascii_lowercase[:i]+
        ascii_uppercase[i:]+ascii_uppercase[:i])
    for i in range(26)]
def Caesar_Cipher(text: str, shifts: int):
    return text.translate(Caesar_Mapping_Tables[shifts%26])

def Vigenere_Cipher(text:str,key:str,to_decrypt:bool=False,decryption_key:bool=False) -> tuple[str,str|None]:
    key = "".join(list(itertools.filterfalse(lambda letter: letter not in ascii_uppercase,key.upper())))
    if to_decrypt or decryption_key:
        rev = "".join([ascii_uppercase[-ascii_uppercase.index(r) % 26] for r in key])
        if to_decrypt: key = rev
    key = key[:len(text)] if len(text) <= len(key) else str(key*((len(text)//len(key))+1))[:len(text)]
    return "".join([
        ascii_lowercase[(ascii_lowercase.index(letter)+ascii_uppercase.index(k)) % 26]
            if letter.islower() else
        ascii_uppercase[(ascii_uppercase.index(letter)+ascii_uppercase.index(k)) % 26]
            if letter.isupper() else
        letter 
        for letter,k in zip(text,key)]),(rev if decryption_key else None)

