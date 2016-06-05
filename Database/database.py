import MySQLdb as msd


class Database(object):
	host = "localhost"
	user = "root"
	password = "Satyam007@"
	db = "zyloc"

	def run_query(self,*args,**kwargs):
		try:
			self.cursor.execute(sql)
		except msd.OperationalError:
			pass

	def insert_data(self,*args,**kwargs):
		try:
			self.cursor.execute(data['sql'])
			self.connection.commit()
		except msd.OperationalError:
			self.connection.rollback()	

	def fetch_data(self,*args,**kwargs):
		pass

	def delete_data(self,*args,**kwargs):
		pass

	def __init__(self):
		self.connection = msd.connect(self.host,self.user,self.password,self.db)
		self.cursor = self.connection.cursor()

	def __del__(self):
		self.connection.close()


