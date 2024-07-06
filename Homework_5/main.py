import requests
import re
import json
import sqlite3

url = 'https://www.lejobadequat.com/emplois'

#def get_content(url):
    # response = requests.get(url)

    # with open('filename', 'w', encoding='utf-8') as f:
        # f.write(response.text)

with open('filename', 'r', encoding='utf-8') as f:
    content = f.read()

    # print(content)

def get_jobs(content):
    jobnames_list = re.findall(r'<h3 class="jobCard_title">(.*?)<\/h3>', content)
    joblinks_list = re.findall(r'<a[^>]*href="([^"]+)"[^>]*class="jobCard_link"[^>]*>', content, re.DOTALL)
    # print(jobnames_list)
    # print(joblinks_list)

    filename = 'homework5_result.json'
    data = [
        {'jobname': re.sub(r'&#\d+;|&[a-zA-Z0-9#]+;', "", job_name), 'job_link': job_link} for job_name, job_link in zip(jobnames_list, joblinks_list)
    ]

    json_data = json.dumps(data, ensure_ascii=False, indent=4)

    # with open('homework5_result.json', 'w', encoding='utf-8') as file:
        # file.write(json_data)

with open('homework5_result.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

def write_sqlite():
    filename = 'jobs.db'

    # Connect to SQLite database (creates file if it doesn't exist)
    conn = sqlite3.connect(filename)
    cursor = conn.cursor()

    # Create table if it does not exist
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS jobs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        jobname TEXT,
        job_link TEXT
    )
    ''')

    # Insert JSON data into the table
    cursor.executemany('''
    INSERT INTO jobs (jobname, job_link)
    VALUES (?, ?)
    ''', [(entry['jobname'], entry['job_link']) for entry in data])

    # Commit changes and close connection
    conn.commit()
    conn.close()

if __name__ == '__main__':
    #get_content(url)
    #get_jobs(content)
    write_sqlite()
    #check_table()

