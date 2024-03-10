import itertools # built-in library
from string import ascii_lowercase,ascii_uppercase # built-in library


def backwardify(text:str) -> str:
    return text[::-1] # Uses string slicing

def Reverse_Cipher(text:str) -> str:
    return backwardify(text)

Atbash_Mapping_Table = str.maketrans(
    ascii_lowercase+ascii_uppercase,
    backwardify(ascii_lowercase)+backwardify(ascii_uppercase)
)
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
    key = "".join(filter(lambda letter: letter in ascii_uppercase, key.upper()))
    if to_decrypt or decryption_key:
        Reverse_Mapping_Dict = {char: ascii_uppercase[-i % 26] for i, char in enumerate(ascii_uppercase)}
        rev = "".join(Reverse_Mapping_Dict.get(r, r) for r in key)
        if to_decrypt: key = rev
    key = (key*((len(text)//len(key))+1))[:len(text)]
    return "".join([letter.translate(Caesar_Mapping_Tables[ascii_uppercase.index(k)])
        for letter,k in zip(text,key)]),(rev if decryption_key else None)