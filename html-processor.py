import re 

with open("testpage.txt","r") as fp:
  text = fp.read()
  #1. εξαγωγή και εκτύπωση του τίτλου
  
  repx = re.compile(r"<title>(.+?)</title>")
  m = repx.search(text)
  printf(m.group(1))
  
  #2. απαλοιφή σχολίων
  repx2 = re.compile(r"<!--.*?-->",re.DOTALL)
  
  #3. απαλοιφή <script> / <style>
  repx3 = re.compile(r"(<script.*?</script>) | (<style.*?</style>)",re.DOTALL)
  
  #4. εξαγωγή και print του <a>
  repx4 = re.compile(r"<a(.+?)</a>",re.DOTALL)
  
  #5. απαλοιφή όλων των tags
  repx5 = re.compile(r"<.+?>",re.DOTALL)
  
  #6. μετατροπή html entities
  repx6 = re.compile(r"(&amp;|&gt;|&lt;|&nbsp;)",re.DOTALL)
  
  #7. μετατροπή whitespace σε ένα κενό
  repx7 = re.compile(r"\s+")
  
  
