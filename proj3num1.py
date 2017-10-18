count = 0

with open('http_access_log') as f:
  for line in f:
      #print line
      if 'GET' in line:
         count = count + 1
 


print  "total requests made: ", count
 
