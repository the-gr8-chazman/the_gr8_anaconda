


Oct1File = []
NovFile = []
DecFile = []
JanFile = []
FebFile = []
MarFile = []
AprFile = []
MayFile = []
JunFile = []
JulFile = []
AugFile = []
SepFile = []
Oct2File = []




with open('http_access_log') as f:
  for line in f:
   if 'Oct/1994' in line:
      Oct1File.append(line)    
   if 'Nov/1994' in line:
      NovFile.append(line)
   if 'Oct/1994' in line:
      DecFile.append(line)
   if 'Oct/1994' in line:
      JanFile.append(line)
   if 'Oct/1994' in line:
      FebFile.append(line)
   if 'Oct/1994' in line:
      MarFile.append(line)
   if 'Oct/1994' in line:
      AprFile.append(line)
   if 'Oct/1994' in line:
      MayFile.append(line)
   if 'Oct/1994' in line:
      JunFile.append(line)
   if 'Oct/1994' in line:
      JulFile.append(line)
   if 'Oct/1994' in line:
      AugFile.append(line)
   if 'Oct/1994' in line:
      SepFile.append(line)
   if 'Oct/1994' in line:
      Oct2File.append(line)
f.close()

f = open('Oct1994','w')
for item in Oct1File:
   print>>f, item
f.close()
print "Oct1done"

f = open('Nov1994','w')
for item in Oct1File:
   print>>f, item
f.close()
print "Novdone"

f = open('Dec1994','w')
for item in Oct1File:
   print>>f, item
f.close()
print "Decdone"

f = open('Jan1995','w')
for item in Oct1File:
   print>>f, item
f.close()
print "Jandone"

f = open('Feb1995','w')
for item in Oct1File:
   print>>f, item
f.close()
print "Febdone"

f = open('Mar1995','w')
for item in Oct1File:
   print>>f, item
f.close()
print "Mardone"

f = open('Apr1995','w')
for item in Oct1File:
   print>>f, item
f.close()
print "Apr1done"

f = open('May1995','w')
for item in Oct1File:
   print>>f, item
f.close()
print "Maydone"

f = open('Jun1995','w')
for item in Oct1File:
   print>>f, item
f.close()
print "Jundone"

f = open('Jul1995','w')
for item in Oct1File:
   print>>f, item
f.close()
print "Juldone"

f = open('Aug1995','w')
for item in Oct1File:
   print>>f, item
f.close()
print "Augdone"

f = open('Sep995','w')
for item in Oct1File:
   print>>f, item
f.close()
print "Sepdone"

f = open('Oct1995','w')
for item in Oct1File:
   print>>f, item
f.close()
print "Oct2done"






"""
   if 'Nov/1994' in line:
         NovCount = NovCount + 1
   if 'Dec/1994' in line:
         DecCount = DecCount + 1
   if 'Jan/1995' in line:
         JanCount = JanCount + 1
   if 'Feb/1995' in line:
         FebCount = FebCount + 1
   if 'Mar/1995' in line:
         MarCount = MarCount  + 1
   if 'Apr/1995' in line:
         AprCount = AprCount  + 1
   if 'May/1995' in line:
         MayCount = MayCount  + 1
   if 'Jun/1995' in line:
         JunCount = JunCount + 1
   if 'Jul/1995' in line:
         JulCount = JulCount + 1
   if 'Aug/1995' in line:
         AugCount = AugCount + 1
   if 'Sep/1995' in line:
         SepCount = SepCount + 1
   if 'Oct/1995' in line:
         Oct2Count = Oct2Count + 1

"""






"""
Oct1Count = 0
NovCount = 0
DecCount = 0
JanCount = 0
FebCount = 0
MarCount = 0
AprCount = 0
MayCount = 0
JunCount = 0
JulCount = 0
AugCount = 0
SepCount = 0
Oct2Count = 0

with open('http_access_log') as f:
  for line in f:
#	print line
   if 'Oct/1994' in line:
         Oct1Count = Oct1Count + 1
	if 'Nov/1994' in line:
         NovCount = NovCount + 1
	if 'Dec/1994' in line:
	 DecCount = DecCount + 1
	if 'Jan/1995' in line:
         JanCount = JanCount + 1
	if 'Feb/1995' in line:
         FebCount = FebCount + 1
	if 'Mar/1995' in line:
         MarCount = MarCount  + 1
	if 'Apr/1995' in line:
         AprCount = AprCount  + 1
	if 'May/1995' in line:
         MayCount = MayCount  + 1
	if 'Jun/1995' in line:
         JunCount = JunCount + 1
	if 'Jul/1995' in line:
         JulCount = JulCount + 1
	if 'Aug/1995' in line:
         AugCount = AugCount + 1
	if 'Sep/1995' in line:
         SepCount = SepCount + 1
	if 'Oct/1995' in line:
         Oct2Count = Oct2Count + 1

print "number of accesses in Oct,1994: ", Oct1Count
print "number of accesses in Nov: ", NovCount
print "number of accesses in Dec: ", DecCount
print "number of accesses in Jan: ", JanCount
print "number of accesses in Feb: ", FebCount
print "number of accesses in Mar: ", MarCount
print "number of accesses in Apr: ", AprCount
print "number of accesses in May: ", MayCount
print "number of accesses in Jun: ", JunCount
print "number of accesses in Jul: ", JulCount
print "number of accesses in Aug: ", AugCount
print "number of accesses in Sep: ", SepCount
print "number of accesses in Oct,1995: ", Oct2Count
"""
