with open('referat.txt','r',encoding='utf-8') as t:
	text = t.read()
	words = text.split(' ')
	amount = len(words)
	print(amount)