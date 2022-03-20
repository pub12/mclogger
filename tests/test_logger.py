import unittest
import os

import sys
sys.path.insert(0, '../mclogger/')


from mclogger import MCLogger

class TestLogger(unittest.TestCase):

	def test_create_logger(self):
		filename = 'temp/test_log.txt'
		os.remove( filename )
		logger = MCLogger(filename).getLogger()

		logger.debug("hello world - debug")
		logger.info("hello world - info")
		logger.error("hello world - error")
		logger.warning("hello world - warning")

		with open(filename) as f:
			lines = f.readlines()

		self.assertEqual( len(lines), 4)


if __name__ == '__main__':
    unittest.main()