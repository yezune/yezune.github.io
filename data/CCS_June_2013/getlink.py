#!/usr/bin/env python

#status, response = http.request('http://www.iss.nl/research/conferences_and_seminars/previous_iss_conferences_and_seminars/complementary_currency_systems/index.html')

import urllib2
import re
url = "http://www.iss.nl/research/conferences_and_seminars/previous_iss_conferences_and_seminars/complementary_currency_systems"
page = urllib2.urlopen(url)
page = page.read()
links = re.findall(r"<a.*?\s*href=\"(.*?)\".*?>(.*?)</a>", page)
for link in links:	
	if "/fileadmin/" in link[0]:
		print("curl http://www.iss.nl"+link[0] + ' -o ' + link[0].split('/')[-1])
		#print('href: %s, HTML text: %s' % (link[0], link[1]))