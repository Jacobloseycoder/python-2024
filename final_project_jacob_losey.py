def main():
  print('_]WELCOME TO DUNGEN MONSTERS'[_)
  print('1.play')
  print('2.rules')
  print('3.quit')
  bing = int(input('select:'))
  if bing == 1:
    #call the start
  elif bing == 2:
    rules()
  elif bing == 3:
    print('ending...')
  else:
    print('not a option')
    main()

def rules():
  print('you will be placed in a maze and you have to escape')
  print('you will be given options to go north,south, west, or east')
  print("you can't move anyother way")
  print('you will have to find loot and fight monsters')
  print('you can pick up items by typing pick up when prompted')
  print('to fight back agenst a monster type sword well fighting to use the sword')
  print('if your hp goes to 0 you lose')
  print('but the most important thing is to have fun')
