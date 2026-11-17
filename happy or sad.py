#LEVEL 1
train_data = [
("I got full marks in the test today!", "Happy"),
("We won the college cricket match", "Happy"),
("My friends planned a surprise party for me", "Happy"),
("The food in the canteen was really tasty", "Happy"),
("I am so excited for the weekend trip", "Happy"),
("Our project got selected for the exhibition", "Happy"),
("I finally learned how to ride a bicycle", "Happy"),
("Mom made my favourite sweets today", "Happy"),
("I lost my phone on the bus", "Sad"),
("I failed in the mathematics exam", "Sad"),
("My best friend is moving to another city", "Sad"),
("It rained and our picnic was cancelled", "Sad"),
("I missed the last bus and felt very upset", "Sad"),
("My laptop stopped working before the submission", "Sad"),
("i felt lonely during the long holiday","Sad"),
]
def count_moods(data):
    count_happy=0
    count_sad=0
    for i in data:
        if i[1].lower()=="happy":
            count_happy+=1
        elif i[1].lower()=="sad":
            count_sad+=1
    return count_happy,count_sad
print(count_moods(train_data))

#LEVEL 2
n=1
happy_words=["won"]
sad_words=["lost"]
punctuation=["?","@","!","#","$","&","_","-",".",":",";",","]
def guess_mood(sentence):
    happy=0
    sad=0
    for word in sentence.split():
        clean=""
        for ch in word:
            if ch not in punctuation:
                clean+=ch
        if clean in happy_words:
            happy+=1
        elif clean in sad_words:
            sad+=1
    if happy>sad:
        return "Happy"
    elif sad>happy:
        return "Sad"
    else:
        return "None"
print(guess_mood("I won todays match"))
print(guess_mood("I won hearts of many"))
print(guess_mood("I lost my wallet"))


#LEVEL 3
practice_data = [
    ("I won a medal in the sports meet", "Happy"),
    ("I lost my notebook before the exam", "Sad"),
    ("My friends gave me a lovely surprise", "Happy"),
    ("The train was late and I felt upset", "Sad"),
    ("Today was a great day", "Happy")
]
correct=0
for sentence,mood in practice_data:
    predicted_mood=guess_mood(sentence)
    print("Sentence:", sentence)
    print("Predicted:", predicted_mood)
    print("Actual:", mood)
    if predicted_mood == mood:
        correct += 1
    print()
total = len(practice_data)
accuracy = (correct / total) * 100
print("Correct predictions:", correct)
print("Total sentences:", total)
print("Accuracy:", accuracy, "%")
