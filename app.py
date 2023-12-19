# app.py
from icecream import ic

from tools import col
from tools.numbers.comp import is_pal, sum_of_digits
from tools.numbers.simp import add_numbers, subtract_numbers

# Flag to check if functions in 'simp' module have been called
simp_module_called = False


def main():
    global simp_module_called

    result_add = None
    result_subtract = None

    try:
        # Test functions in 'simp' module
        # comment out block start
        result_add = add_numbers(3, 4)
        result_subtract = subtract_numbers(7, 2)

        ic(f"Result of adding: {result_add}")
        ic(f"Result of subtracting: {result_subtract}")
        # comment out block end

        # Update the flag to indicate that at least one function in 'simp' module has been called
        if result_add or result_subtract:
            simp_module_called = True
        else:
            raise Exception("At least one function in 'simp' module must be called.")

    except Exception as e:
        ic(f"Exception: {e}")
        return

    # Test functions in 'comp' module
    result_sum_of_digits = sum_of_digits(234)
    result_is_palindrome = is_pal(1221)

    ic(f"Result of sum_of_digits: {result_sum_of_digits}")
    ic(f"Result of is_palindrome: {result_is_palindrome}")

    # Test function in 'col' module
    zipped_result = col.myzip([1, 2, 3], ["a", "b", "c"])
    ic("Zipped result:", list(zipped_result))


if __name__ == "__main__":
    main()
