#!/usr/bin/env python3

import sys
from antlr4 import *
from antlr4.error.ErrorListener import ErrorListener

# Estas clases se generarían automáticamente con ANTLR
# Para el propósito de demostración, simulamos la funcionalidad

class RobotLexer:
    """Simulación del lexer generado por ANTLR"""
    
    def __init__(self, input_stream):
        self.input = input_stream.lower()
        self.pos = 0
        self.tokens = []
        self._tokenize()
    
    def _tokenize(self):
        """Tokenización básica simulando ANTLR"""
        import re
        
        token_patterns = [
            ('NOUN', r'\b(robot|ai|thing)\b'),
            ('PRONOUN', r'\byou\b'),
            ('COURTESY', r'\b(could|would|should|please|kindly)\b'),
            ('MOVE_VERB', r'\bmove\b'),
            ('TURN_VERB', r'\bturn\b'),
            ('BLOCKS', r'\bblocks?\b'),
            ('DEGREES', r'\bdegrees?\b'),
            ('AHEAD', r'\bahead\b'),
            ('AND', r'\band\b'),
            ('THEN', r'\bthen\b'),
            ('COMMA', r','),
            ('ADVERBIAL', r'\b(right now|now|quickly|immediately)\b'),
            ('DEGREE', r'\b(90|180|270|360)\b'),
            ('NUMBER', r'\b\d+\b'),
            ('WS', r'[ \t]+'),
            ('EOL', r'\n'),
        ]
        
        combined_pattern = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in token_patterns)
        
        for match in re.finditer(combined_pattern, self.input):
            token_type = match.lastgroup
            token_value = match.group()
            
            if token_type != 'WS':  # Skip whitespace
                self.tokens.append((token_type, token_value))

class RobotParser:
    """Simulación del parser generado por ANTLR"""
    
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0
        self.instructions = []
        self.errors = []
    
    def parse(self):
        """Parse principal"""
        try:
            while self.pos < len(self.tokens):
                if self._current_token()[0] == 'EOL':
                    self.pos += 1
                    continue
                
                instruction = self._parse_instruction()
                if instruction:
                    self.instructions.extend(instruction)
                
        except Exception as e:
            self.errors.append(f"Parse error: {e}")
        
        return self.instructions, self.errors
    
    def _current_token(self):
        if self.pos >= len(self.tokens):
            return ('EOF', '')
        return self.tokens[self.pos]
    
    def _consume_token(self, expected_type=None):
        if self.pos >= len(self.tokens):
            return None
        
        token = self.tokens[self.pos]
        if expected_type and token[0] != expected_type:
            raise Exception(f"Expected {expected_type}, got {token[0]}")
        
        self.pos += 1
        return token
    
    def _parse_instruction(self):
        """Parse una instrucción completa"""
        instructions = []
        
        # Skip courtesy words
        while self._current_token()[0] in ['NOUN', 'PRONOUN', 'COURTESY']:
            self.pos += 1
        
        # Parse primera acción
        first_action = self._parse_action()
        if first_action:
            instructions.append(first_action)
        
        # Check for compound command
        if self._current_token()[0] in ['COMMA', 'AND', 'THEN']:
            # Skip connector
            if self._current_token()[0] == 'COMMA':
                self.pos += 1
            if self._current_token()[0] in ['AND', 'THEN']:
                self.pos += 1
            
            # Parse segunda acción
            second_action = self._parse_action()
            if second_action:
                instructions.append(second_action)
        
        return instructions
    
    def _parse_action(self):
        """Parse una acción individual (move o turn)"""
        token = self._current_token()
        
        if token[0] == 'MOVE_VERB':
            return self._parse_move()
        elif token[0] == 'TURN_VERB':
            return self._parse_turn()
        else:
            raise Exception(f"Expected MOVE_VERB or TURN_VERB, got {token[0]}")
    
    def _parse_move(self):
        """Parse comando de movimiento"""
        self._consume_token('MOVE_VERB')
        
        number_token = self._consume_token('NUMBER')
        if not number_token:
            raise Exception("Expected NUMBER after MOVE_VERB")
        
        self._consume_token('BLOCKS')  # Optional
        self._consume_token('AHEAD')   # Optional
        
        # Skip adverbials
        if self._current_token()[0] == 'ADVERBIAL':
            self.pos += 1
        
        return f"MOV,{number_token[1]}"
    
    def _parse_turn(self):
        """Parse comando de giro"""
        self._consume_token('TURN_VERB')
        
        degree_token = self._consume_token('DEGREE')
        if not degree_token:
            raise Exception("Expected DEGREE after TURN_VERB")
        
        self._consume_token('DEGREES')  # Optional
        
        # Skip adverbials
        if self._current_token()[0] == 'ADVERBIAL':
            self.pos += 1
        
        return f"TURN,{degree_token[1]}"

class CustomErrorListener(ErrorListener):
    """Manejo de errores personalizado"""
    
    def __init__(self):
        super().__init__()
        self.errors = []
    
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        self.errors.append(f"Line {line}:{column} - {msg}")

class RobotANTLRCompiler:
    """Compilador principal usando ANTLR (simulado)"""
    
    def __init__(self):
        self.error_listener = CustomErrorListener()
    
    def compile(self, input_text):
        """Compila texto a instrucciones de ensamblador"""
        try:
            # Crear lexer
            lexer = RobotLexer(input_text)
            
            # Crear parser
            parser = RobotParser(lexer.tokens)
            
            # Parse
            instructions, errors = parser.parse()
            
            if errors:
                return None, errors
            
            return instructions, []
            
        except Exception as e:
            return None, [f"Compilation error: {e}"]
    
    def compile_to_file(self, input_text, output_file):
        """Compila y guarda en archivo"""
        instructions, errors = self.compile(input_text)
        
        if errors:
            return False, errors
        
        try:
            with open(output_file, 'w') as f:
                f.write("# Generated by ANTLR Robot Compiler\n")
                for instruction in instructions:
                    f.write(f"{instruction}\n")
            
            return True, []
            
        except Exception as e:
            return False, [f"File write error: {e}"]

def main():
    """Función principal de prueba"""
    compiler = RobotANTLRCompiler()
    
    test_cases = [
        "Robot please move 3 blocks ahead",
        "Could you turn 90 degrees",
        "Robot could you move 2 blocks ahead and turn 180 degrees",
        "Please move 1 blocks ahead, then turn 270 degrees"
    ]
    
    print("🚀 ANTLR Robot Compiler Test")
    print("=" * 40)
    
    for i, test_case in enumerate(test_cases, 1):
        print(f"\nTest {i}: {test_case}")
        print("-" * 30)
        
        instructions, errors = compiler.compile(test_case)
        
        if errors:
            print("❌ Compilation Errors:")
            for error in errors:
                print(f"  {error}")
        else:
            print("✅ Compilation Successful!")
            print("Generated Instructions:")
            for instruction in instructions:
                print(f"  {instruction}")
        
        # Test file output
        success, file_errors = compiler.compile_to_file(test_case, f"test_{i}.asm")
        if success:
            print(f"✅ Saved to test_{i}.asm")
        else:
            print("❌ File save errors:")
            for error in file_errors:
                print(f"  {error}")

if __name__ == "__main__":
    main()