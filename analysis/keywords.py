import pandas as pd
import re
import os

keyword_file = os.path.join("data", "SG Red Cross Society - Keywords.xlsx")

def load_keywords(file_path):
  
    xls = pd.ExcelFile(file_path)
    keywords = {}

    for sheet in xls.sheet_names:
        df = xls.parse(sheet)

        col_lower = [c.lower() for c in df.columns]
        if "keyword" in col_lower:
            col = df.columns[col_lower.index("keyword")]
            words = df[col].dropna().astype(str).tolist()
        else:
           
            words = df.iloc[:, 0].dropna().astype(str).tolist()

        keywords[sheet] = words

    return keywords


def build_patterns(keywords_dict):
    
    patterns = {}
    for category, words in keywords_dict.items():
        pattern = re.compile(r"\b(?:{})\b".format("|".join(re.escape(w) for w in words)), flags=re.I)
        patterns[category] = pattern
    return patterns


def tag_text(text, patterns):

    tags = []
    for category, pattern in patterns.items():
        if pattern.search(text):
            tags.append(category)
    return tags



if __name__ == "__main__":
    keywords = load_keywords(keyword_file)
    print("Loaded keywords:", keywords)  
    
  