
import os
import pandas as pd

file_path = 'E:/qa-src.csv' 
output_file_path = 'E:/contentIds/qa-updated.csv' 

if os.path.exists(output_file_path):
    try:
        os.rename(output_file_path, output_file_path) 
    except OSError:
        raise PermissionError(f"The file {output_file_path} is in use. Please close it and try again.")


df = pd.read_csv(file_path)
df.columns = [col.strip().lower() for col in df.columns] 

if 'qa_id' not in df.columns or 'last updated' not in df.columns:
    raise ValueError("The input CSV must contain 'QA_ID' and 'last updated' columns.")

def extract_name(content_id):
    parts = content_id.split('-')
    if len(parts) >= 2:
        return parts[1]
    return "default"  

df['content_id'] = df['qa_id'].str.lower().str.replace('.', '-', regex=False)
df['name'] = df['content_id'].apply(extract_name)
df['content_id'] = "eu/" + df['name'] + "/" + df['content_id']
df['dated_content_id'] = df['content_id'] + "/" + df['last updated']

df = df[['content_id', 'dated_content_id']]


try:
    df.to_csv(output_file_path, index=False)
    print(f"Updated CSV has been saved to {output_file_path}")
except PermissionError:
    raise PermissionError(f"Could not write to {output_file_path}. Check file permissions or close the file if open.")
