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
  
  #callback function για την μετατροπή των html entities
  def func(m):
    if m.group(0) == "&amp;":
      return '&'
    elif m.group(0) == "&gt;":
      return '>'
    elif m.group(0) == "&lt;":
      return '<'
    elif m.group(0) == "&nbsp;":
      return ' '
  
  text1 = repx2.sub("", text)
  
  text2 = repx3.sub("", text1)
  
  for m in repx4.finditer(text2):
    print(m.group(1))
  
  text3 = repx5.sub("", text2)
  
  text4 = repx6.sub(func, text3)
  
  text5 = repx7.sub(" ", text4)
  
  #εκτύπωση του κειμένου μετά τις μετατροπές
  print(text5)
