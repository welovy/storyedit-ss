#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3;
import uuid;
import datetime;

from storyedit.user import *;
from storyedit.schema import *;
from storyedit.error import *;
from storyedit.story import *;

STORAGEFILE = "db/data.sqlite3";

class SETable(object):
	__slots__ = ['name']
	def __init__(self, name):
		self.name = name;
		pass;

	def addColumn(self):
		pass;

class SEStorage(object):
	__slots__ = ['con'];
	def __init__(self):
		self.con = sqlite3.connect(STORAGEFILE);
		schema = UserSchema();
		sql = schema.getSchemaString();
		self.con.execute(sql);
		schema = TreesetSchema();
		sql = schema.getSchemaString();
		self.con.execute(sql);
		schema = TreeSchema();
		sql = schema.getSchemaString();
		self.con.execute(sql);
		schema = StorySchema();
		sql = schema.getSchemaString();
		self.con.execute(sql);
#		self._makeTestData();

	def _makeTestData(self):
		userid = uuid.uuid1();
		treesetid = '';
		sql = """insert into user_tbl values('%s', '', 123)
		""" % (userid);
		self.con.execute(sql);
		storyid = 1;

		sql = """insert into tree_tbl values('%s', 1, 100, '%s')
		""" % (userid, storyid);
		self.con.execute(sql);
		self.con.commit();

	# def insertUser(self, userid, treeid):
	# 	sql = """insert into user_tbl(userid, treeid, createdate)
	# 	values(%s,%s, %s)""";
	# 	sql % (123, 234, 456);
	# 	self.con.execute(sql);
	# 	self.con.commit();

	def _insertTree(self):
		pass;

	def _insertStory(self, story):
		pass;

	def _updateStory(self):
		pass;

	def getStory(self, storyid):
		sql = """select * from story_tbl where storyid='%s'""" % (storyid);
		c = self.con.cursor();
		c.execute(sql);
		count = 0
		for row in c:
			count += 1;
			s = (row[1], row[2]); # supposed to be (title, body);
		assert(count == 1);
		return s;

	def getTreeSetByUserID(self, userid):
		sql = "select treesetid from user_tbl where userid='" + str(userid) + "'";
		c = self.con.cursor();
		num = c.execute(sql);
		treesetid = -1;
		for row in c:
			treesetid = row[0];
		return treesetid;

	def saveNewUser(self, userid, treesetid):
		#save new user
		sql = UserSchema().getInsertString();
		self.con.execute(sql, (userid, treesetid, userid));
		self.con.commit();


	def saveNewStorySet(self, storyset):
		# save storyset
		sql = TreesetSchema().getInsertString();
		assert(storyset.child[0] != None);
		blankstory = storyset.child[0];
		self.con.execute(sql,
		     (storyset.treesetID,
		     blankstory.getStoryID(),
		     blankstory.getStoryTitle(),
		     '2012-11-29',
		     '2012-11-29')
		);
		self.con.commit();

		#save default tree
		sql = TreeSchema().getInsertString();
		# firststory should be 1.0 -- 100.0
		storyid = 1;
		self.con.execute(sql, (blankstory.getStoryID(), 1.0, 100.0, storyid));
		self.con.commit();

		#save default story
		sql = StorySchema().getInsertString();
		self.con.execute(sql, (None, blankstory.getStoryTitle(), blankstory.getStoryBody()));
		self.con.commit();
		return Success;


	def _getTreeSetFromTreeSetID(self, treesetid):
		pass;

	def getFirstTreeFromTreeSetID(self, treesetid):
		sql = "select * from treeset_tbl where treesetid='%s'" % treesetid;
		c = self.con.cursor();
		c.execute(sql);
		count = 0;
		treeid = '';
		for row in c:
			count += 1;
			treeid = row[1]; # FIXME it must be array.
		assert(count == 1); # it should be unique
		return treeid;
		
	def getFirstStoryFromTreeID(self, treeid):
		sql = "select * from tree_tbl where treeid='%s'" % treeid;
		c = self.con.cursor();
		c.execute(sql);
		count = 0;
		storyid = '';
		for row in c:
			count += 1;
			storyid = row[3];
		assert(count == 1);
		# now, get contents;
		sql = "select * from story_tbl where storyid='%d'" % storyid;
		c.execute(sql);
		storyTitle = '';
		storyBody = '';
		for row in c:
			storyTitle = row[1];
			storyBody = row[2];
		story = SEStory();
		story.setStoryTitle(storyTitle);
		story.setStoryBody(storyBody);
		return story;


	def _getTreeDepth(self, treeid):
		pass;

	def validateUser(self, user):
		sql = "select * from user_tbl where userid='" + user.getUserID()+ "'";
		c = self.con.cursor();
		c.execute(sql);
		count = 0;
		for row in c:
			count += 1;
		status = None;
		if count >= 1 :
			status = Success;
		else:
			status = InvalidUserError;
			status.setDetail(status.getDetail() + ':your userid=%s, but count=%d' % (user.getUserID(), count));
		return status

	def saveStory(self, user, treenode, story):
		self._validateStory(user, treenode);
		self._updateStory(self);
		return status;

	def _validateStory(self, user, treenode):
		sql = "select * from tree_tbl where treeid='%s'" % treenode.getTreeID();
		c = sql.con.cursor();
		c.execute(sql);
		count = 0;
		for row  in c:
			count += 1;
		status = None;
		if count >= 1 :
			status = Success;
		else:
			status = InvalidUserError;
			status.setDetail(status.getDetail() + ':your userid=%s, but count=%d' % (user.getUserID(), count));
	def finalize(self):
		self.con.close();
	
