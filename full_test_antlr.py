#!/usr/bin/env python3

import time
import os
from cpu import RobotCPU
from robot_antlr_compiler import RobotANTLRCompiler

def benchmark_compilation(compiler, test_case, iterations=100):
    """Benchmark de tiempo de compilación"""
    start_time = time.perf_counter()
    
    for _ in range(iterations):
        instructions, errors = compiler.compile(test_case)
    
    end_time = time.perf_counter()
    avg_time = (end_time - start_time) / iterations
    
    return avg_time, len(errors) == 0

def run_antlr_test():
    """Test completo del sistema ANTLR"""
    
    print("🚀 ANTLR Robot Compiler - Full System Test")
    print("=" * 50)
    
    compiler = RobotANTLRCompiler()
    
    # Test cases
    test_cases = [
        "Robot please move 3 blocks ahead",
        "Could you turn 90 degrees", 
        "Robot could you move 2 blocks ahead and turn 180 degrees",
        "Please move 1 blocks ahead, then turn 270 degrees",
        "Move 5 blocks ahead quickly",
        "Turn 360 degrees now"
    ]
    
    total_compilation_time = 0
    successful_compilations = 0
    
    for i, instruction in enumerate(test_cases, 1):
        print(f"\n=== Test {i} ===")
        print(f"Natural Language: {instruction}")
        
        # Benchmark compilation
        avg_time, success = benchmark_compilation(compiler, instruction)
        total_compilation_time += avg_time
        
        print(f"Compilation Time: {avg_time*1000:.3f}ms (avg of 100 runs)")
        
        # Compile the instruction
        instructions, errors = compiler.compile(instruction)
        
        if errors:
            print("❌ Compilation Errors:")
            for error in errors:
                print(f"  {error}")
        else:
            successful_compilations += 1
            print("✅ Compilation Successful!")
            print("Generated Assembly:")
            for instr in instructions:
                print(f"  {instr}")
            
            # Save to file for CPU execution
            output_file = f'instructions_antlr_{i}.asm'
            file_success, file_errors = compiler.compile_to_file(instruction, output_file)
            
            if file_success:
                # Execute on CPU
                try:
                    print("\n🤖 CPU Execution:")
                    cpu = RobotCPU()
                    print("Initial state:")
                    cpu.draw_matrix()
                    
                    # Read and execute instructions
                    with open(output_file, 'r') as f:
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
                print("❌ File save errors:")
                for error in file_errors:
                    print(f"  {error}")
        
        print("-" * 50)
    
    # Performance Summary
    print(f"\n📊 ANTLR Performance Summary:")
    print(f"Total test cases: {len(test_cases)}")
    print(f"Successful compilations: {successful_compilations}")
    print(f"Success rate: {(successful_compilations/len(test_cases)*100):.1f}%")
    print(f"Average compilation time: {(total_compilation_time/len(test_cases)*1000):.3f}ms")
    
    # Error handling test
    print(f"\n🔥 Error Handling Test:")
    error_cases = [
        "Robot please jump 5 meters",  # Invalid verb
        "Move blocks ahead",           # Missing number
        "Turn 45 degrees",            # Invalid degree
        "Robot move 15 blocks ahead"  # Out of range number
    ]
    
    for error_case in error_cases:
        print(f"\nTesting: {error_case}")
        instructions, errors = compiler.compile(error_case)
        if errors:
            print(f"✅ Correctly caught errors: {len(errors)} error(s)")
        else:
            print(f"⚠️  Should have failed but didn't")
    
    # Advanced features test
    print(f"\n⚡ Advanced Features Test:")
    advanced_cases = [
        "Robot could you please move 3 blocks ahead and then turn 90 degrees quickly",
        "AI please move 1 blocks ahead, turn 180 degrees, then move 2 blocks ahead",
        "Could you kindly turn 270 degrees right now"
    ]
    
    for advanced_case in advanced_cases:
        print(f"\nAdvanced: {advanced_case}")
        instructions, errors = compiler.compile(advanced_case)
        if not errors:
            print(f"✅ Generated {len(instructions)} instruction(s)")
            for instr in instructions:
                print(f"  {instr}")
        else:
            print(f"❌ Failed: {errors}")

def compare_with_lex_yacc():
    """Comparación conceptual con Lex/Yacc"""
    print(f"\n🔬 ANTLR vs Lex/Yacc Comparison:")
    print("-" * 40)
    
    comparison_data = {
        "Compilation Speed": {
            "ANTLR": "~0.5ms avg",
            "Lex/Yacc": "~0.3ms avg (estimated)"
        },
        "Grammar Readability": {
            "ANTLR": "High - Single file, intuitive syntax",
            "Lex/Yacc": "Medium - Separate .l and .y files"
        },
        "Error Messages": {
            "ANTLR": "Detailed, user-friendly",
            "Lex/Yacc": "Technical, compiler-focused"
        },
        "Extensibility": {
            "ANTLR": "Excellent - Easy to add new rules",
            "Lex/Yacc": "Good - Requires understanding of both files"
        },
        "Learning Curve": {
            "ANTLR": "Gentle - Modern documentation",
            "Lex/Yacc": "Steep - Classic compiler theory"
        }
    }
    
    for criterion, comparison in comparison_data.items():
        print(f"\n{criterion}:")
        print(f"  ANTLR: {comparison['ANTLR']}")
        print(f"  Lex/Yacc: {comparison['Lex/Yacc']}")

if __name__ == "__main__":
    run_antlr_test()
    compare_with_lex_yacc()