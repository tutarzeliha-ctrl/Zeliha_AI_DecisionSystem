import pandas as pd
from pdf_generator import create_bilingual_pdf
from analyze_event_module import analyze_event  # Eğer ayrı dosyada ise

def full_pipeline(df):
    df_ai = df["trigger"].apply(analyze_event)
    df_ai = pd.DataFrame(df_ai.tolist())

    if "trigger" in df_ai.columns:
        df_ai = df_ai.drop(columns=["trigger"])

    df_clean = pd.concat([df, df_ai], axis=1)

    pdf_file = create_bilingual_pdf(df_clean)

    return df_clean, pdf_file

if __name__ == "__main__":
    df = pd.read_csv("data/logs.csv")
    df_clean, pdf_file = full_pipeline(df)
    print("Pipeline tamamlandı. PDF oluşturuldu:", pdf_file)
