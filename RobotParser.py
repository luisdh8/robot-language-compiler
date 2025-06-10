# Generated from Robot.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,19,86,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,1,0,1,0,1,0,1,0,5,0,19,8,0,10,0,12,0,22,9,0,1,0,3,0,25,8,0,5,0,
        27,8,0,10,0,12,0,30,9,0,1,0,1,0,1,1,1,1,3,1,36,8,1,1,2,3,2,39,8,
        2,1,2,1,2,1,2,3,2,44,8,2,1,2,3,2,47,8,2,1,2,3,2,50,8,2,1,3,3,3,53,
        8,3,1,3,1,3,1,3,3,3,58,8,3,1,3,3,3,61,8,3,1,4,4,4,64,8,4,11,4,12,
        4,65,1,5,1,5,1,6,3,6,71,8,6,1,6,1,6,1,6,3,6,76,8,6,1,6,1,6,3,6,80,
        8,6,1,6,1,6,3,6,84,8,6,1,6,0,0,7,0,2,4,6,8,10,12,0,3,1,0,6,7,1,0,
        8,9,1,0,1,3,96,0,28,1,0,0,0,2,35,1,0,0,0,4,38,1,0,0,0,6,52,1,0,0,
        0,8,63,1,0,0,0,10,67,1,0,0,0,12,83,1,0,0,0,14,20,3,2,1,0,15,16,3,
        12,6,0,16,17,3,2,1,0,17,19,1,0,0,0,18,15,1,0,0,0,19,22,1,0,0,0,20,
        18,1,0,0,0,20,21,1,0,0,0,21,24,1,0,0,0,22,20,1,0,0,0,23,25,5,18,
        0,0,24,23,1,0,0,0,24,25,1,0,0,0,25,27,1,0,0,0,26,14,1,0,0,0,27,30,
        1,0,0,0,28,26,1,0,0,0,28,29,1,0,0,0,29,31,1,0,0,0,30,28,1,0,0,0,
        31,32,5,0,0,1,32,1,1,0,0,0,33,36,3,4,2,0,34,36,3,6,3,0,35,33,1,0,
        0,0,35,34,1,0,0,0,36,3,1,0,0,0,37,39,3,8,4,0,38,37,1,0,0,0,38,39,
        1,0,0,0,39,40,1,0,0,0,40,41,5,4,0,0,41,43,5,16,0,0,42,44,7,0,0,0,
        43,42,1,0,0,0,43,44,1,0,0,0,44,46,1,0,0,0,45,47,5,10,0,0,46,45,1,
        0,0,0,46,47,1,0,0,0,47,49,1,0,0,0,48,50,3,10,5,0,49,48,1,0,0,0,49,
        50,1,0,0,0,50,5,1,0,0,0,51,53,3,8,4,0,52,51,1,0,0,0,52,53,1,0,0,
        0,53,54,1,0,0,0,54,55,5,5,0,0,55,57,5,15,0,0,56,58,7,1,0,0,57,56,
        1,0,0,0,57,58,1,0,0,0,58,60,1,0,0,0,59,61,3,10,5,0,60,59,1,0,0,0,
        60,61,1,0,0,0,61,7,1,0,0,0,62,64,7,2,0,0,63,62,1,0,0,0,64,65,1,0,
        0,0,65,63,1,0,0,0,65,66,1,0,0,0,66,9,1,0,0,0,67,68,5,14,0,0,68,11,
        1,0,0,0,69,71,5,13,0,0,70,69,1,0,0,0,70,71,1,0,0,0,71,72,1,0,0,0,
        72,73,5,11,0,0,73,84,5,12,0,0,74,76,5,13,0,0,75,74,1,0,0,0,75,76,
        1,0,0,0,76,77,1,0,0,0,77,84,5,11,0,0,78,80,5,13,0,0,79,78,1,0,0,
        0,79,80,1,0,0,0,80,81,1,0,0,0,81,84,5,12,0,0,82,84,5,13,0,0,83,70,
        1,0,0,0,83,75,1,0,0,0,83,79,1,0,0,0,83,82,1,0,0,0,84,13,1,0,0,0,
        16,20,24,28,35,38,43,46,49,52,57,60,65,70,75,79,83
    ]

