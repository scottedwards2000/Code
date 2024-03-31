
def outer_function():
  outer_var = "I'm from the outer function"

  def inner_function():
    nonlocal outer_var 
    print(outer_var)
    outer_var = "I've been changed"

  inner_function()
  print(outer_var)

outer_function()

#BUT, we don't have to use 'nonlocal' if the outer scope is global:
def printtest():
  #global test #if you include this line it will modify the outside version (nonlocal doesn't work here b/c test in GLOBAL scope)
  test='mod'
  print(test)

test = 'global test was not modified'
printtest()
print(test)

#but this will not work because scope search doesn't go out-to-in:
#print(outer_var)
