#!/bin/bash

echo "Testing compound commands with debug..."

# Use the debug lexer to see token flow
cp robot.l robot_backup.l
cp debug_robot.l robot.l

bison -d robot.y
flex robot.l
gcc robot.tab.c lex.yy.c -o robot -lfl

echo "=== Testing: Robot could you move 2 blocks ahead and turn 180 degrees ==="
echo "Robot could you move 2 blocks ahead and turn 180 degrees" | ./robot

echo ""
echo "=== Testing: Could you move 1 blocks ahead, then turn 270 degrees ==="  
echo "Could you move 1 blocks ahead, then turn 270 degrees" | ./robot

# Restore original lexer
cp robot_backup.l robot.l
rm robot_backup.l