import pandas as pd

# file=pd.read_csv(r"D:\ITI\datawarehouse\full project snow python power bi\tmdb_project\fact.csv")

# df = file.drop_duplicates(subset=["date_key"],keep="first")
# duplicates = df[df.duplicated(subset=["date_key"])]
# print(duplicates)


# df.to_csv("fact_trending_titles.csv", index=False)



# Load CSV
df = pd.read_csv(r"D:\ITI\datawarehouse\full project snow python power bi\tmdb_project\date.csv")
df2 = pd.read_csv(r"D:\ITI\datawarehouse\full project snow python power bi\tmdb_project\fact_trending_titles.csv")
# Specify the column and character to remove
column_name = "date_key"
char_to_remove = "_"

# Remove the character from that column
df[column_name] = df[column_name].astype(str).str.replace(char_to_remove, "", regex=False)
print(df.head())

# Remove the character from that column
df2[column_name] = df2[column_name].astype(str).str.replace(char_to_remove, "", regex=False)
print(df2.head())



df.to_csv("cleaned_file_dim_date.csv", index=False)
df2.to_csv("fact_trending_titles.csv", index=False)
