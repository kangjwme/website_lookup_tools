from flask import Flask, request, render_template, redirect, url_for
import subprocess
import urllib.parse
import json
import uuid
from datetime import datetime

app = Flask(__name__)

# 定義存儲查詢結果的 JSON 文件路徑
QUERY_RESULTS_FILE = 'query_results.json'

# 如果 JSON 文件不存在，則創建一個空的列表來存儲查詢結果
try:
    with open(QUERY_RESULTS_FILE, 'r') as f:
        query_results = json.load(f)
except FileNotFoundError:
    query_results = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form['url']
        
        # 如果使用者只輸入主機名，加上 https:// 前綴
        if not url.startswith('http://') and not url.startswith('https://'):
            url = 'https://' + url
        
        parsed_url = urllib.parse.urlparse(url)
        domain = parsed_url.hostname
        
        try:
            # 獲取Response Headers
            headers = subprocess.check_output(['curl', '-sI', url]).decode('utf-8').strip()
            
            # 使用本機的 whois 命令獲取 whois 資訊
            whois_info = subprocess.check_output(['whois', domain]).decode('utf-8')

            nslookup_info = subprocess.check_output(['nslookup', domain, '8.8.8.8']).decode('utf-8')
            
            # 生成唯一ID
            query_id = str(uuid.uuid4())
            
            # 添加到查詢結果列表
            query_results.append({
                "id": query_id,
                "url": url,
                "whois": whois_info,
                "headers": headers,
                "hostname": domain,
                "nslookup": nslookup_info,
                "query_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            })
            
            # 將查詢結果保存到 JSON 文件中
            with open(QUERY_RESULTS_FILE, 'w') as f:
                json.dump(query_results, f, indent=4)
            
            # 重定向到該結果路徑
            return redirect(url_for('result', query_id=query_id))
            
        except Exception as e:
            print(e)
            return render_template('index.html', error_message="未知的網址或網域")
    return render_template('index.html')

@app.route('/domain/<query_id>')
def result(query_id):
    for result in query_results:
        if result['id'] == query_id:
            return render_template('result.html', result=result)
    return render_template('index.html', error_message="查無此紀錄")

if __name__ == '__main__':
    app.run(debug=True)
