import pandas as ma
from pathlib import Path
from datetime import datetime


data = ma.read_csv("data/raw/kerala_malayalam_news_supervised.csv", encoding="utf-8")
print(data.head())

print("Dataset Shape:", data.shape)
print("Columns in dataset:", data.columns.tolist())
print("Missing values in dataset:", data.isnull().sum())

def load_news(path):
    """
    Load Malayalam news articles from a CSV file.
    """
    data = ma.read_csv(path, encoding="utf-8")
    return data

def clean_news(data):
    """
    Fill missing publication dates with Unknown.
    """
    data = data.copy()
    data["published_date"] = data["published_date"].fillna("Unknown")
    return data   

def save_cleaned_news(cleaned_data, original_data):
    output_dir = Path("data/processed")
    output_dir.mkdir(parents=True, exist_ok=True)
    output_file = output_dir / "clean_kerala_news.csv"
    cleaned_data.to_csv(output_file, index=False, encoding="utf-8")
    audit_file = output_dir / "news_ingestion_audit.log"
    with open(audit_file, "a", encoding="utf-8") as log:
        log.write(f"Date and time: {datetime.now()}\n")
        log.write(f"Total articles in before cleaning: {len(original_data)}\n")
        log.write(f"Total articles after cleaning: {len(cleaned_data)}\n")
        log.write(f"Missing values before cleaning: {original_data['published_date'].isnull().sum()}\n")
        log.write(f"Missing values after cleaning: {cleaned_data['published_date'].isnull().sum()}\n")

    print("Cleaned dataset saved successfully!")
    print("Audit log saved successfully!")    

if __name__ == "__main__":
    news = load_news("data/raw/kerala_malayalam_news_supervised.csv")
    cleaned_news = clean_news(news)
    save_cleaned_news(cleaned_news, news)
    print("Loaded news articles:", len(news))
    print("Cleaned news articles:", len(cleaned_news))
    print("Missing values after cleaning:", cleaned_news.isnull().sum())
    print("Missing dates row:")
    print(news[news["published_date"].isnull()])
