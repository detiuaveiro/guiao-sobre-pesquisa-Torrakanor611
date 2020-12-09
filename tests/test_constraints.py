import pytest
import mapas
import amigos

def test_exercicio1_4():
    assert mapas.cs.search() == {'A': 'red', 'B': 'blue', 'C': 'red', 'D': 'blue', 'E': 'green'}

def test_exercicio1_5():
    assert amigos.cs.search() == {'Andre': ('Claudio', 'Bernardo'), 'Bernardo': ('Andre', 'Claudio'), 'Claudio': ('Bernardo', 'Andre')}

def test_exercicio2():
    assert amigos.cs.calls == 18