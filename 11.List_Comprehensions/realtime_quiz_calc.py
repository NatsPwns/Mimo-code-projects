answers = ['C', 'B', 'C', 'A', 'D', 'A', 'B', 'D', 'D', 'C']
responses = ['C', 'B', 'C', 'A', 'D', 'A', 'B', 'D', 'D', 'C']

if responses[-1] == answers[len(responses)-1]:
    correct = True
else:
    correct = False

if not correct:
    del responses[-1]
    print('Sorry, please try the last question again!')
