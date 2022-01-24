import unittest

from Utils.utils import conversion_Rib_to_compte

class Test(unittest.TestCase):

    def test_conversion_Rib_to_compte(self):
        self.assertEqual(conversion_Rib_to_compte("007780000115500030610689"),"000115S000306106")
        self.assertEqual(conversion_Rib_to_compte("0077800001155000306106899"),"000115S000306106")





if __name__ == '__main__':
    unittest.main()