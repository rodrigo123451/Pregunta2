# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 22:12:15 2021

@author: USUARIO
"""
from pyswip import Prolog
prolog=Prolog()
prolog.assertz("padre(juan, maria)")
prolog.assertz("padre(pablo, juan)")
prolog.assertz("padre(pablo, marcela)")
prolog.assertz("padre(carlos, debora)")

list(prolog.query("padre(juan,X)"))==[{'X':'maria'},{'X':'juan'},{'X':'marcela'},{'X':'debora'}]
for elemento in prolog.query("padre(X, Y)"):
    print(elemento["X"],"es  padre de",elemento["Y"])