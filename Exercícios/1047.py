# -*- coding: utf-8 -*-

A, B, C, D = input().split(' ')
hi = int(A)
mi = int(B)
hf = int(C)
mf = int(D)
if hi == hf:
    if mi < mf:
        m = mf-mi
        h = 0
    if mi == mf:
        h = 24
        m = 0
    if mi > mf:
        m = (60 - mi) + mf
        h = 23
if hi > hf:
    h = (24 - hi) + hf
    if mi == mf:
        m = 0
    if mi > mf:
        m = (60 - mi) + mf
        h = h - 1
    if mi < mf:
        m = mf - mi
if hi < hf:
    h = hf - hi
    if mi == mf:
        m = 0
    if mi > mf:
        m = (60 - mi) + mf
        h = h - 1
    if mi < mf:
        m = mf - mi

print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format(h, m))