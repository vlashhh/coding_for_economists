# Exercise: Indexing and Slicing

url = "https://github.com/codedthinking/tender-home-bias/releases/download/v1.0/ted-sample.csv"

file_name = url[-14:]
print(file_name) 

protcol = url[0:5]
print(protcol)

host_name = url[8:18]
print(host_name)


output = protcol + "://" + host_name + "/" + file_name
print(output)