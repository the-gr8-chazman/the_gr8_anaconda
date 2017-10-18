import re 

counts_by_day = {}

pattern = re.compile(".*\[(.*)\]\s+\".*")
with open('http_access_log') as f:
	for line in f:
	    match = pattern.match(line)
	    if match:
	        d = match.group(1)[:11]
	    else:
	        continue
	    if d not in counts_by_day:
	        counts_by_day[d] = 0
	    counts_by_day[d] += 1
#print counts_by_day

for k, v in counts_by_day.items():
         print(k, v)

#print [(x[0], x[1]) for x in sorted(counts_by_day.items(), key=lambda k: k[1])]
