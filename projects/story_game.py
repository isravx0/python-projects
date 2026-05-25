# load story text in read mode
with open ("story.txt", "r") as f:
    story = f.read()

words = set()
start_of_word = -1

target_sart = "<"
target_end = ">"

# loop through the story
for i, char in enumerate(story):
    # check if it's equal to <
    if char == target_sart:
        start_of_word = i
    if char == target_end and start_of_word != -1:
        # add the words to the words array
        word = story[start_of_word: i + 1]
        words.add(word)
        start_of_word = -1

answers = {}
print("\n" + "="*60)
print("Welcome to the Mad Libs Story Game!")
print("="*60 + "\n")

for word in words:
    answer = input("Enter a word for " + word + ": ")
    answers[word] = answer

# replace input answers with the story words
for word in words:
    story = story.replace(word, answers[word])

print("\n" + "="*60)
print("✨ HERE'S YOUR STORY ✨")
print("="*60 + "\n")
print(story)
print("\n" + "="*60 + "\n")


