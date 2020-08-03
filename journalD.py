import requests
import urllib.request
from bs4 import BeautifulSoup as BS4
import string

url = 'https://scholar.google.com/scholar?hl=en&as_sdt=0%2C55&q='

query = str(input("Topics: "))
query = "+".join(query.split(" "))
url += query
page = 1
_sort = False

#=============================================================================================================
def download_journal(response,items):
	urlDownload = items[response-1].h3.a.attrs['href']
	print("Link Jurnal:",urlDownload)
	title = items[response-1].h3.a.text.translate(str.maketrans("","",string.punctuation)) + ".pdf"
	scihub = "https://sci-hub.tw"
	payload = {"request":urlDownload}
	pdf = False
	try:
		pdfLink = items[response-1].find('div',class_='gs_or_ggsm').a.attrs['href']
		print("Link PDF:",pdfLink)
		pdf = '.pdf' in pdfLink
	except:
		pass

	print("Sedang mendownload: %s" %title)

	if pdf:
		urllib.request.urlretrieve(pdfLink,title)
		print("Berhasil mendownload Jurnal:",title)
	else:
		session = requests.Session()
		_link = session.post(scihub, data=payload)
		soup = BS4(_link.text, 'html.parser')
		downloadLink = soup.find('li').a.attrs['onclick'].replace("location.href=","").replace("'","")
		print(downloadLink)
		
		if downloadLink[:4] != "http":
			downloadLink = "https:" + downloadLink
		print("Link Download:",downloadLink)
		urllib.request.urlretrieve(downloadLink,title)

		print("Berhasil mendownload Jurnal:",title)


while True:
	print("Silahkan tunggu...")
	print("\nHalaman %i\n" %page)
	_get = requests.get(url)
	soup = BS4(_get.text, "html.parser")
	test = soup.find("div", id="gs_res_ccl_mid")
	items = test.find_all('div',class_='gs_scl')

	for x in range(len(items)):
		try:
			title = items[x].h3.a.text
			info = items[x].find('div',class_='gs_a').text
		except:
			title = 'Unknown'
			info = 'Unknown'
		#desc = items[x].find('div',class_='gs_rs').text
		'''cite = items[x].find_all('div',class_='gs_fl')
		if len(cite) == 2:
			cite = cite[1].find_all('a')[2].text
		else:
			cite = cite[0].find_all('a')[2].text'''
		print(" ["+str(x+1)+"]\t", title)
		print("\t", info)
		#print("    ", desc)
		#print("    ", cite)

	txt = '''
-----------------------------------------------------------------------
| Ketik nomor Jurnal yang akan didownload (1-10)                      |
|                                                                     |
| Catatan:                                                            |
| - Ketik 0 untuk membatalkan                                         |
| - Ketik 11 untuk melihat daftar Jurnal selanjutnya                  |
| - Ketik 12 untuk menyortir Jurnal                                   |
| - Ketik tahun contoh: 2010 untuk melihat Jurnal dari tahun tersebut |
-----------------------------------------------------------------------
'''
	print(txt)

	respon = int(input("* Ketik respon disini: "))

	if respon == 0:
		break

	elif respon==1 or respon==2 or respon==3 or respon==4 or respon==5 or respon==6 or respnd_all('a')[2].text'''
		print(" ["+str(x+1)+"]\t", title)
		print("\t", info)
		#print("    ", desc)
		#print("    ", cite)

	txt = '''
-----------------------------------------------------------------------
| Ketik nomor Jurnal yang akan didownload (1-10)                      |
|                                                                     |
| Catatan:                                                            |
| - Ketik 0 untuk membatalkan                                         |
| - Ketik 11 untuklace('&scisbd=1','')
			_sort = False

	else:
		yr = respon
		url += "&as_ylo=" + str(yr)