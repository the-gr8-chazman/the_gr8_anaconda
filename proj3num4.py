count = 0.0

three_errors = 0.0

percent_error = 0.0

with open('http_access_log') as f:
  for line in f:
      #print line
      if 'GET' in line:
         count = count + 1

three_string = '" 3'
#The 3xx after the "GET xxxxxx" part of the line
with open('http_access_log') as j:
  for line in j:
        if three_string in line:
          three_errors = three_errors +1

percent_error = three_errors/count *100


print  "total requests made: ", count
print  "total 3xx errors: ", three_errors
print  "the % of 3xx of all requests:", percent_error, "%"


