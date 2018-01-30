text = raw_input("Enter text string: ")
searchString = raw_input("Enter search string: ")

def makePattern(search):
	searchLen = len(search)
	result = [0]*searchLen

	maxPreLen = 0
	result[0] = maxPreLen
	i = 1
	while (i < searchLen):
		if(search[i] == search[maxPreLen]):
			maxPreLen += 1
			result[i] = maxPreLen
			i += 1
		else:
			if(maxPreLen!=0):
				maxPreLen = result[maxPreLen-1]
			else:
				result[i] = 0
				i += 1
	return result

def KmpMatch(text, search):
	pattern = makePattern(search)
	results = list()
	M = len(search)
	N = len(text)
	i = 0
	j = 0
	while(i<N):
		if(text[i] == search[j]):
			i+=1
			j+=1

		if(j==M):
			results.append(i-j)
			j = pattern[j-1]
			print 'match at index' + str(i-j)

		elif(i<N and search[j] != text[i]):
			if(j):
				j = pattern[j-1]
			else:
				i+=1
	return results


print KmpMatch(text, searchString)
# print makePattern(searchString)
