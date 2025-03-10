#This program will take a paragraph and determine its
#sentences. It with then display each sentence, and
#how many sentences there are.

import re
#determines the sentence by punctuation, after dividing it by punctuation
def paragraphExaminer(paragraph):
    #divides the sentences by punctuation
    sentences = re.split(r'(?<=[.!?])\s+', paragraph)
    #makes sure the sentence has characters, and ends with punctuation
    sentencesReal = [sentence.strip() for sentence in sentences if sentence.strip() and sentence.strip()[-1] in ".!?"]
    return sentencesReal
#formats and displays the sentences properly
def sentenceShower(sentences):
    #each sentence is stored on the index, which displays
#the sentence number and its content
    for i, sentence in enumerate(sentences, 1):
        print(f"Sentence {i}: {sentence}")
    #prints the total  number  of  sentences
    print(f"\nTotal number of sentences: {len(sentences)}")
#gathers the information from the user
def main():
    paragraph = input("Enter a paragraph: ")
    sentences = paragraphExaminer(paragraph)
    sentenceShower(sentences)

main()
