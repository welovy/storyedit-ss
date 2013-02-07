#!/usr/bin/python
# -*- coding: utf-8 -*-
import json;
import uuid;
import datetime;
#from i18n import _

__all__ = ["SEStory", "SEStorySet", "SETreeNode"];

class SEStory(object):
    __slots__ = ['storyID', 'storyTitle', 'storyBody', 'createDate', 'modifiedDate'];

    def __init__ (self):
        self.storyID = '';
        self.storyTitle = 'undefined';
        self.storyBody = 'unwritten';
        self.createDate = datetime.date(2012, 11, 29);
        self.modifiedDate = datetime.date(2012, 11, 29);

    def setupAsDefault(self, parentStory = None):
        self.storyID = str(uuid.uuid1());
        self.createDate.today();
        self.storyTitle= 'undefined';
        if parentStory != None:
            self.parent = parentStory;
    
    def getStoryID(self):
        return self.storyID;

    def setStoryID (self, id) :
        self.storyID = id;

    def setStoryTitle (self, title) :
        self.storyTitle = title;

    def getStoryTitle(self):
        return self.storyTitle;

    def setStoryBody (self, body):
        self.storyBody = body;

    def getStoryBody(self):
        return self.storyBody;

    def initFromJSON(self, jsonstr):
        obj = json.load(jsonstr);
        self.storyID = obj['storyid'];
        self.storyTitle = obj['title'];
        self.storyBody = ojb['body'];

    def initFromDict(self, storydata):
        self.storyID = storydata['storyid'];
        self.storyTitle = storydata['storytitle'];
        self.storyBody = storydata['storybody'];

class SETreeNode:
    __slots__ = ['belongsTreeSetID', 'storyID', 'parentID'];
    def __init__ (self, parent=''):
        self.belongsTreeSetID = parent;
        self.storyID = 0;
        self.parentID = 0;
    def setTreesetID(self, parent):
        self.belongsTreeSetID = parent;
        
    def initFromDict(self, treenodeData):
        self.storyID = treenodeData['storyid'];
        self.parentID = treenodeData['parent'];

class SEStorySet:
    __slots__ = ['treesetID', 'treesetOwner', 'parent', 'child'];
    def __init__(self, owner = None):
        self.treesetID = '';
        if owner == None:
            self.treesetOwner = None;
        else:
            self.treesetOwner = owner.getUserID();
        self.parent = 1; ## root id is always 1;
        self.child = [];

    def setupAsDefault(self, userid, blankstory):
        self.treesetID = str(uuid.uuid1());
        self.treesetOwner = userid;
        self.parent = 1 # its always root;
        self.child.append(blankstory);

    def getTreeSetID(self):
        return self.treesetID;

    def initFromDict(self, storyset):
        self.treesetID = storyset['treesetid'];
        self.treesetOwner = storyset['treesetowner'];
        self.parent = storyset['parent'];
        ## TODO
        ## set child or not


