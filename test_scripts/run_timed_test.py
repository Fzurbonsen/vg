import subprocess
import sys
import time

def main():
    print("started: run_timed_test.py\n")

    if len(sys.argv) < 2:
        print("Usage: python time_binary.py <binary> [args...]")
        sys.exit(1)

    output_file = input("please input the input file (aln.gam): ")

    binary = sys.argv[1]
    args = sys.argv[2:]
    command = [binary] + args

    print(f"Running: {' '.join(command)}")

    start_time = time.perf_counter()

    try:
        with open(output_file, "wb") as f:
            subprocess.run(command, check=True, stdout=f, stderr=sys.stderr)
    except subprocess.CalledProcessError as e:
        print(f"Error: Command failed with exit code {e.returncode}")
        sys.exit(e.returncode)
    except FileNotFoundError:
        print(f"Error: Binary not found: {binary}")
        sys.exit(1)

    end_time = time.perf_counter()
    elapsed = end_time - start_time

    print(f"\nExecution time: {elapsed:.4f} seconds")

if __name__ == "__main__":
    main()