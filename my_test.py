basic_answers = [{'key':'Привет'}, {'key':'Нормально'},{'answer':'Пока'}]

# lists = list(basic_answers)
# print(lists)

for i in basic_answers:
	for j in i:
		print(j,';',i[j])