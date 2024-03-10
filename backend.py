from string import ascii_lowercase,ascii_uppercase # built-in library


def backwardify(text:str) -> str:
    return text[::-1]

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

ascii_lowercase_indexes = {char: index for index, char in enumerate(ascii_lowercase)}
ascii_uppercase_indexes = {char: index for index, char in enumerate(ascii_uppercase)}

def Vigenere_Cipher(text:str,key:str,to_decrypt:bool=False,decryption_key:bool=False) -> tuple[str,str|None]:
    key = "".join(filter(lambda letter: letter in ascii_uppercase, key.upper()))
    if to_decrypt or decryption_key:
        Reverse_Mapping_Dict = {char: ascii_uppercase[-i % 26] for i, char in enumerate(ascii_uppercase)}
        rev = "".join(Reverse_Mapping_Dict.get(r, r) for r in key)
        if to_decrypt: key = rev
    key = (key*((len(text)//len(key))+1))[:len(text)]
    return "".join([char.translate(Caesar_Mapping_Tables[ascii_uppercase_indexes[k]])
        for char,k in zip(text,key)]),(rev if decryption_key else None)

Multiplier_Options = [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25] # 26 coprimes
def Affine_Cipher(text:str,multiplier:int,shifts:int,decrypt:bool=False):
    if multiplier not in Multiplier_Options:
        raise ValueError(f"Nah bro, must be in {", ".join([str(n) for n in Multiplier_Options])}")
    if decrypt: inverse_multiplier = next(i for i in range(1, 26) if (multiplier * i) % 26 == 1)
    func = (lambda index:
        ((inverse_multiplier)*(index-shifts))%26
    ) if decrypt else (lambda index:
        ((multiplier*index)+shifts)%26
    )
    return "".join([
        ascii_lowercase[func(ascii_lowercase_indexes[char])]
            if char in ascii_lowercase else 
        ascii_uppercase[func(ascii_uppercase_indexes[char])]
            if char in ascii_uppercase else 
        char for char in text]
    )

# # # print(Vigenere_Cipher("ndkjieidMONNWKNWKEy 372187{}~';/;./;'/","azyxwv",False,True))
# # print(Vigenere_Cipher("nemmmjieORRSWLPZOJy 372187{}~';/;./;'/","AZYXWV",False,True))
# print(Affine_Cipher("hdsjaiaodfDDEE",11,4,False))
# print(Affine_Cipher("dluzeoeclhLLWW",11,4,True))