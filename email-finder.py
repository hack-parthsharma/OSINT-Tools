from pyhunter import PyHunter
import sys

if len(sys.argv) != 5:
	print "Usage:   ", sys.argv[0], "Domain Count Start APIkey"
	print "Example: ", sys.argv[0], "microsoft.com 20 10 0123456789"
	print "Note: Hunter API Maximum Count is 100"
	exit()

domain = sys.argv[1]
count = int(sys.argv[2])
start = int(sys.argv[3])
API = sys.argv[4]

print "Domain:", domain
print "Count:", count
print "Start:", start
print "API Key:", API
print "----------------------------------------------------------"

hunter = PyHunter(API)

data1 = hunter.email_count(company=domain)
print "Number of all available emails:", data1['total']

print "----------------------------------------------------------"

data2 = hunter.account_information()
print "Account Information:-"
for x,y in data2.items():
	print x+":", y

print "----------------------------------------------------------"

data = hunter.domain_search(company=domain, limit=count, offset=start)

for x in data["emails"]:
	print x["value"]
