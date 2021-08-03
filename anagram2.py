sorted_words = []
anagrams = {}
words_in_scope  = []
sorted_inscope_words = []
words = [
  'serve', 'rival', 'lovely','caveat', 'devote', 'irving', 'livery',
  'selves', 'latvian','saviour', 'observe', 'octavian','dovetail', 'levantine'
  ]

#loop through 'words' list, sort each value and store it in sorted_words list.
for key in words:
    key = list(key)
    key.sort()
    res = ''.join(key)
    sorted_words.append(res)


#Open the file with words and store all words starting with 'v' to list words_in_scope.
with open ('./wordList.txt') as f:
    for word in f:
        if word.startswith('v'):
            words_in_scope.append((word.removeprefix('\n')).removesuffix('\n'))

#loop through the filtered words (words starting with letter 'v') and sort each value, store it in sorted_in_scope list.
for word in words_in_scope:
    new_word  = list(word)
    new_word.sort()
    res = ''.join(new_word)
    sorted_inscope_words.append(res)

#loop through the sorted list of words from above, check for anagrams 
# against the sorted_words list, store the key value pairs in dictionary anagrams.
for word in sorted_inscope_words:
    if word in sorted_words:
        anagrams[word]  = words_in_scope[sorted_inscope_words.index(word)]


print(anagrams)

