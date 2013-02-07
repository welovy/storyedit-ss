#!/usr/bin/python
# -*- coding: utf-8 -*-
import cgi;

#from storyedit import *;

from storyedit.debug import *
from storyedit.storage import SEStorage;
from storyedit.story import *;
from storyedit.user import SEUser;
from storyedit.communicate import Response, Request;
from storyedit.error import *;

class SEEngine(object):
    __slots__ = ['result', 'storage', 'response', 'request'];
    def __init__(self):
        self.result = {};
        self.storage = SEStorage();
        self.response = Response();
        self.request = Request();

    def __str__(self):
        pass;

    def __repr__(self):
        pass;

    def setup(self):
        self.request.initRequestFromFieldStorage(cgi.FieldStorage());

    def createUser(self, userid):
        ## this function is initiate userdata
        ## generate treecode;
        storyset = SEStorySet(userid);
        blankstory = SEStory(storyset, storyset.root);

    def process(self):
        ##store into sqlite
        command = self.request.getCommand();
        if command == "save":
            user = SEUser();
            user.initFromDict(self.request.getUserData());
            status = self.storage.validateUser(user);
            if status == Success:
                treesetid = self.storage.getTreeSetByUserID(user.getUserID());
                treenode = SETreeNode(treesetid);
                treenode.initFromDict(self.request.getStoryTreeNodeData());
                ## get storydata;
                story = SEStory();
                story.initFromDict(self.request.getStoryData());
                status = self.storage.saveStory(user, treesetid, treenode);
            else:
                pass;
            ## TODO;


            
        elif command == 'login':
            ## validate, and if its new, make default tree.
            user = SEUser();
            user.initFromDict(self.request.getUserData());
            status = self.storage.validateUser(user);
            if status != Success:
                status = self.prepareForNewUser(user)
            else:
                # login success, load default data
                treesetid = self.storage.getTreeSetByUserID(user.getUserID());
                treeid = self.storage.getFirstTreeFromTreeSetID(treesetid);
                story = self.storage.getFirstStoryFromTreeID(treeid);
                self.response.setKeyValue('title', story.getStoryTitle());
                self.response.setKeyValue('body', story.getStoryBody());
                pass;
        else:
            # there's some error.
            if self.request.isError() == True:
                status = self.request.getError();
                self.response.setFailed(status);
                D('"' + status.getDetail() + '"');
            else:
                # no error. hum...
                pass;
        if status == Success:
            self.response.setSuccess();
        else:
            self.response.setFailed(status);
        self.response.setRequestedCommand(command);
        self.response.prepareSysmsg();

    def prepareForNewUser(self, user):
        # its new user, create userid;
        # make new user;
        newuser = user;
        blankstory = SEStory();
        blankstory.setupAsDefault();
        newstoryset = SEStorySet(newuser);
        newstoryset.setupAsDefault(newuser.getUserID(), blankstory);
        self.storage.saveNewUser(newuser.getUserID(), newstoryset.getTreeSetID());
        self.storage.saveNewStorySet(newstoryset);
        
        status = Success; # FIXME : its temp
        self.response.setSuccess(); # FIXME : its temp
        return status;

    def putresult(self):
        self.response.printHTTP();

    def close(self):
        pass;
