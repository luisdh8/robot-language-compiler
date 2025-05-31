class RobotCPU:
    def __init__(self, grid_size=10):
        self.grid_size = grid_size
        self.x, self.y = grid_size // 2, grid_size // 2  # centro: (5,5)
        self.directions = ['N', 'E', 'S', 'W']
        self.direction_idx = 0  # N (norte)
        self.state = 'Q0'
        self.history = []

    def execute_instruction(self, instr):
        parts = instr.strip().lower().split(',')
        if len(parts) != 2:
            raise ValueError(f"Malformed instruction: {instr}")
        
        cmd, val = parts[0], parts[1]

        if cmd == 'mov' and val.isdigit() and 1 <= int(val) <= 9:
            if self.state in ['Q0', 'Q3', 'Q4']:
                self._move(int(val))
                self.state = 'Q3'
            else:
                raise ValueError(f"Unexpected MOV at state {self.state}")
        
        elif cmd == 'turn' and val in ['90', '180', '270', '360']:
            if self.state in ['Q0', 'Q3', 'Q4']:
                self._turn(int(val))
                self.state = 'Q4'
            else:
                raise ValueError(f"Unexpected TURN at state {self.state}")
        else:
            raise ValueError(f"Illegal instruction: {instr}")

    def _move(self, blocks):
        dx, dy = 0, 0
        direction = self.directions[self.direction_idx]
        if direction == 'N': dy = -1
        elif direction == 'S': dy = 1
        elif direction == 'E': dx = 1
        elif direction == 'W': dx = -1
        new_x = self.x + dx * blocks
        new_y = self.y + dy * blocks
        if not (0 <= new_x < self.grid_size and 0 <= new_y < self.grid_size):
            raise ValueError("Illegal move: out of bounds")
        self.x, self.y = new_x, new_y
        self.history.append((self.x, self.y))

    def _turn(self, angle):
        self.direction_idx = (self.direction_idx + (angle // 90)) % 4

    def try_accept(self):
        if self.state in ['Q3', 'Q4']:
            self.state = 'Q5'
        return self.state == 'Q5'

    def draw_matrix(self):
        grid = [['.' for _ in range(self.grid_size)] for _ in range(self.grid_size)]
        grid[self.y][self.x] = self.directions[self.direction_idx]
        print("\n".join(" ".join(row) for row in grid))
        print(f"Robot at ({self.x},{self.y}) facing {self.directions[self.direction_idx]}")
        print('-' * (2 * self.grid_size - 1))


def run_cpu_from_file(filepath):
    cpu = RobotCPU()
    print("Initial state:")
    cpu.draw_matrix()

    with open(filepath, 'r') as f:
        for line in f:
            line = line.strip()
            if line:
                print(f"Instruction: {line}")
                cpu.execute_instruction(line)
                cpu.draw_matrix()

    accepted = cpu.try_accept()
    print(f"Final state accepted? {accepted}")
