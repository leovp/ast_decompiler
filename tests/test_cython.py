from .tests import assert_decompiles


def test_simple_function():
    assert_decompiles('''
def func(a: int, b: int) -> float:
    pass
''', '''
cpdef func(a: int, b: int) -> float:
    pass
''', mode='cython', do_check=False)
