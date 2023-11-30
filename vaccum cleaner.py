import random

class VacuumAgent:
    def __init__(self, environment_size):
        self.environment_size = environment_size
        self.environment = [random.choice([0, 1]) for _ in range(environment_size)]
        self.position = random.randint(0, environment_size - 1)

    def perceive(self):
        return self.environment[self.position]

    def clean(self):
        self.environment[self.position] = 0

    def move_left(self):
        self.position = max(0, self.position - 1)

    def move_right(self):
        self.position = min(self.environment_size - 1, self.position + 1)

def simulate_vacuum_cleaner(agent, steps):
    print("Initial Environment:", agent.environment)

    for step in range(steps):
        perception = agent.perceive()
        print(f"Step {step + 1}: Position {agent.position + 1} - {perception}")

        if perception == 1:
            print("Cleaning...")
            agent.clean()

        # Move randomly left or right
        if random.choice([True, False]):
            agent.move_left()
        else:
            agent.move_right()

    print("Final Environment:", agent.environment)

if __name__ == "__main__":
    environment_size = 5  # Adjust the size of the environment as needed
    vacuum_agent = VacuumAgent(environment_size)
    simulation_steps = 10  # Number of steps to simulate

    simulate_vacuum_cleaner(vacuum_agent, simulation_steps)
