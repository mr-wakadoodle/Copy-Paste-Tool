import pyperclip
# pyperclip.copy("Any String entered here will be copied on clipboard and can be pasted using Ctrl+v anywhere :), for example - suchh as this string")
# You can also input an string you want to copy in the clipboard
x = input("Enter String: ")
pyperclip.copy(x)
pyperclip.paste()
