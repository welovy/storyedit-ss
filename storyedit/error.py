#!/usr/bin/python
# -*- coding: utf-8 -*-


_errstrs = [
'Success',
'Invalid User Error',
'Invalid Request Command Error'
'Invalid Story Error'
];

class SEError(object):
	__slots__ = ['errno', 'errstr', 'detail'];

	def __init__(self, errno=0):
		self.errno = errno;
		self.errstr = '';
		self.detail = _errstrs[errno];

	def __eq__ (self, obj):
		if self.errno == obj.errno:
			return True;
		else:
			return False;

	def setDetail(self, msg = ""):
		if msg != "":
			self.detail = msg;
		else:
			self.detail = _errstrs[self.errno];
		
	def getDetail(self):
		return self.detail;

Success = SEError(0);
InvalidUserError = SEError(1);
InvalidRequestCommandError = SEError(2);
InvalidStoryError = SEError(3);
