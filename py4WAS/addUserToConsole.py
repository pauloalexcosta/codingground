#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

# import sys and os
import sys, os, os.path

#testar user
iswas = os.getlogin()
if iswas is 'was':
        print('yep, user correcto')
else:
        print('nope, volta à casa de partida')

# Testar se sys.argv é string ou ficheiro
#userlist = sys.argv[1]
#print('userlist')
#if os.path.isfile(sys.argv[1]) == 'true':
#       print('é ficheiro')
#else:
#       print('é user')

userlist=sys.argv[1]
try:
   with open(userlist) as f: print("É ficheiro...")
except IOError as e:
   print("Erro: não é ficheiro")

