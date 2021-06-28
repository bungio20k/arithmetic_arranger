# This entrypoint file to be used in development. Start by reading README.md
from arithmetic_arranger import arithmetic_arranger
from unittest import main


# print(arithmetic_arranger(["3 + 855", "3801 - 2", "45 + 43", "123 + 49"]))
# print("    3      3801      45      123\n+ 855    -    2    + 43    +  49\n-----    ------    ----    -----")
# Run unit tests automatically
main(module='test_module', exit=False)
