file = open('data/raw/european_commission/ted-sample.csv')

print(file.readline())
print(file.readline())
            
file.close()

with open('data/raw/european_commission/ted-sample.csv') as file:
  for line in file:
    print(line)