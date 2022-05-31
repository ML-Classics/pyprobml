"""
This code read the internal/chapter_no_to_name_mapping_book2.csv generated by internal/book2/chapter_mapping_from_toc.py.
"""
import pandas as pd

df = pd.read_csv("internal/chapter_no_to_name_mapping_book2.csv")
df["Notebook"] = df["chap_no"].apply(lambda x: f"[{x:02d}/]({x:02d}/)")

md = "# Probabilistic Machine Learning: Advanced Topics\n\n## Chapters\n\n" + df.to_markdown(index=False)
with open("notebooks/book2/README.md", "w") as fp:
    fp.write(md)