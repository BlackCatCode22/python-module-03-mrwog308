##################################################
#                                                #
#   Exercise 5: Slicing strings (work_ex_6_5)    #
#                                                #
##################################################

str = 'X-DSPAM-Confidence: 0.8475'
index = str.find(':')
# print(str[index + 1:])
# print(str[index + 1:].strip())
num = float(str[index + 1:].strip())
print(num, type(num))