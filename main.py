# Standard Libraries
import sys
import traceback

# Custom Modules
from utils import file_utils
from core.sums_counter import SumsCounter


def stop():
    sys.exit(1)


def main():
    # Create necessary class objects
    sums_counter = SumsCounter()

    try:
        # Step #1: Loading 1M numbers from txt file
        loaded_unique_numbers = file_utils.load_unique_numbers_from_txt_file(file_path="files/input_1M_numbers.txt")

        # Step #2: Count unique sums & print result
        print(f"[INFO] Counting sums, it may take some time...")
        unique_sums = sums_counter.count(numbers=loaded_unique_numbers, min_sum=-1000, max_sum=1000)
        print(f"[INFO] Unique sums count: {unique_sums}")
    except KeyboardInterrupt:
        print("[ERROR] Failed: script interrupted by user (CTRL + C)")
        stop()
    except Exception as e:
        print(f"[ERROR] Failed: unexpected exception: {e}")
        traceback.print_exc()  # traceback included


if __name__ == '__main__':
    main()
