from .tests import assert_decompiles


def test_simple_function():
    assert_decompiles('''
def func(a: int, b: int) -> float:
    pass
''', '''
cpdef float func(int a, int b):
    pass
''', mode='cython', do_check=False)


def test_no_return_type():
    assert_decompiles('''
def func(a: int, b: int):
    pass
''', '''
cpdef object func(int a, int b):
    pass
''', mode='cython', do_check=False)


def test_variable_annotations():
    assert_decompiles('''
def func():
    x: int = 0
    y: float
''', '''
cpdef object func():
    cdef int x = 0
    cdef float y
''', mode='cython', do_check=False)