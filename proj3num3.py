count = 0.0

four_errors = 0.0

percent_error = 0.0

with open('http_access_log') as f:
  for line in f:
      #print line
      if 'GET' in line:
         count = count + 1

four_string = '" 4'
#the 4xx after the "GET xxxxxx" part of the line 
with open('http_access_log') as j:
  for line in j:
	if four_string  in line:
	  four_errors = four_errors +1

percent_error = four_errors/count *100

print  "total requests made: ", count
print  "total 4xx errors: ", four_errors
print  "the % of 4xx of all requests:", percent_error, "%"
