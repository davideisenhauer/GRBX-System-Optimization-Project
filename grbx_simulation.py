import simpy
import random
import statistics

# Class representing the GRBX system simulation
class GRBXSimulation:
    def __init__(
        self,
        sim_time=480,
        arrival_rate_per_hour=20,
        service_min=0.75,
        service_max=1.25,
        capacity=1,
        seed=42
    ):
        self.sim_time = sim_time
        self.arrival_rate_per_hour = arrival_rate_per_hour
        self.arrival_rate_per_minute = arrival_rate_per_hour / 60
        self.service_min = service_min
        self.service_max = service_max
        self.capacity = capacity

        # To ensure consistent results
        random.seed(seed)

        # tracking
        self.wait_times = []
        self.system_times = []
        self.queue_lengths = []
        self.users_completed = 0
        self.busy_time = 0

    def user(self, env, system):
        arrival_time = env.now
        self.queue_lengths.append(len(system.queue))

        with system.request() as request:
            yield request

            wait_time = env.now - arrival_time
            self.wait_times.append(wait_time)

            service_time = random.uniform(self.service_min, self.service_max)

            start_service = env.now
            yield env.timeout(service_time)
            end_service = env.now

            self.busy_time += (end_service - start_service)

            total_time = env.now - arrival_time
            self.system_times.append(total_time)

            self.users_completed += 1

    # Generates users entering the system over time
    def arrivals(self, env, system):
        while True:
            env.process(self.user(env, system))
            interarrival = random.expovariate(self.arrival_rate_per_minute)
            yield env.timeout(interarrival)

    def run(self):
        env = simpy.Environment()
        system = simpy.Resource(env, capacity=self.capacity)

        env.process(self.arrivals(env, system))
        env.run(until=self.sim_time)

        utilization = self.busy_time / (self.sim_time * self.capacity)

        results = {
            "users_completed": self.users_completed,
            "avg_wait": statistics.mean(self.wait_times),
            "max_wait": max(self.wait_times),
            "avg_system_time": statistics.mean(self.system_times),
            "max_system_time": max(self.system_times),
            "avg_queue": statistics.mean(self.queue_lengths),
            "max_queue": max(self.queue_lengths),
            "utilization": utilization
        }

        return results

# Function to print simulation results in a clean format
def print_results(title, results):
    print(title)
    print("-" * 40)
    print(f"Users completed: {results['users_completed']}")
    print(f"Average wait time: {results['avg_wait']:.2f} minutes")
    print(f"Max wait time: {results['max_wait']:.2f} minutes")
    print(f"Average system time: {results['avg_system_time']:.2f} minutes")
    print(f"Max system time: {results['max_system_time']:.2f} minutes")
    print(f"Average queue length: {results['avg_queue']:.2f}")
    print(f"Max queue length: {results['max_queue']}")
    print(f"Utilization: {results['utilization']:.2f}")
    print()

# Main execution block
if __name__ == "__main__":

    # Scenario 1: Current/Baseline
    sim1 = GRBXSimulation(arrival_rate_per_hour=20, capacity=1)
    results1 = sim1.run()
    print_results("Scenario 1: Baseline Demand", results1)

    # Scenario 2: Higher Demand/Growth Estimates
    sim2 = GRBXSimulation(arrival_rate_per_hour=40, capacity=1)
    results2 = sim2.run()
    print_results("Scenario 2: Higher Demand", results2)

    # Scenario 3: Higher Demand + Increased Capacity
    sim3 = GRBXSimulation(arrival_rate_per_hour=40, capacity=2)
    results3 = sim3.run()
    print_results("Scenario 3: Increased Capacity", results3)
