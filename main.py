import pandas as pd
df = pd.read_csv("Players.csv")

# Bring the first 10 records.
result = df.head(10)
print(result)

# How many records are there in total?
result = len(df.index)
print(result)

# What is the average height of the players?
result = df["height"].mean()
print(result)

# How much does the heaviest player weigh?
result = df["weight"].max()
print(result)

# What is the information of the tallest player?
result = df[df["height"] == df["height"].max()]["Player"].iloc[0]
print(result)

# Get the record of players born 1920 to 1930.
result = df[(df["born"] >= 1920) & (df["born"] < 1930)][["Player","born","birth_city"]].sort_values("born", ascending=False)
print(result)

# What is the birth date of the actor named "Gene Berce"?
result = df[df["Player"] == "Gene Berce"].iloc[0]
print(result)

# What is the average height information by years?
result = df.groupby("born").mean()["height"]
print(result)

# How many different schools are there?
result = df["collage"].unique()
print(result)

# How many players are in each school?
result = df["collage"].value_counts()
print(result)

# List players whose names contain the word "jo".
df = df.dropna()
def str_find(name):
    if "jo" in name.lower():
        return True
    return False
result = df[df["Player"].apply(str_find)]
print(result)
