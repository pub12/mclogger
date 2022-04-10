import unittest
import os

import sys
sys.path.insert(0, '../')


from mclogger.mclogger import MCLogger

filename = 'temp/test_log.txt'
if os.path.exists(filename): os.remove( filename )
logger = MCLogger(filename)

class TestLogger(unittest.TestCase):
	def __init__(self, arg):
		super().__init__(arg)
		self.logger = logger

	# ########################################################
	# def create_logger(self):
	# 	self.logger = logger
	# 	# return logger

	########################################################
	def test_create_logger(self):
		# logger = self.create_logger()

		self.logger.debug("hello world - debug")
		self.logger.info("hello world - info")
		self.logger.error("hello world - error")
		self.logger.warning("hello world - warning")

		self.assertEqual( len( self.logger.read_log_file()  ), 4)

	########################################################
	# @MCLogger.logfunc_cls()
	@MCLogger.logfunc_cls('logger')
	def test_log_func(self):
		print("AA")
		# self.logger = self.create_logger()
		# breakpoint()
		@logger.logfunc_loc
		def func_name(arg1, arg2):
			print( f"add: {arg1 + arg2}"  )

		print("start")
		func_name(10,15)
		print("end")

if __name__ == '__main__':
    unittest.main()