import json;
from storyedit.debug import *;
from storyedit.error import *;

class Response(object):
	__slots__ = ['isSuccess', 'response', 'requestedCommand', 'diagnosis'];

	def __init__(self):
		self.isSuccess = False;
		self.response = {};
		self.requestedCommand = '';
		self.diagnosis = '';

	def setRequestedCommand(self, command):
		self.requestedCommand = command;

	def setSuccess(self):
		self.isSuccess = True;

	def setFailed(self, status):
		self.isSuccess = False;
		self.diagnosis = status.getDetail();

	def prepareSysmsg(self):
		if self.isSuccess == True:
			self.response['success'] = 'true';
			if self.requestedCommand == "save":
				self.response['sysmsg'] = "your document has saved successfully";
			elif self.requestedCommand == "login":
				self.response['sysmsg'] = "welcome %s";
		else:
			self.response['success'] = 'false';
			if self.requestedCommand == "save":
				self.response['sysmsg'] = "Sorry, your document hasn't saved";
				self.response['diagnosis'] = self.diagnosis;
			elif self.requestedCommand == "login":
				self.response['sysmsg'] = "loging failed";
				self.response['diagnosis'] = self.diagnosis;
			else:
				# just print error status
				self.response['sysmsg'] = 'Sorry, error occurs, details shown in diagnosis message';
				self.response['diagnosis'] = self.diagnosis;

	def printHTTP(self):
		# output html with header
		print "Content-type: application/json; charset=utf-8";
		print
		print json.dumps(self.response, indent=1);
		print

	def setKeyValue(self, key, value):
		self.response[key] = value;


class Request(object):
	__slots__ = ['requestData', 'error'];
	def __init__(self):
		self.requestData = {};
		self.error = None;

	def setKeyValue(self, key, value):
		self.requestData[key] = value;

	def isError(self):
		if self.error != None:
			return True;
		else:
			return False;

	def getError(self):
		## TODO: object check
		## isError(self.error) needed
		return self.error;

	def getCommand(self):
		try:
			return self.requestData['command']
		except KeyError:
			## error, invalid request.
			self.error = InvalidRequestCommandError;
			return "";

	def initRequestFromFieldStorage(self, fs):
		for k in fs.keys():
			self.requestData[k] = fs.getvalue(k);

	def getKeys(self):
		return self.requestData.keys();
	def getStorySetData(self):
		storysetdata = {};
		storysetdata['treesetid'] = self.requestData['treesetid'];
		storysetdata['treesetowner'] = self.requestData['treesetowner'];
		storysetdata['parent'] = self.requestData['parent'];
		storysetdata['child'] = self.requestData['child'];
		return storysetdata;
	def getStoryTreeNodeData(self):
		treenode = {};
		treenode['parent'] = self.requestData['parent'];
		treenode['storyid'] = self.requestData['storyid'];
		return treenode;
	def getTreeData(self):
		storysetdata = {};
		storysetdata;
		return storysetdata;
	def getStoryData(self):
		storydata = {};
		storydata['storyid'] = self.requestData['storyid'];
		storydata['storytitle'] = self.requestData['storytitle'];
		storydata['storybody'] = self.requestData['storybody'];
		return storydata;

	def getUserData(self):
		userdata = {};
		userdata['username'] = self.requestData['username'];
		userdata['userid'] = self.requestData['userid'];
		return userdata;
