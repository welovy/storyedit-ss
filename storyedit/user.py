#!/usr/bin/python
# -*- coding: utf-8 -*-

__all__ = ['SEUser'];

class SEUser(object):
	__slots__ = ['username', 'userID'];
	def __init__ (self):
		self.username = 'unkonwn';
		self.userID = 'xxxx-xxxx-xxxx';

	def setUserName(self, name):
		self.username = name;

	def setUserID(self, userID):
		self.userID = userID;

	def getUserID(self) :
		return self.userID;

	def getUserName(self):
		return self.username;

	def initFromDict(self, dict):
		self.username = dict['username'];
		self.userID = dict['userid'];
		pass;

