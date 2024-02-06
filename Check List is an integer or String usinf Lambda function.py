'''write a python code using Lambda Function
to check every element of a list is an integer or string'''

data=[1,"abc",2,"def"]

type_of_data=lambda x : type(x)

result=list(map(type_of_data, data))

print(result)
