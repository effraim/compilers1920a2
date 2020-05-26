import re 

with open("testpage.txt","r") as fp:
  text = fp.read()
  #1. εξαγωγή και εκτύπωση του τίτλου
  
  #μηχανή ταιριάσματος
  rexp = re.compile(r"<title>(.+?)</title>")
  m = repx.search(text)
  printf(m.group(1))