class RobotParser ( Parser ):

    grammarFileName = "Robot.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "','" ]

    symbolicNames = [ "<INVALID>", "NOUN", "PRONOUN", "COURTESY", "MOVE_VERB", 
                      "TURN_VERB", "BLOCKS", "BLOCK", "DEGREES", "DEGREEWORD", 
                      "AHEAD", "AND", "THEN", "COMMA", "ADVERBIAL", "DEGREE", 
                      "NUMBER", "WS", "EOL", "ERROR_CHAR" ]

    RULE_program = 0
    RULE_polite_command = 1
    RULE_polite_move = 2
    RULE_polite_turn = 3
    RULE_courtesy_opener = 4
    RULE_adverbial = 5
    RULE_connector = 6

    ruleNames =  [ "program", "polite_command", "polite_move", "polite_turn", 
                   "courtesy_opener", "adverbial", "connector" ]

    EOF = Token.EOF
    NOUN=1
    PRONOUN=2
    COURTESY=3
    MOVE_VERB=4
    TURN_VERB=5
    BLOCKS=6
    BLOCK=7
    DEGREES=8
    DEGREEWORD=9
    AHEAD=10
    AND=11
    THEN=12
    COMMA=13
    ADVERBIAL=14
    DEGREE=15
    NUMBER=16
    WS=17
    EOL=18
    ERROR_CHAR=19

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(RobotParser.EOF, 0)

        def polite_command(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RobotParser.Polite_commandContext)
            else:
                return self.getTypedRuleContext(RobotParser.Polite_commandContext,i)


        def connector(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RobotParser.ConnectorContext)
            else:
                return self.getTypedRuleContext(RobotParser.ConnectorContext,i)


        def EOL(self, i:int=None):
            if i is None:
                return self.getTokens(RobotParser.EOL)
            else:
                return self.getToken(RobotParser.EOL, i)

        def getRuleIndex(self):
            return RobotParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)




    def program(self):

        localctx = RobotParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 28
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 62) != 0):
                self.state = 14
                self.polite_command()
                self.state = 20
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 14336) != 0):
                    self.state = 15
                    self.connector()
                    self.state = 16
                    self.polite_command()
                    self.state = 22
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 24
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==18:
                    self.state = 23
                    self.match(RobotParser.EOL)


                self.state = 30
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 31
            self.match(RobotParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Polite_commandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def polite_move(self):
            return self.getTypedRuleContext(RobotParser.Polite_moveContext,0)


        def polite_turn(self):
            return self.getTypedRuleContext(RobotParser.Polite_turnContext,0)


        def getRuleIndex(self):
            return RobotParser.RULE_polite_command

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPolite_command" ):
                listener.enterPolite_command(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPolite_command" ):
                listener.exitPolite_command(self)




    def polite_command(self):

        localctx = RobotParser.Polite_commandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_polite_command)
        try:
            self.state = 35
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 33
                self.polite_move()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 34
                self.polite_turn()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Polite_moveContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MOVE_VERB(self):
            return self.getToken(RobotParser.MOVE_VERB, 0)

        def NUMBER(self):
            return self.getToken(RobotParser.NUMBER, 0)

        def courtesy_opener(self):
            return self.getTypedRuleContext(RobotParser.Courtesy_openerContext,0)


        def AHEAD(self):
            return self.getToken(RobotParser.AHEAD, 0)

        def adverbial(self):
            return self.getTypedRuleContext(RobotParser.AdverbialContext,0)


        def BLOCKS(self):
            return self.getToken(RobotParser.BLOCKS, 0)

        def BLOCK(self):
            return self.getToken(RobotParser.BLOCK, 0)

        def getRuleIndex(self):
            return RobotParser.RULE_polite_move

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPolite_move" ):
                listener.enterPolite_move(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPolite_move" ):
                listener.exitPolite_move(self)




    def polite_move(self):

        localctx = RobotParser.Polite_moveContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_polite_move)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 38
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 14) != 0):
                self.state = 37
                self.courtesy_opener()


            self.state = 40
            self.match(RobotParser.MOVE_VERB)
            self.state = 41
            self.match(RobotParser.NUMBER)
            self.state = 43
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==6 or _la==7:
                self.state = 42
                _la = self._input.LA(1)
                if not(_la==6 or _la==7):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()


            self.state = 46
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==10:
                self.state = 45
                self.match(RobotParser.AHEAD)


            self.state = 49
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==14:
                self.state = 48
                self.adverbial()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Polite_turnContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TURN_VERB(self):
            return self.getToken(RobotParser.TURN_VERB, 0)

        def DEGREE(self):
            return self.getToken(RobotParser.DEGREE, 0)

        def courtesy_opener(self):
            return self.getTypedRuleContext(RobotParser.Courtesy_openerContext,0)


        def adverbial(self):
            return self.getTypedRuleContext(RobotParser.AdverbialContext,0)


        def DEGREES(self):
            return self.getToken(RobotParser.DEGREES, 0)

        def DEGREEWORD(self):
            return self.getToken(RobotParser.DEGREEWORD, 0)

        def getRuleIndex(self):
            return RobotParser.RULE_polite_turn

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPolite_turn" ):
                listener.enterPolite_turn(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPolite_turn" ):
                listener.exitPolite_turn(self)




    def polite_turn(self):

        localctx = RobotParser.Polite_turnContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_polite_turn)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 52
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 14) != 0):
                self.state = 51
                self.courtesy_opener()


            self.state = 54
            self.match(RobotParser.TURN_VERB)
            self.state = 55
            self.match(RobotParser.DEGREE)
            self.state = 57
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==8 or _la==9:
                self.state = 56
                _la = self._input.LA(1)
                if not(_la==8 or _la==9):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()


            self.state = 60
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==14:
                self.state = 59
                self.adverbial()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Courtesy_openerContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOUN(self, i:int=None):
            if i is None:
                return self.getTokens(RobotParser.NOUN)
            else:
                return self.getToken(RobotParser.NOUN, i)

        def PRONOUN(self, i:int=None):
            if i is None:
                return self.getTokens(RobotParser.PRONOUN)
            else:
                return self.getToken(RobotParser.PRONOUN, i)

        def COURTESY(self, i:int=None):
            if i is None:
                return self.getTokens(RobotParser.COURTESY)
            else:
                return self.getToken(RobotParser.COURTESY, i)

        def getRuleIndex(self):
            return RobotParser.RULE_courtesy_opener

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCourtesy_opener" ):
                listener.enterCourtesy_opener(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCourtesy_opener" ):
                listener.exitCourtesy_opener(self)




    def courtesy_opener(self):

        localctx = RobotParser.Courtesy_openerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_courtesy_opener)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 63 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 62
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 14) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 65 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 14) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AdverbialContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ADVERBIAL(self):
            return self.getToken(RobotParser.ADVERBIAL, 0)

        def getRuleIndex(self):
            return RobotParser.RULE_adverbial

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAdverbial" ):
                listener.enterAdverbial(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAdverbial" ):
                listener.exitAdverbial(self)




    def adverbial(self):

        localctx = RobotParser.AdverbialContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_adverbial)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 67
            self.match(RobotParser.ADVERBIAL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConnectorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return RobotParser.RULE_connector

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class CommaConnectorContext(ConnectorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RobotParser.ConnectorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def COMMA(self):
            return self.getToken(RobotParser.COMMA, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCommaConnector" ):
                listener.enterCommaConnector(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCommaConnector" ):
                listener.exitCommaConnector(self)


    class AndConnectorContext(ConnectorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RobotParser.ConnectorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def AND(self):
            return self.getToken(RobotParser.AND, 0)
        def COMMA(self):
            return self.getToken(RobotParser.COMMA, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAndConnector" ):
                listener.enterAndConnector(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAndConnector" ):
                listener.exitAndConnector(self)


    class AndThenConnectorContext(ConnectorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RobotParser.ConnectorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def AND(self):
            return self.getToken(RobotParser.AND, 0)
        def THEN(self):
            return self.getToken(RobotParser.THEN, 0)
        def COMMA(self):
            return self.getToken(RobotParser.COMMA, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAndThenConnector" ):
                listener.enterAndThenConnector(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAndThenConnector" ):
                listener.exitAndThenConnector(self)


    class ThenConnectorContext(ConnectorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RobotParser.ConnectorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def THEN(self):
            return self.getToken(RobotParser.THEN, 0)
        def COMMA(self):
            return self.getToken(RobotParser.COMMA, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterThenConnector" ):
                listener.enterThenConnector(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitThenConnector" ):
                listener.exitThenConnector(self)



    def connector(self):

        localctx = RobotParser.ConnectorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_connector)
        self._la = 0 # Token type
        try:
            self.state = 83
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                localctx = RobotParser.AndThenConnectorContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 70
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==13:
                    self.state = 69
                    self.match(RobotParser.COMMA)


                self.state = 72
                self.match(RobotParser.AND)
                self.state = 73
                self.match(RobotParser.THEN)
                pass

            elif la_ == 2:
                localctx = RobotParser.AndConnectorContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 75
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==13:
                    self.state = 74
                    self.match(RobotParser.COMMA)


                self.state = 77
                self.match(RobotParser.AND)
                pass

            elif la_ == 3:
                localctx = RobotParser.ThenConnectorContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 79
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==13:
                    self.state = 78
                    self.match(RobotParser.COMMA)


                self.state = 81
                self.match(RobotParser.THEN)
                pass

            elif la_ == 4:
                localctx = RobotParser.CommaConnectorContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 82
                self.match(RobotParser.COMMA)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





