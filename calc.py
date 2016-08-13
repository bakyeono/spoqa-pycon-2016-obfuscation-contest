from sys import argv as star_star_argv
from re import compile as oh_my_eyes


class visit_my_blog:
    """http://bakyeono.net"""

    net = {}
    let = lambda _, o__: bytes(oo_ ^ b'o_o_oo__'[_oo % 8] for _oo, oo_ in enumerate(o__))
    car = lambda _, _o_: _.let(_o_.encode())
    cdr = lambda _, __o: _.let(__o).decode()

    def __init__(_):
        _.net.update({
            _.cdr(b'\x0c3\x005\x1a\x1d:'):
                oh_my_eyes(_.cdr(b'1\x03\x1cuG4\x03t\x13r2`43q\x03\x0b\x02Dv3\x1cu{')),
            _.cdr(b'\x0c0\x022\x00\x01\x7f3\x06,\x1f'):
                oh_my_eyes(_.cdr(b'G\x043t\x13B\x02`4\x03A\x03\x0b2tv3,E\x03D3,uG\x043t\x13B\x02`4\x03A\x03\x0b2tv')),
            _.cdr(b'\x1c<\x07:\x02\n'):
                oh_my_eyes(_.cdr(b'G\x043t\x13B\x02`4\x03A\x03\x0b2tv3,E\x03B3,uG\x043t\x13B\x02`4\x03A\x03\x0b2tv')),
            _.cdr(b'\x0c'):
                oh_my_eyes(_.cdr(b'G\x043t\x13B\x02`4\x03A\x03\x0b2tv3,E\x03E3,uG\x043t\x13B\x02`4\x03A\x03\x0b2tv')),
            _.cdr(b'\x0ctD'):
                oh_my_eyes(_.cdr(b'G\x043t\x13B\x02`4\x03A\x03\x0b2tv3,Ep3\x1cuw4\x03D#B2`\x043q3;2Dv')),
            _.cdr(b'\x1d'):
                oh_my_eyes(_.cdr(b'3,E\x03GGquF\x03F\x03\x1cE')),
            _.cdr(b'\x1f&\x1b7\x00\x01'):
                lambda o___, ___o: o___.__add__(___o),
            _.cdr(b'\x0b5\x0e1\x08\x00'):
                lambda _o__, __o_: _o__.__sub__(__o_),
            _.cdr(b'\n3\x0e,\x1b\x06<,\n>\x1d<\x07'):
                lambda __o_, _o__: __o_.__mul__(_o__),
            _.cdr(b'\x05>\x19>\x1c\x0c-6\x1f+'):
                lambda ___o, o___: ___o.__truediv__(o___),
        })


bakyeono = visit_my_blog()

def reduce(__):
    _ = bakyeono.net['clojure'].match(__)
    if _:
        return _.group(1)
    _ = bakyeono.net['r'].search(__)
    if _:
        return reduce(bakyeono.net['r']
                      .sub(reduce(_.group(1)),
                           __))
    _ = bakyeono.net['c'].search(__)
    if _:
        return reduce(bakyeono.net['c']
                      .sub(reduce(str(bakyeono.net['elasticsearch'](float(_.group(1)),
                                                                    float(_.group(2))))),
                           __))
    _ = bakyeono.net['c++'].search(__)
    if _:
        return reduce(bakyeono.net['c++']
                      .sub(reduce(str(bakyeono.net['javascript'](float(_.group(1)),
                                                                 float(_.group(2))))),
                           __))
    _ = bakyeono.net['common lisp'].search(__)
    if _:
        return reduce(bakyeono.net['common lisp']
                      .sub(reduce(str(bakyeono.net['python'](float(_.group(1)),
                                                             float(_.group(2))))),
                           __))
    _ = bakyeono.net['scheme'].search(__)
    if _:
        return reduce(bakyeono.net['scheme']
                      .sub(reduce(str(bakyeono.net['django'](float(_.group(1)),
                                                             float(_.group(2))))),
                           __))

    exit(42)

try:
    _ = float(reduce(star_star_argv[1]))
    if _.is_integer():
        print(str(int(_)))
    else:
        print(str(_))
except Exception:
    exit(42)

