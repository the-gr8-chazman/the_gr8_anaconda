


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




