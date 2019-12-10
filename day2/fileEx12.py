import pickle

infile = open('list.pickle', 'wb')
test=[1,2,3,4,5]
pickle.dump(test, infile)
infile.close()

infile2 = open('list.pickle', 'rb')
test_pickle=pickle.load(infile2)
print(test_pickle)
infile2.close()

