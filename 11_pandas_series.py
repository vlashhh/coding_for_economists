import pandas as pd
import numpy as np

ps = pd.Series(["a", 1, 2, np.pi])

print(ps)

print(type(ps))

print(type(ps.values))

print(ps[0:2])

series_1 = pd.Series(
  data = ["Schnitzel",
         "Lemonade",
         "Whiskey"],
  index = ["Food",
          "Soda",
          "Alcohol"]
)

print(series_1.loc["Food"])
print(series_1.loc[["Food", "Alcohol"]])

print(series_1[1])
print(series_1.iloc[1])

print(series_1.loc["Food":"Alcohol"])