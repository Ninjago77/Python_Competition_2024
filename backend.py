from string import ascii_lowercase,ascii_uppercase # built-in library
ascii_letters = ascii_lowercase+ascii_uppercase

def backwardify(text:str) -> str:
    return text[::-1]

def pairwise(iterable):
    a = iter(iterable)
    return zip(a, a)

def Reverse_Cipher(text:str) -> str:
    return backwardify(text)

Atbash_Mapping_Table = str.maketrans(
    ascii_letters,
    backwardify(ascii_lowercase)+backwardify(ascii_uppercase)
)
def Atbash_Cipher(text:str) -> str:
    return text.translate(Atbash_Mapping_Table)

Caesar_Mapping_Tables = [
    str.maketrans(
        ascii_letters,
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

Affine_Multiplier_Options = [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25] # 26 coprimes
def Affine_Cipher(text:str,multiplier:int,shifts:int,decrypt:bool=False):
    if multiplier not in Affine_Multiplier_Options:
        raise ValueError("Nah bro, must be in ["+", ".join([str(n) for n in Affine_Multiplier_Options])+"]")
    if decrypt: inverse_multiplier = next(i for i in range(1, 26) if (multiplier * i) % 26 == 1)
    func = (lambda index:
        ((inverse_multiplier)*(index-shifts))%26
    ) if decrypt else (lambda index:
        ((multiplier*index)+shifts)%26
    )
    available_chars = "".join(list(filter(lambda letter: letter in ascii_letters, set(text))))
    return text.translate(str.maketrans(available_chars,"".join([   
        ascii_lowercase[func(ascii_lowercase_indexes[char])]
            if char in ascii_lowercase else 
        ascii_uppercase[func(ascii_uppercase_indexes[char])]
            if char in ascii_uppercase else 
        char for char in available_chars
    ])))

Bifid_J_to_I_Mapping_Table = str.maketrans("jJ","iI")
Bifid_Table = {
    11:"A",12:"B",13:"C",14:"D",15:"E",
    21:"F",22:"G",23:"H",24:"I",25:"K",
    31:"L",32:"M",33:"N",34:"O",35:"P",
    41:"Q",42:"R",43:"S",44:"T",45:"U",
    51:"V",52:"W",53:"X",54:"Y",55:"Z",
}
Inverse_Bifid_Table = {v: str(k) for k, v in Bifid_Table.items()}
def Bifid_Cipher(text:str,decrypt:bool=False):
    text = text.translate(Bifid_J_to_I_Mapping_Table)
    if decrypt:
        allblocks = [item for sublist in [
            (int(Inverse_Bifid_Table[char][0]),int(Inverse_Bifid_Table[char][1]))
            for char in text.upper()
            if char in ascii_uppercase
        ] for item in sublist]
        rows, columns = allblocks[:len(allblocks)//2], allblocks[len(allblocks)//2:]
    else:
        rows = []
        columns = []
        for char in text.upper():
            if char in ascii_uppercase:
                rows.append(int(Inverse_Bifid_Table[char][0]))
                columns.append(int(Inverse_Bifid_Table[char][1]))
    val = zip(rows,columns) if decrypt else pairwise(rows+columns)
    letters = [Bifid_Table[(r*10)+c] for r,c in val]
    return "".join([
        letters.pop(0).lower()
            if char in ascii_lowercase else
        letters.pop(0)
            if char in ascii_uppercase else
        char for char in text
        ])