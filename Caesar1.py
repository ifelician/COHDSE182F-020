def cipher(text,key):
        
        result = ""

for i in range(len(text)):
      char = text[i]
      
      
      if (char.isupper()):
         result += chr((ord(char) - 65 + key) % 26 + 65)
      else:
         result += chr((ord(char) - 97 + key) % 26 + 97)
      return result

text = "the die has been cast"
key = 3
print ("Plain text: "+text)
print ("key: "+key)
print ("Cipher: "+cipher(text, key))
