# Generated from Robot.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .RobotParser import RobotParser
else:
    from RobotParser import RobotParser

# This class defines a complete listener for a parse tree produced by RobotParser.
class RobotListener(ParseTreeListener):

    # Enter a parse tree produced by RobotParser#program.
    def enterProgram(self, ctx:RobotParser.ProgramContext):
        pass

    # Exit a parse tree produced by RobotParser#program.
    def exitProgram(self, ctx:RobotParser.ProgramContext):
        pass


    # Enter a parse tree produced by RobotParser#polite_command.
    def enterPolite_command(self, ctx:RobotParser.Polite_commandContext):
        pass

    # Exit a parse tree produced by RobotParser#polite_command.
    def exitPolite_command(self, ctx:RobotParser.Polite_commandContext):
        pass


    # Enter a parse tree produced by RobotParser#polite_move.
    def enterPolite_move(self, ctx:RobotParser.Polite_moveContext):
        pass

    # Exit a parse tree produced by RobotParser#polite_move.
    def exitPolite_move(self, ctx:RobotParser.Polite_moveContext):
        pass


    # Enter a parse tree produced by RobotParser#polite_turn.
    def enterPolite_turn(self, ctx:RobotParser.Polite_turnContext):
        pass

    # Exit a parse tree produced by RobotParser#polite_turn.
    def exitPolite_turn(self, ctx:RobotParser.Polite_turnContext):
        pass


    # Enter a parse tree produced by RobotParser#courtesy_opener.
    def enterCourtesy_opener(self, ctx:RobotParser.Courtesy_openerContext):
        pass

    # Exit a parse tree produced by RobotParser#courtesy_opener.
    def exitCourtesy_opener(self, ctx:RobotParser.Courtesy_openerContext):
        pass


    # Enter a parse tree produced by RobotParser#adverbial.
    def enterAdverbial(self, ctx:RobotParser.AdverbialContext):
        pass

    # Exit a parse tree produced by RobotParser#adverbial.
    def exitAdverbial(self, ctx:RobotParser.AdverbialContext):
        pass


    # Enter a parse tree produced by RobotParser#AndThenConnector.
    def enterAndThenConnector(self, ctx:RobotParser.AndThenConnectorContext):
        pass

    # Exit a parse tree produced by RobotParser#AndThenConnector.
    def exitAndThenConnector(self, ctx:RobotParser.AndThenConnectorContext):
        pass


    # Enter a parse tree produced by RobotParser#AndConnector.
    def enterAndConnector(self, ctx:RobotParser.AndConnectorContext):
        pass

    # Exit a parse tree produced by RobotParser#AndConnector.
    def exitAndConnector(self, ctx:RobotParser.AndConnectorContext):
        pass


    # Enter a parse tree produced by RobotParser#ThenConnector.
    def enterThenConnector(self, ctx:RobotParser.ThenConnectorContext):
        pass

    # Exit a parse tree produced by RobotParser#ThenConnector.
    def exitThenConnector(self, ctx:RobotParser.ThenConnectorContext):
        pass


    # Enter a parse tree produced by RobotParser#CommaConnector.
    def enterCommaConnector(self, ctx:RobotParser.CommaConnectorContext):
        pass

    # Exit a parse tree produced by RobotParser#CommaConnector.
    def exitCommaConnector(self, ctx:RobotParser.CommaConnectorContext):
        pass



del RobotParser