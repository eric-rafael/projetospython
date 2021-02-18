from requests import Session
import re, os

def start():
	try:
		with open('google.txt', 'r') as file:
			db = file.readlines()
			file.close()
	except:
		db = []

	def save(db):
		with open('google.txt', 'w') as file:
			file.writelines(db)
			file.close()

	def extract(session):
		exp = '<a href="/url\?q=(.*?)">'
		inp = input('Search: ')
		url = 'https://www.google.com/search?q={}&start={}'
		req = ''
		a = 0
		while(not 'não encontrou nenhum documento correspondente.' in req or not 'did not find any matching documents' in req):
			link = url.format(inp.replace(' ', '+'), str(a))
			req = session.get(link).text
			if('Sometimes you may be asked to solve the CAPTCHA if you are using advanced terms that robots are known to use, or sending requests very quickly.' in req):
				save(db)
				exit('RECAPTCHA ACIONADO!')
			list = re.findall(exp, req)
			if(len(list) <= 1):
				break
			for x in list:
				try:
					hst = re.search('https?://(.*?)/', x).group(0)
				except:
					hst = 'http://example.com/'
					break
				print(hst)
				if(not hst+"\n" in db):
					db.append(hst+"\n")
			save(db)
			a += 10
		#os.system('clear')
		print('Total: {}'.format(len(db)))

	cnf = 'y'
	session = Session()
	while(cnf.lower() != 'n'):
		extract(session)
		cnf = input('Deseja continuar? [Y/n]')
	#print(db)
start()