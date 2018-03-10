basic_answers = [{'question':'Привет', 'answer':'Здравствуй'}, {'question':'Как дела?','answer':'Хорошо'},{'question':'Ну пока','answer':'Пока'}]
import csv

with open('basic_answers.csv', 'w', encoding='cp1251') as f:
	fields = ['question','answer']
	writer = csv.DictWriter(f, fields, delimiter=';')
	writer.writeheader()
	for string in basic_answers:
		writer.writerow(string)