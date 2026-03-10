def pig_it(text):
    text = text.split()
    words = []
    for word in text:
        if word in ['!', '?', '.', ',']:
            words.append(word)
        else:
            word = word[1:] + word[0] + 'ay'
            words.append(word)
    return ' '.join(words)