#!/usr/bin/python
#< ----------- Classes to represent propositions, e.g., "Socrates is a man." ----------- >
from enum import Enum
from BaseClasses import *

class PropTypes(Enum):
    SIMPLE = 0,
    COMPLEX = 1

class BasicProposition(Proposition):
    """ Represents an instance of a propsostion in propositional logic, specifically """

    def __invert__(self):
        """ Shortcut for converting a Proposition to a string.  So ~P == str(P) """
        return self.rawData
    def __neg__(self):
        """ Shortcut for negating a proposition, e.g., !"My favorite food is cake" ==
            "My favorite food is not cake"
        """
        from Operators import UnaryOperator as OP
        op = OP()
        cp = op.negate(self)
        return cp
    def __and__(self, value):
        """ Shortcut for conjoining two Propositions """
        from Operators import BinaryOperator as OP
        op = OP()
        cp = op.conjoin(self, value)
        return cp
    def __or__(self, value):
        """ Shortcut for disjoining (inclusive) two Propositions """
        from Operators import BinaryOperator as OP
        op = OP()
        cp = op.disjoin(self, value)
        return cp
    def __gt__(self, value):
        """ Shortcut for disjoin(negate(P), Q), where (P,Q) are Propositions """
        from Operators import BinaryOperator as OP
        op = OP()
        cp = op.imply(self, value)
        return cp
    def __add__(self, value):
        """ Shortcut for xor(P, Q), where (P,Q) are Propositioins """
        from Operators import BinaryOperator as OP
        op = OP()
        cp = op.xor(self, value)
        return cp
    def __iter__(self):
        """ Make all propositions iterable so they can be used in iterable manipulations """
        return self
    def __next__(self):
        """ Make all propositions iterable so they can be used in iterable manipulations,
            however each subclass needs to implement what "next" means when iterating *over* a
            proposition, rather than over a *list* of propositions
        """
        pass

    def getPropType(self):
        """  Conceptual Shortcut for typeOf(P), where P is an instantiation of a subclass of
             Proposition 
        """
        return self.propType
""" END CLASS"""
class SimpleProp(BasicProposition):
    """ Represents a single simple proposition in string form; e.g., "Pythons are snakes", which can
        be represented by a single symbol, e.g. P=="Pythons are snakes" 
    """
    propType = PropTypes.SIMPLE
""" END CLASS """
class ComplexProp(BasicProposition):
    """ Represents a single binary proposition, e.g., "2+2=4"=>"1+1=2" or "P OR Q", etc...
    """
    secondProp = ""
    operator = ""
    propType = PropTypes.COMPLEX
    """ Members: rawData is the first Proposition (of any type, including ComplexProp), and the
                   secondProp is similarly the first Proposition.  The operator is any supported
                   binary operater in propositional logic.
    """

    members = ['rawData', 'operator', 'secondProp']
    """ Class variables:  Shortcuts for processing instance information of this class """

    def __eq__(self, value):
        """ Defines P=>Q == P=>Q and P=>Q != Q=>P, etc...
        """
        props = [self, value]
        return all([[getattr(x, z) == getattr(y, z) for x, y in props] for z in self.members])
    def __str__(self):
        """ If (P,=>,Q) is a ComplexProp, then str((P,=>,Q)) == "P=>Q"
        """
        return self.rawData + self.operator + self.secondProp
    def __invert__(self):
        """ Need to override the base class' invert as just returning rawData doesn't properly 
            represent the string form of a ComplexProp
        """
        return str(self)
    def __init__(self, *args, **kwargs):
        """ Logic: ComplexProp(P,<op>,Q) needs to properly represent P <op> Q, and we also need
            to account for P or Q being a ComplexProp by using parentheses.
        """
        if(len(args) >= 3):
            self.rawData = args[0]
            self.operator= args[1]
            self.secondProp = args[2]
            from Operators import OpStrings
            operators = [op for op in OpStrings.opList]
            containsOp = any([x in self.rawData for x in operators])
            parenthesized = "(" == self.rawData.strip("~")[0]
            if(containsOp and not parenthesized):
                    self.rawData = "("+self.rawData+")"
            containsOp = any([x in self.secondProp for x in operators])
            parenthesized = "(" == self.secondProp.strip("~")[0]
            if(containsOp and not parenthesized):
                    self.secondProp = "("+self.secondProp+")"

"""END CLASS"""
