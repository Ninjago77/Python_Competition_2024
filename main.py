from backend import Reverse_Cipher, Atbash_Cipher, Caesar_Cipher, Vigenere_Cipher, Affine_Cipher, Bifid_Cipher, Affine_Multiplier_Options
import flet as ft

def main(page: ft.Page):
    global Cipher_Index,Display_Cipher,CipherControls,mobile
    mobile = page.width < page.height
    page.title = "Cipher Selector"
    Cipher_Index = 0
    Display_Cipher = ft.Container()
    def CMD(e):
        global CipherControls
        if Cipher_Index == 0:
            CipherControls[0].controls[3].value = Reverse_Cipher(CipherControls[0].controls[1].value)
        if Cipher_Index == 1:
            CipherControls[1].controls[3].value = Atbash_Cipher(CipherControls[1].controls[1].value)
        if Cipher_Index == 2:
            decrypt = CipherControls[2].controls[2].controls[1].value == "Decrypt"
            CipherControls[2].controls[3].value = Caesar_Cipher(
                CipherControls[2].controls[1].value,
                shifts=int(CipherControls[2].controls[2].controls[0].value)*int(-1 if decrypt else 1),
            )
        if Cipher_Index == 3:
            decrypt = CipherControls[3].controls[3].controls[1].value == "Decrypt"
            decrypt_key = bool(CipherControls[3].controls[3].controls[1].value)
            CipherControls[3].controls[5].value,key = Vigenere_Cipher(
                CipherControls[3].controls[1].value,
                key=CipherControls[3].controls[2].value,
                to_decrypt=decrypt,
                decryption_key=decrypt_key
            )
            CipherControls[3].controls[6].value = key
            CipherControls[3].controls[6].disabled = not CipherControls[3].controls[3].controls[1].value
        if Cipher_Index == 4:
            decrypt = CipherControls[4].controls[2].controls[2].value == "Decrypt"
            CipherControls[4].controls[4].value = Affine_Cipher(
                CipherControls[4].controls[1].value,
                multiplier=int(CipherControls[4].controls[2].controls[0].value),
                shifts=int(CipherControls[4].controls[2].controls[1].value),
                decrypt=decrypt,
            )
        if Cipher_Index == 5:
            decrypt = CipherControls[5].controls[3].controls[0].value == "Decrypt"
            CipherControls[5].controls[4].value = Bifid_Cipher(
                CipherControls[5].controls[2].value,
                decrypt=decrypt,
            )
        
        page.update()
    def vigenere_dec_key_change(e):
        global CipherControls
        CipherControls[3].controls[6].disabled = not e.control.value
        CipherControls[3].controls[6].update()
    CipherControls = [
        ft.Column(controls= [# Reverse
            ft.Text("Reverse Cipher",theme_style=ft.TextThemeStyle.DISPLAY_SMALL),
            ft.TextField(label="Input",multiline=True),
            ft.FloatingActionButton(text="Submit",on_click=CMD,width=300),
            ft.TextField(label="Output",read_only=True,multiline=True),
        ]),
        ft.Column(controls= [# Atbash
            ft.Text("Atbash Cipher",theme_style=ft.TextThemeStyle.DISPLAY_SMALL),
            ft.TextField(label="Input",multiline=True),
            ft.FloatingActionButton(text="Submit",on_click=CMD,width=300),
            ft.TextField(label="Output",read_only=True,multiline=True),
        ]),
        ft.Column(controls= [# Caesar
            ft.Text("Caesar Cipher",theme_style=ft.TextThemeStyle.DISPLAY_SMALL),
            ft.TextField(label="Input",multiline=True),
            ft.Row(controls=[
                ft.TextField(label="Shifts",input_filter=ft.NumbersOnlyInputFilter(),width=75),
                ft.Dropdown(width=100,value="Encrypt",options=[
                    ft.dropdown.Option("Encrypt"),
                    ft.dropdown.Option("Decrypt"),
                ],),
                ft.FloatingActionButton(text="Submit",on_click=CMD,width=100),
            ]),
            ft.TextField(label="Output",read_only=True,multiline=True),
        ]),
        ft.Column(controls= [# Vigenere
            ft.Text("Vigenere Cipher",theme_style=ft.TextThemeStyle.DISPLAY_SMALL),
            ft.TextField(label="Input",multiline=True),
            ft.TextField(label="Key",input_filter=ft.TextOnlyInputFilter()),
            ft.Row(controls=[
                ft.Switch(label="Decryption Key",value=False,width=175,on_change=vigenere_dec_key_change),
                ft.Dropdown(width=100,value="Encrypt",options=[
                    ft.dropdown.Option("Encrypt"),
                    ft.dropdown.Option("Decrypt"),
                ],),
            ]),
            ft.FloatingActionButton(text="Submit",on_click=CMD,width=300),
            ft.TextField(label="Output",read_only=True,multiline=True),
            ft.TextField(label="Decryption Key",disabled=True,read_only=True),
        ]),
        ft.Column(controls= [# Affine
            ft.Text("Affine Cipher",theme_style=ft.TextThemeStyle.DISPLAY_SMALL),
            ft.TextField(label="Input",multiline=True),
            ft.Row(controls=[
                ft.Dropdown(width=100,value="1",label="Multiplier",
                    options=[ft.dropdown.Option(str(op)) for op in Affine_Multiplier_Options],),
                ft.TextField(label="Shifts",input_filter=ft.NumbersOnlyInputFilter(),width=75),
                ft.Dropdown(width=100,value="Encrypt",options=[
                    ft.dropdown.Option("Encrypt"),
                    ft.dropdown.Option("Decrypt"),
                ],),
            ]),
            ft.FloatingActionButton(text="Submit",on_click=CMD,width=300),
            ft.TextField(label="Output",read_only=True,multiline=True),
        ]),
        ft.Column(controls= [# Bifid
            ft.Text("Bifid Cipher",theme_style=ft.TextThemeStyle.DISPLAY_SMALL),
            ft.Text('*The "J/j"s will get converted to "I/i"s.',theme_style=ft.TextThemeStyle.HEADLINE_SMALL),
            ft.TextField(label="Input",multiline=True),
            ft.Row(controls=[
                ft.Dropdown(width=100,value="Encrypt",options=[
                    ft.dropdown.Option("Encrypt"),
                    ft.dropdown.Option("Decrypt"),
                ],),
                ft.FloatingActionButton(text="Submit",on_click=CMD,width=175),
            ]),
            ft.TextField(label="Output",read_only=True,multiline=True),
        ]),
        ft.Column(controls= [# About
            ft.Text("About The App",theme_style=ft.TextThemeStyle.DISPLAY_SMALL),
            ft.Text("This Project was made by Shanvanth Arunmozhi & Dominic Koh for the 2024 Python Coding Challenge & its theme:- Ciphers!\n\n\n Mobile View Coming Soon!",width=300,theme_style=ft.TextThemeStyle.BODY_LARGE),
        ]),

    ]
    def nav_rail_switch(e):
        global Cipher_Index,Display_Cipher
        Cipher_Index = e.control.selected_index
        display_cipher_update()
    def display_cipher_update():
        global Cipher_Index,Display_Cipher
        Display_Cipher.content = CipherControls[Cipher_Index]
        page.update()
    display_cipher_update()
    page.appbar = ft.AppBar(
        title=ft.Text("Cipher Selector",color=ft.colors.ON_PRIMARY),
        bgcolor=ft.colors.PRIMARY,
    )
    page.add(
        ft.Row([
                ft.NavigationRail(
                    destinations=[
                        ft.NavigationRailDestination(
                            icon=ft.icons.KEYBOARD_ARROW_RIGHT_OUTLINED,
                            selected_icon=ft.icons.KEYBOARD_DOUBLE_ARROW_RIGHT_ROUNDED,
                            label_content=ft.Text("Reverse Cipher"),
                        ),
                        ft.NavigationRailDestination(
                            icon=ft.icons.KEYBOARD_ARROW_RIGHT_OUTLINED,
                            selected_icon=ft.icons.KEYBOARD_DOUBLE_ARROW_RIGHT_ROUNDED,
                            label_content=ft.Text("Atbash Cipher"),
                        ),
                        ft.NavigationRailDestination(
                            icon=ft.icons.KEYBOARD_ARROW_RIGHT_OUTLINED,
                            selected_icon=ft.icons.KEYBOARD_DOUBLE_ARROW_RIGHT_ROUNDED,
                            label_content=ft.Text("Caesar Cipher"),
                        ),
                        ft.NavigationRailDestination(
                            icon=ft.icons.KEYBOARD_ARROW_RIGHT_OUTLINED,
                            selected_icon=ft.icons.KEYBOARD_DOUBLE_ARROW_RIGHT_ROUNDED,
                            label_content=ft.Text("Vigenere Cipher"),
                        ),
                        ft.NavigationRailDestination(
                            icon=ft.icons.KEYBOARD_ARROW_RIGHT_OUTLINED,
                            selected_icon=ft.icons.KEYBOARD_DOUBLE_ARROW_RIGHT_ROUNDED,
                            label_content=ft.Text("Affine Cipher"),
                        ),
                        ft.NavigationRailDestination(
                            icon=ft.icons.KEYBOARD_ARROW_RIGHT_OUTLINED,
                            selected_icon=ft.icons.KEYBOARD_DOUBLE_ARROW_RIGHT_ROUNDED,
                            label_content=ft.Text("Bifid Cipher"),
                        ),
                        ft.NavigationRailDestination(
                            icon=ft.icons.INFO_OUTLINE_ROUNDED,
                            selected_icon=ft.icons.INFO_ROUNDED,
                            label_content=ft.Text("About"),
                        ),
                    ],
                    on_change= nav_rail_switch,
                ),
                ft.VerticalDivider(width=1),
                Display_Cipher,
            ],
            expand=True,
        )
    )

ft.app(target=main,web_renderer=ft.WebRenderer.HTML,view=ft.AppView.WEB_BROWSER)