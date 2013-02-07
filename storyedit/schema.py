
class SESchema(object):
	__slots__ = ['name'];
	def __init__(self):
		self.name = "";

class UserSchema(SESchema):
	def __init__(self):
		self.name = "user_tbl";

	def getSchemaString(self):
		return """create table if not exists user_tbl (
			userid varchar(128) not null primary key,
			treesetid varchar(128) not null unique,
			createdate datetime
			)""";
	def getInsertString(self):
		sql = 'insert into ' + self.name + " values(?, ?, ?)";
		return sql;

class TreesetSchema(SESchema):
	def __init__(self):
		self.name = "treeset_tbl";
	def getSchemaString(self):
		return """create table if not exists treeset_tbl (
			treesetid varchar(128) not null primary key,
			treeid varchar(128) not null unique,
			title varchar(128) not null,
			createdate datetime,
			modifieddate datetime
			)""";
	def getInsertString(self):
		sql = "insert into " + self.name + " values(?, ?, ?, ?, ?)"
		return sql;

class TreeSchema(SESchema):
	def __init__(self):
		self.name = "tree_tbl";
	def getSchemaString(self):
		return """create table if not exists tree_tbl (
			treeid varchar(128) not null primary key,
			left real not null,
			right real not null,
			storyid  integer
			)""";
	def getInsertString(self):
		sql = "insert into " + self.name + " values(?, ?, ?, ?);";
		return sql;

class StorySchema(SESchema):
	def __init__(self):
		self.name = 'story_tbl';
	def getSchemaString(self):
		return """create table if not exists story_tbl (
			storyid integer not null primary key autoincrement,
			title string not null,
			body text
			)"""
	def getInsertString(self):
		return "insert into " + self.name + " values(?, ?, ?)";

