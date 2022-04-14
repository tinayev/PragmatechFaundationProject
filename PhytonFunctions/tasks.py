# a b-dən böyükdürsə a və b ədədləri arasında 5-ə bölünən amma 7-yə bölünməyən ədədləri ekrana çap edin.(a=50,b=20)
b=20 
print(b)
b=b+5
print(b)
b=b+10
print(b)
b=b+15
print(b)
b=b+25
# a və b arasında olan ədədlərin cəmini return edin.1 den-100 e qeder ededlerin cemini cap et
def ededleriTopla():
  i=0
  cemi=0
  while i<100:
      cem=cem+1
      i=i+1
      print(cem)
      ededleriTopla()
