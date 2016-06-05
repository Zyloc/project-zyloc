import database 

db = database.Database()
sql =  "INSERT INTO contest(platform,name,startTime,timeInterval) VALUES('Hacker Earth','randi ka naach',1,2)"
data = {}
data['sql'] = sql
db.insert_data(data)
	
