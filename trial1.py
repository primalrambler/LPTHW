sentence1 = "word1,word2,word3,word4"
sentence2 = "word1 word2 word3 word4"
sentence3 = "word1\tword2\tword3\nword4"

print sentence1.split(',')
print sentence2.split()
print sentence3.split('\t')