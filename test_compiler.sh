#!/bin/bash

echo "Building robot compiler..."
bison -d robot.y
flex robot.l
gcc robot.tab.c lex.yy.c -o robot -lfl

if [ $? -eq 0 ]; then
    echo "✅ Compilation successful!"
    echo ""
    
    # Clear previous instructions
    > instructions.asm
    
    # Test cases
    echo "=== Testing valid commands ==="
    echo ""
    
    echo "Test 1: Simple move command"
    echo "Robot please move 3 blocks ahead" | ./robot
    echo "Generated:"
    cat instructions.asm
    echo ""
    
    echo "Test 2: Simple turn command"  
    echo "Please turn 90 degrees" | ./robot
    echo "Generated:"
    cat instructions.asm
    echo ""
    
    echo "Test 3: Compound command"
    echo "Robot could you move 2 blocks ahead and turn 180 degrees" | ./robot
    echo "Generated:"
    cat instructions.asm
    echo ""
    
    echo "Test 4: Another compound with comma"
    echo "Could you move 1 blocks ahead, then turn 270 degrees" | ./robot
    echo "Generated:"
    cat instructions.asm
    echo ""
    
    echo "=== Testing invalid commands ==="
    echo ""
    
    echo "Test 5: Missing courtesy (should fail)"
    echo "Robot move 3 blocks ahead" | ./robot
    echo ""
    
    echo "Test 6: Invalid direction (should fail)"
    echo "Robot please move 3 blocks right" | ./robot
    echo ""
    
    echo "Test 7: Invalid degree (should fail)"
    echo "Robot please turn 45 degrees" | ./robot
    echo ""
    
else
    echo "❌ Compilation failed!"
fi