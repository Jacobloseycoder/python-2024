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
