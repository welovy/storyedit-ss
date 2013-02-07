
__all__ = ["D"];

import inspect;

DEBUG=False;

def _debug(msg) :
	fr = inspect.currentframe();
	try:
		fr = fr.f_back;
		if fr is None:
			print "[nocaller]" + msg;
		fi = inspect.getframeinfo(fr, 0);
		if fi[2] =='<module>':
			print "[%s:%d]" % (fi[0], fi[1]) + msg;
		else:
			print "[%s() [%s:%d]" % (fi[2], fi[0], fi[1]) + msg;
	finally:
		del fr;

if DEBUG is True:
	D = _debug;
else:
	D = lambda message: message;


