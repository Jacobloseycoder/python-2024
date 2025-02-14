def p1():
  name = input("enter the name")
  for ch in name:
    if ch == "t" or ch == "T":
      oo = oo + 1
  print("t appers", oo, "times")

def p2():
  meme = "Roses are red"
  print("meme[1]")

def p3():
  meme = "Roses"
  meme += "are"
  meme += "red"
  print(meme)

def p4():
  name = "carmen"
  print("where in the world is", name)
  name += "sandeago"
  print("where in the world is", name)

def p5():
  name = "jim bim tim"
  middle_name = name[4:6]
  print(middle_name)
  middle_name = name[4:6+1]
  print(middle_name)

def p6():
  name = ‘Norma Jean Mortensen’
  first_name = name[:4+1]
  print(first_name)
  last_name = name[11:]
  print(last_name)
  middle_name = name[6:9+1]
  print(middle_name)
  what_does_this_do = name[-9:]

def p7():
  fn = input("firxt name")
  ln = input("last name")
  id = input("id number")
  userlog = 
