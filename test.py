import json
from lark import Lark, Tree, Token
import time

def timing(func):
    def wrapper(*arg, **kw):
        t1 = time.time()
        res = func(*arg, **kw)
        t2 = time.time()
        print(func.__name__, 'took', t2 - t1, 's.')
        return res
    return wrapper

@timing
def Earley(grammar, string):
    parser = Lark(grammar, start='score')
    return parser.parse(string)

@timing
def LALR(grammar, string):
    parser = Lark(grammar, start='score', parser='lalr')
    return parser.parse(string)

def toList(tree: Tree or str):
    if type(tree) is str: return tree
    elif type(tree) is Token: return {
        "name": tree.type,
        "value": tree.value
    }
    else: return {
        "name": tree.data,
        "value": list(map(lambda x: toList(x), tree.children))
    }

with open("test.lark", "r") as f:
    grammer = f.read()
    res = Earley(grammer, """
        $T{4/4} $K{3#} $C{G8va+}
        C-   -    C4=C4_C4  C4 |
        Eb4_ Eb4_ Eb4  Eb4=Eb4_Eb4  3(Eb4_Eb4_Eb4) |||
    """)
    with open("test.tree", "w") as f:
        f.write(json.dumps(toList(res), indent="\t"))

# LALR()
