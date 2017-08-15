import sys
import re

userRE = r'@\w+'
hashtagRE = r'#\w+'
linkRE = r'((http[s]?|ftp):\/)?\/?([^:\/\s]+)((\/\w+)*\/)([\w\-\.]+[^#?\s]+)(.*)?(#[\w\-]+)?'
nonalphabeticalRE = r'[^a-z]'
wsRE = r'\s+'

for line in sys.stdin:
  line = ",".join(line[:-1].split(',')[3:]).lower()
  line = re.sub(userRE, "", line)
  line = re.sub(hashtagRE, "", line)
  line = re.sub(linkRE, "", line)
  line = re.sub(nonalphabeticalRE, " ", line)
  line = re.sub(wsRE, " ", line)
  print(line)
