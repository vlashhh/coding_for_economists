file = open('data/raw/european_commission/ted-sample.csv', "r")

headers = file.readline().strip().split(",")
file.close()

for i, head in enumerate(headers):
  print(i, head)