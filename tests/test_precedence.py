from tests import check


def test_Yield():
    check('def f(): yield')
    check('def f(): x = yield 3')
    check('def f(): return (yield 3)')
    check('def f(): (yield 3)[f] += 4')
    check('def f(): (yield 3)[(yield 4):(yield 5):] += yield 6')
    check('lambda x: (yield x)')
    check('def f(): (yield a), b')


def test_Tuple():
    check('def f(): return x, y')
    check('def f(): yield x, y')
    check('def f((a, b)): pass')
    check('lambda (a, b): None')
    check('[(1, 2)]')
    check('{(1, 2): (3, 4)}')
    check('[(a, b) for f in c, d]')
    check('(a, b) + 3')
    check('lambda x: (a, b)')
    check('x[(1, 2):(3, 4):(5, 6), (7, 8):]')
    check('()')
    check('x,')


def test_Lambda():
    check('lambda x: lambda y: x + y')
    check('lambda x: y if z else x')
    check('(lambda x: y) if z else x')


def test_IfExp():
    check('y if x else a, b')
    check('(yield y) if (yield x) else (yield a), b')
    check('y if x else z if a else b')
    check('y if x else (z if a else b)')
    check('(y if x else z) if a else b')
    check('y if (x if z else a) else b')


def test_BinOp():
    check('(a ** b) ** c')
    check('a ** b ** c')
    check('a ** (b ** c)')
    check('(a + b) * c')
    check('a + b + c')
    check('(a + b) + c')
    check('a + (b + c)')
    check('x * (a or b)')


def test_UnaryOp():
    check('not not x')
    check('-(not x)')
    check('not (-x)')
    check('(-1) ** x')
    check('-((-1)**x)')


def test_Call():
    check('f(a, b)')
    check('f((a, b))')
    check('(a, b)(a, b)')
    check('a.b(c, d)')
    check('f((yield a), b)')
    check('f(a, (yield b))')
