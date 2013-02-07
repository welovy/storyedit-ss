#!/usr/bin/python
# -*- coding: utf-8 -*-

import cgitb; cgitb.enable();

from storyedit.engine import *
from storyedit.debug import *

if __name__ == "__main__":
	engine = SEEngine();
	engine.setup();
	engine.process();
	engine.putresult();
	engine.close();

