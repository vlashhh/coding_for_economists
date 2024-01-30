a = [1,2,3,1,2,1]

d = {}

for num in a:
  if not num in d:
    d[num] = 0
  d[num] += 1

print(d)

f = open('data/raw/european_commission/ted-sample.csv')

headers = f.readline().strip().split(',')

f.close()

for index, value in enumerate(headers):
    print(index, value)


data = []

with open('data/raw/european_commission/ted-sample.csv') as file:
  for line in file:
    data.append(list(line.split(",")))

print(data[0])

wins = {}

for value in data:
  countries = value[61].split("---")
  for winning_country in countries:
    if winning_country not in wins:
      wins[winning_country] = 0
  wins[winning_country] += 1

print(wins)