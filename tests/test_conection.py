import unittest

import sys
sys.path.append("../")
from config import mysql

class TestDbConnect(unittest.TestCase):

  def test_success_connect(self):
    conn = mysql.connect()
  
if __name__ == '__main__':
  unittest.main()