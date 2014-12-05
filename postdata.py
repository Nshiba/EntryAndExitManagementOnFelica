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

  host = '133.20.55.164'
  host = host.encode('utf-8')

  content_type = 'application/x-www-form-urlencoded'
  content_type = content_type.encode('utf-8')

  headers = {'Host':host, 'User-Agent':userAgent, 'Content-Type':content_type}

  req = urllib2.Request(url,data,headers)
  response = urllib2.urlopen(req)

  responseData['body'] = response.read()
  responseData['body'] = responseData['body'].decode('utf-8')

  responseData['head'] = response.info().dict
  responseData['head'] = responseData['head'].decode('utf-8')

  row = []
  row.append(responseData)

  print row

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
