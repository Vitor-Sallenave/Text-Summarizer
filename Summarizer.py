import spacy

def line():
    print('==' * 40)


def Header():
    print('\n')
    line()
    print(f'\n{"Author: Vítor Sallenave Sales Milome":^75}\n')
    line()
    print('\b')


# Creates a dictionary with the frequency of the words
def createDict(document):
    dictionary = dict()

    for token in document:
        token_text = token.text
        if token_text not in dictionary:
            dictionary[token_text] = 1
        else:
            dictionary[token_text] += 1

    return dictionary


# Analyses the sentences' score: (index, sentence, score)
def verifySentsScore(document, dictionary):
    # Sentence's information
    sentences = document.sents
    sentences_verified = list()

    # Analyzing each sentence
    for i, sentence in enumerate(sentences):
        sentence_score = 0
        sent_size = len(sentence)
        sentence_text = sentence.text.strip().replace('\n', '')

        for word in sentence:
            word_score = dictionary[word.text]
            sentence_score += word_score

        sentences_verified.append((i, sentence_text, sentence_score/sent_size))

    # Returning the verified sentences based in their score and position in the obj
    return sorted(sorted(sentences_verified, key=lambda x: x[2], reverse=True), key=lambda x: x[0])


# Summarizes the text after the sentences have been verified
def Summarizer(sentences_verified, num_sents):
    summarized_text = ''

    for i in range(num_sents):
        summarized_text += sentences_verified[i][1] + ' '

    return summarized_text


# Prints text in a defined format
def printText(obj):
    print(obj)
    print('\b')
    line()

# Prints information stored in the sentences
def printSent(obj):
    print('- Sentences: \n')
    for item in obj:
        print(f'{item}\b')
    print('\b')
    line()
    print('\b')


# Prints information stored in a dictionary
def printDict(obj):
    print('\b')
    print('- Dictionary: \n')
    for item in obj:
        print(f'{item} : {obj[item]} \b')
    print('\b')
    line()
    print('\b')


def main():
    Header()
    # Loading the pipeline
    nlp = spacy.load("pt_core_news_lg")
    # Example test
    text = """O processamento de linguagem natural é um ramo da inteligência artificial
    que permite aos computadores compreender, gerar e manipular a linguagem humana.
    O processamento de linguagem natural tem a capacidade de interrogar os dados com texto
    ou voz de linguagem natural. Isso também é chamado de entrada de linguagem.
    A maioria dos consumidores provavelmente interagiu com a PNL sem perceber.
    Por exemplo, NLP é a tecnologia básica protegida por assistentes virtuais, como o
    Oracle Digital Assistant, Siri, Cortana ou Alexa. Quando fazemos perguntas sobre
    esses assistentes virtuais, o NLP é o que permite que eles não apenas entendam
    a solicitação do usuário, mas também respondam em linguagem natural."""
    # Creating a document
    doc = nlp(text)
    printText(doc)
    dictionary = createDict(doc)
    printDict(dictionary)
    sentences_verified = verifySentsScore(doc, dictionary)
    printSent(sentences_verified)
    print('- Summary: \n')
    summarized_text = Summarizer(sentences_verified, 3)
    printText(summarized_text)


main()