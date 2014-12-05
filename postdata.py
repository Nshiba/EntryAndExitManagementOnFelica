import urllib
import urllib2
import csv

try:
  url = 'http://133.20.55.164/insert/'

  value = { 'student_id':'12fi078','name':'SHIBAHARA NAOYA','now':1,'date':'' }
  data = urllib.urlencode(value)
  data = data.encode('utf-8')

  userAgent = 'raspberryPi'
  userAgent = userAgent.encode('utf-8')

  headers = {'User-Agent':userAgent}

  req = urllib2.Request(url,data,headers)
  print req.get_full_url()
  response = urllib2.urlopen(req)

  responseData = response.read()
  responseData = responseData.decode('utf-8')

  row = []
  row.append(responseData)

  filename = 'postlog.csv'
  with open(filename, 'a') as f:
    writer = csv.writer(f, lineterminator='\n')
    writer.writerow(row)
except Exception as e:
  row = []
  row.append('reigai')
  row.append(e)

  filename = 'postlog.csv'
  with open(filename, 'a') as f:
    writer = csv.writer(f, lineterminator='\n')
    writer.writerow(row)
