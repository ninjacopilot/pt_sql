textos ="""This is a reST style.
:param param1: this is a first param
:param param2: this is a second param
:returns: this is a description of what is returned
:raises keyError: raises an exception
"""
list = [] 
lista = textos.split("\n")
for l in lista:
    print(l)
