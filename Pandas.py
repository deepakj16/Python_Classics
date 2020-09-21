# pd.read_csv("f500.csv", index_col=0) , index_col would be used to index or refer the row
# type(df), df.info(), df.shape, df.tail(), df.head(), df.dtypes
# df.loc[:,"col2"], df[["col1","col2"]], df.loc[:,"col1":"col2"]
# can use index col df.loc["row1"]
# Series.value_counts(), df["col1"].value_counts()
# df["col1"].loc["items8"], df["col1"].loc["items8","item9"],df["col1"]["items8","item9"], S.loc[2:4], S[2:4]

import pandas as pd

tst=pd.DataFrame()

tst.info()