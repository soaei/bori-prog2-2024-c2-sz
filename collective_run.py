import time
from pathlib import Path

from single_run import RUNDIR, main

SIZES = [
    (10_000, 50),
    (50_000, 200),
    (250_000, 500),
    (1_000_000, 1000),
    (10_000_000, 1000),
    (100_000_000, 10_000),
]

BASIS = "solution-1"
MAX_TIME = 3


class Runner:
    def __init__(self) -> None:
        self.solutions = [
            s.name
            for s in Path(".").iterdir()
            if s.is_dir()
            and s.name not in [".git", ".github", "__pycache__", RUNDIR, BASIS]
        ]
        self.valid_solutions = []
        self.seed = int(time.time() * 100000) // 17

    def validate(self):
        main(BASIS, 1000, 20, seed=self.seed)
        for s in self.solutions:
            try:
                main(s, 1000, 20, comparison=BASIS, seed=self.seed)
                self.valid_solutions.append(s)
            except Exception as e:
                print(f"failed {s}", e)

    def run(self):
        remaining = set(self.solutions)
        for in_size, q_size in SIZES:
            for s in self.valid_solutions:
                if s not in remaining:
                    continue
                try:
                    times = main(s, in_size, q_size, seed=self.seed)
                except Exception as e:
                    print(f"{s} failed with {e}")
                    continue
                if float(times[-1]) > MAX_TIME:
                    remaining.remove(s)


if __name__ == "__main__":
    runner = Runner()
    runner.validate()
    runner.run()
