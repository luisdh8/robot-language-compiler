#!/usr/bin/env python3

import subprocess
import os
from cpu import RobotCPU

def compile_instruction(instruction):
    """Compile a natural language instruction to assembly"""
    try:
        # Use echo to pipe the instruction to the compiler
        result = subprocess.run(
            ['echo', instruction], 
            stdout=subprocess.PIPE, 
            text=True
        )
        
        if result.returncode == 0:
            # Pipe the output to our robot compiler
            compile_result = subprocess.run(
                ['./robot'], 
                input=result.stdout,
                capture_output=True,
                text=True
            )
            
            if compile_result.returncode == 0:
                print(f"✅ Compiled: '{instruction}'")
                return True
            else:
                print(f"❌ Compilation failed: {compile_result.stderr}")
                return False
        else:
            print(f"❌ Echo failed: {result.stderr}")
            return False
            
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def run_full_test():
    """Test the complete pipeline: Natural Language -> Assembly -> CPU Execution"""
    
    # Build the compiler first
    print("Building compiler...")
    build_result = subprocess.run(['bison', '-d', 'robot.y'], capture_output=True)
    if build_result.returncode != 0:
        print("❌ Bison failed")
        return
        
    build_result = subprocess.run(['flex', 'robot.l'], capture_output=True)
    if build_result.returncode != 0:
        print("❌ Flex failed")
        return
        
    build_result = subprocess.run(['gcc', 'robot.tab.c', 'lex.yy.c', '-o', 'robot', '-lfl'], capture_output=True)
    if build_result.returncode != 0:
        print("❌ GCC failed")
        return
    
    print("✅ Compiler built successfully!")
    print()
    
    # Test cases
    test_cases = [
        "Robot please move 3 blocks ahead",
        "Could you turn 90 degrees", 
        "Robot could you move 2 blocks ahead and turn 180 degrees",
        "Please move 1 blocks ahead, then turn 270 degrees"
    ]
    
    for i, instruction in enumerate(test_cases, 1):
        print(f"=== Test {i} ===")
        print(f"Natural Language: {instruction}")
        
        # Clear previous instructions
        with open('instructions.asm', 'w') as f:
            f.write("")
        
        # Compile the instruction
        if compile_instruction(instruction):
            # Check if instructions.asm was generated
            if os.path.exists('instructions.asm') and os.path.getsize('instructions.asm') > 0:
                print("Generated Assembly:")
                with open('instructions.asm', 'r') as f:
                    assembly_content = f.read()
                    print(assembly_content)
                
                # Execute on CPU
                try:
                    print("CPU Execution:")
                    cpu = RobotCPU()
                    print("Initial state:")
                    cpu.draw_matrix()
                    
                    # Read and execute instructions
                    with open('instructions.asm', 'r') as f:
                        for line in f:
                            line = line.strip()
                            if line and not line.startswith('#'):
                                print(f"Executing: {line}")
                                cpu.execute_instruction(line)
                                cpu.draw_matrix()
                    
                    accepted = cpu.try_accept()
                    print(f"Final state accepted: {accepted}")
                    
                except Exception as e:
                    print(f"❌ CPU execution failed: {e}")
            else:
                print("❌ No assembly file generated")
        
        print("-" * 50)
        print()

if __name__ == "__main__":
    run_full_test()