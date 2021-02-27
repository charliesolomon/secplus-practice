import pdftotext
import csv

# Extract text from Security+ practice test PDF file, split the questions/answers and export to a CSV
# that can be imported to flash card apps

# Load your PDF
with open("../security+501/NEW2020Test/NEWEST/secplus-2021-0121-practice-test.pdf", "rb") as f:
    pdf = pdftotext.PDF(f)

# How many pages?
print(len(pdf))

# Old 501 questions: 
# Initialize page numbers to extract
min = 1
max = 102

# Split questions into a list (includes answers)
str = ''
for i in range(min,max):
    str = str + pdf[i] 
joined = str.split('QUESTION ')
print(len(joined)) # total number of questions found

# check first/last with print statements to make sure we have the data:
#print(joined[1])
#print(joined[len(joined)-1])
# (first element is title, ignore)

# Split each element in list into question/answer pair
# ignore first element, it's not a question
export = []
for question in joined:
    qna = question.split('Correct Answer: ')
    # add the QUESTION and Correct Answer: text back in (it was stripped out when we used "split")
    if len(qna) > 1:
        export.append(['QUESTION '+qna[0], 'Correct Answer: '+qna[1]])

print('Finished!!\n\n')
#print(export[0][0])
#print(export[0][1])

# Dump it out to CSV
with open('export.csv', 'w') as f: 
    write = csv.writer(f)
    write.writerows(export)

# New 501 questions: (todo)
#print(pdf[102])

# New 601 questions: (todo)
#print(pdf[217])

