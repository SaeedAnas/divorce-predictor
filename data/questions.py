import json

data = {}
data['questions'] = []
data['questions'].append({
    'id': 1,
    'question': 'I know we can ignore our differences, even if things get hard sometimes.'
})

data['questions'].append({
    'id': 2,
    'question': 'We don\'t have time at home as partners.'
})

data['questions'].append({
    'id': 3,
    'question': 'I think that one day in the future, when I look back, I see that my spouse and I have been in harmony with each other.'
})

data['questions'].append({
    'id': 4,
    'question': 'My spouse and I have similar ideas about how marriage should be.' 
})

data['questions'].append({
    'id': 5,
    'question': 'I know my spouse\'s basic anxieties.'
})

data['questions'].append({
    'id': 6,
    'question': 'We\'re just starting a discussion before I know what\'s going on.'
})

with open('questions.json', 'w') as outfile: 
    json.dump(data, outfile)


# with open('questions.json') as json_file:
#     data = json.load(json_file)

# questions = data['questions']
# for question in questions:
#     print(question.get('question'))
# print(questions)