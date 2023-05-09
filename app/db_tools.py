
 

import sqlite3

DB_FILE = "data.db"

#db = sqlite3.connect(DB_FILE, check_same_thread=False) #sqlite3.connect(DB_FILE)
#c = db.cursor()

stories_header = "(storyName TEXT, fullStory TEXT, lastAdded TEXT, Contributors TEXT)"
users_header = ("(username TEXT, password TEXT)")
db_header = ("(Brookyln TEXT, Bronx TEXT, Manhattan TEXT, Queens TEXT, Staten Island TEXT)")
def query(sql, extra = None):
    db = sqlite3.connect(DB_FILE, check_same_thread=False)
    c = db.cursor()
    if extra is None:
        res = c.execute(sql)
    else:
        res = c.execute(sql, extra)
    db.commit()
    db.close()
    return res
def create_table(name, header):
    query(f"CREATE TABLE IF NOT EXISTS {name} {header}")

create_table("DBInfo", db_header)
#create_table("UserInfo", users_header)

def get_table_list(tableName):
    db = sqlite3.connect(DB_FILE, check_same_thread=False)
    c = db.cursor()
    res = c.execute(f"SELECT * from {tableName}")
    out = res.fetchall()
    db.commit()
    db.close()
    return out
#add data row to sqlTable, put row in list format
#if username already in db returns -1
def add_account(username, password):
    if not(account_exists(username)):
        query("INSERT INTO UserInfo VALUES (?, ?)", (username, password))
    else:
        return -1

def account_exists(username):
    accounts = get_table_list("UserInfo")
    for account in accounts:
        if account[0] == username:
            return True
    return False
#return true if username and password are in db, false if one isn't
def verify_account(username, password):
    accounts = get_table_list("UserInfo")
    for account in accounts:
        if account[0] == username and account[1] == password:
            return True
    return False

def get_db_data(db_name):
    dbs = get_table_list("DBInfo")
    for db in dbs:
        if db[0] == db_name:
            return db[1:]
    return -1
def add_db_data(db_name, db_data):
    if not(db_exists(db_name)):
        query("INSERT INTO DBInfo VALUES (?, ?, ?, ?, ?)", (db_data[0], db_data[1], db_data[2], db_data[3], db_data[4]))
    else:
        return -1
def update_db_data(db_name, db_data):
    if db_exists(db_name):
        query(f'''
        UPDATE DBInfo
        SET Brooklyn = ?,
        Bronx = ?,
        Manhattan = ?,
        QUeens = ?,
        Staten Island = ?,
        WHERE
        storyName = ?
        ''', (db_data[0], db_data[1], db_data[2], db_data[3], db_data[4], db_name))
    else: 
        return -1
def db_exists(db_name):
    dbs = get_table_list("DBInfo")
    for db in dbs:
        if db[0] == db_name:
            return True
    return False

#add new story to db
#if a story with that name already exists 
def add_story(storyName, newText, contributor):
    if not(story_exists(storyName)):
        query("INSERT INTO StoryInfo VALUES (?, ?, ?, ?)", (storyName, newText, newText, contributor))
    else:
        return -1
#return fullText, lastAdded, and contributors of a story
#return -1 if story is not in db
def get_story_info(storyName):
    storyInfo = get_table_list("StoryInfo")
    for row in storyInfo:
        if row[0] == storyName:
            return row[1:]
    return -1
    
def get_story_contents(storyName):
    storyInfo = get_table_list("StoryInfo")
    for row in storyInfo:
        if row[0] == storyName:
            return row[1]
    return -1
            
#edit story
def edit_story(storyName, newText, contributor):
    if story_exists(storyName):
        storyInfo = get_story_info(storyName)
        fullText = storyInfo[0] + newText 
        print(fullText)
        contributors = contributor + "," + storyInfo[2] 
        query(f'''
        UPDATE storyInfo
        SET fullStory = ?,
        lastAdded = ?,
        Contributors = ?
        WHERE
        storyName = ?
        ''', (fullText, newText, contributors, storyName))
    else:
        return -1
def get_user_stories(username):
    viewable_stories = []
    editable_stories = []
    stories = get_table_list("StoryInfo")
    for story in stories:
        contributors = story[3].split(",")
        if username in contributors:
            viewable_stories.append(story[0])
        else:
            editable_stories.append(story[0])
    return viewable_stories, editable_stories

#add_story("beesInfo", "bees are cool", "AymanLublsky")
# print(edit_story("beeInfo", ".  I hate bees :(", "Ayman"))
#print(get_table_list("storyInfo"))
#print(verify_account("hello", "world"))
#print(add_account("my", "name"))
#print(get_table_list("UserInfo"))
#print(get_user_stories("SamLublsky"))

#db.commit()
#db.close()
