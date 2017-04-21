import functools

def tau(l,i):
    """
    The tau operator
    
    EXAMPLES::
    
        sage: l = (3,2,1,0)
        sage: tau(l, 1)
        (3, 2, 0, 1)     
    """
    pos = l.index(i)
    return l[:pos]+l[pos+1:]+(l[pos],)

def taui(i):
    return functools.partial(tau, i=i)

def monoid(n):
    P = Permutations(range(n)).map(tuple)
    F = FiniteSetMaps(P); F
    generators = [ F(taui(i)) for i in range(n) ]
    return F.submonoid(generators)
