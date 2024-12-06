import os
import pandas as pd

csv_file_path = 'E:/qa-src.csv'
data = pd.read_csv(csv_file_path)

output_dir = 'E:/finalCsvUpdate'
os.makedirs(output_dir, exist_ok=True)  

html_page_template = """
<!DOCTYPE html>
<html lang="en">
<body>
    <div class="eurlex">
        <p class="eurlex-sti-art eurlexsolo center-text">
            <font color="#E75948">[Regulation topic] - {regulation_topic} [Question topic] - {question_topic} [Question last updated] - {last_updated}</font>
        </p>
        <p class="eurlex-sti-art eurlexsolo center-text">Question</p>
        <p class="eurlexsolo esma-qa">{question}</p>
        <p class="eurlex-sti-art eurlexsolo center-text">Answer</p>
        <p class="eurlexsolo esma-qa">{answer}</p>
    </div>
</body>
</html>
"""

html_file_paths = []
for idx, row in data.iterrows():
    file_name = f"qa_{idx + 1}.html"
    file_path = os.path.join(output_dir, file_name)
    
    html_content = html_page_template.format(
        regulation_topic=row["Regulation topic"],
        question_topic=row["Question topic"],
        last_updated=row["Last Updated"],
        question=row["Question"],
        answer=row["Answer"]
    )

    with open(file_path, 'w', encoding='utf-8') as html_file:
        html_file.write(html_content)
    
    html_file_paths.append(file_path)

print(f"Generated files are saved in: {output_dir}")
