#!/usr/bin/python
# -*- coding: utf-8 -*-
blob = """
           ��q(�%��m�ܨ.+�����Z��p>=�+���=(S���G���1+������V�������	���d�5nt$�^l/����_]EAt��n����:z}�k�c��GG4TK���"""
from hashlib import sha256
print sha256(blob).hexdigest()
