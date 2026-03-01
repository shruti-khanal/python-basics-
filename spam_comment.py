p1="click this"
p2="buy this"
p3="open link"
p4="send money"
message=input("enter your comment ")
if(p1 in message) or (p2 in message ) or (p3 in message) or (p4 in message):
   print("this is a spam comment ")
else : 
   print("this is not a spam comment")   