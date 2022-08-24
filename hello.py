#!/usr/bin/env python3
"""Hello World Multi Languages

Dependendo da lingua configurada no ambiente o programa exibe a mensagem 
correspondente.

Modo de uso:

Tenha a variavel LANG devidamente configurada

    export LANG=pt_BR

Execução:

    python3 hello.py
    ou
    ./hello.py
"""

#Metadados
__version__ = "0.0.1"
__author__ = "Nuno"
__license__ = "Unlicense"

import os

# Dunder = texto entre dois underlines
# Este é o meu primeiro programa de muitos

current_language = os.getenv("LANG", "en_US")[:5]

msg = "Hello World!"

if current_language == "pt_BR":
    msg = "Olá Mundo!"
elif current_language == "it_IT":
    msg = "Ciao, Mondo!"
elif current_language == "es_SP":
    msg = "Hola, Mundo!"
elif current_language == "fr_FR":
    msg = "Bonjour Monde!"   
   
print (msg)
