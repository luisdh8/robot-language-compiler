from cpu import run_cpu_from_file

def test_cpu():
    test_file = "instructions.asm"
    try:
        run_cpu_from_file(test_file)
        print("Test completed successfully.")
    except Exception as e:
        print(f"Test failed: {e}")

if __name__ == "__main__":
    test_cpu()
