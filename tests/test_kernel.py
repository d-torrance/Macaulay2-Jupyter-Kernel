import unittest
import jupyter_kernel_test


class M2KernelTests(jupyter_kernel_test.KernelTests):
    kernel_name = "m2"
    language_name = "Macaulay2"

    code_hello_world = '"hello, world!"'

if __name__ == "__main__":
    unittest.main()
