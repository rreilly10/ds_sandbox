import pandas as pd

reviews = pd.read_csv("data/ign.csv")

# print(reviews.head())
# print(reviews.iloc[:5, :])

some_reviews = reviews.iloc[10:20,]
# print(some_reviews.head())

# print(reviews[["score", "release_year"]])
#
# # PANDAS SERIES OBJECT (1D ARRAY)
# s1 = pd.Series([1,2])
# s2 = pd.Series(["Boris Yeltsin", "Mikhail Gorbachev"])
#
# print(s1)
# print(s2)
#
# df = pd.DataFrame([s1,s2])
#
# # SAME AS
#
# df = pd.DataFrame(
#     [
#         [1,2],
#         ["Boris Yeltsin", "Mikhail Gorbachev"]
#     ],
#     index=["row1", "row2"], # SPECIFIC ROW LABELS
#     columns=["column1", "column2"] # ALLOWS US TO SPECIFY COLUMN NAMES
#
# )
# print(df.loc["row1":"row2", "column1"])
#
# df = pd.DataFrame(
#     {
#         "column1": [1, "Boris Yeltsin"],
#         "column2": [2, "Mikhail Gorbachev"]
#     }
# )
#
# print(df["column1"])


# print(reviews["title"])

# print(reviews.mean())
# print(reviews["score"].mean())

# print(reviews.corr())
#
# print(reviews["score"] / 2) # Switch from 0-10 scale to 0-5 scale

score_filter = reviews["score"] > 7

xbox_one_filter = (reviews["score"] > 7) & (reviews["platform"] == "Xbox One")

# print(reviews[score_filter].head())
# print(reviews[xbox_one_filter].head())

reviews[reviews["platform"] == "Xbox One"]["score"].plot(kind="hist")
