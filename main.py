# Standard Libraries
import sys
import traceback

# Custom Libraries
from utils import file_utils


def stop():
    sys.exit(1)


def main():
    try:
        # Step #1: Loading 1M numbers from txt file
        loaded_unique_numbers = file_utils.load_unique_numbers_from_txt_file(file_path="files/input_1M_numbers.txt")

        # Step #2: Count unique sums
        ...
    except KeyboardInterrupt:
        print("[ERROR] Failed: script interrupted by user (CTRL + C)")
        stop()
    except Exception as e:
        print(f"[ERROR] Failed: unexpected exception: {e}")
        traceback.print_exc()  # traceback included


if __name__ == '__main__':
    main()
