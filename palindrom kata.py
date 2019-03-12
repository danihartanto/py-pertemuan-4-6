from modulStack import*
def reverseword(kata):
	word=stack.stack()
	string=''
	for i in (kata):
		stack.push(word, i)
	for i in range(stack.size(word)):
		temp = stack.pop(word)
		string = string + temp
	print (string)
	print('')
kata=input("masukkan kata: ")
if kata == kata:
        print("palindrom")
        reverseword(kata)
else:
        print("bukan palindrom")

