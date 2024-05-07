# 網站資訊查詢
使用 Python flask X subprocess 做出來的小網站，可以利用本機端指令 whois、curl 跟 nslookup 查詢網站 Response Header、WHOIS 跟 DNS lookup

## 程式預覽
<img width="872" alt="image" src="https://github.com/kangjwme/website_lookup_tools/assets/71870130/5e206d57-bff9-44d9-b550-9a4953997a02">
<img width="1362" alt="image" src="https://github.com/kangjwme/website_lookup_tools/assets/71870130/bae42141-ef90-4900-89db-9c4b64ca0592">

<img width="1021" alt="image" src="https://github.com/kangjwme/website_lookup_tools/assets/71870130/63301af8-9921-4a5b-9842-414d9fe33eb3">

## 程式功能
- 針對網站（或網域）進行 Response Header、Whois 和 nslookup 查詢跟顯示，並且增加歷史紀錄（暫時用 json，懶得用 db）可以透過指定 uuid 去存取歷史訊息
## 使用說明
安裝必要套件後，直接執行 `app.py` 或是在資料夾中執行 `flask run` 即可，之後可利用 http://localhost:5000 連線到網站
