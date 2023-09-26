# 利用LINE Notify自動傳送長輩圖到LINE群組

## 簡介
為了聯繫家人之間的感情，促進家庭和諧安寧，每日訊息上的晨昏定省是必不可少的。身為每天收到父母傳來早安圖的子女，除了默默靜音他們或是已讀不回之外，你或許渴望著其他選擇。如果你就是每天在網路上苦尋新的圖片要發給其他親友的長輩們，你或許也希望能夠迅速的尋找照片並轉發給所有人。

擁有這些困擾的人們你們有福了，只要執行這個程式，他就會自動從[👴長輩圖大全【早安區】](https://chunting.me/elder-photos-good-morning/#google_vignette)隨機下載一張照片，並且將此照片以及問候訊息傳送給所有你希望收到的人。再搭配工作排程的功能，就可以不求人每天時間到了自動幫你傳早安圖給朋友們。

本程式利用requests和BeautifulSoup等套件實作網路爬蟲，搜尋當中的img標籤從中找尋圖片的url，並隨機選取一張下載到目前工作資料夾中，在利用LINE Notify的功能將預設訊息以及圖片傳送到指定的聊天室。(注意：因為下載的照片會取名為temp.jpg，請確保程式所在的資料夾並沒有此一檔案。)

執行結果：

<img src="https://github.com/superr0ng/LINEtools/blob/main/greeting_demo.jpeg" alt="Demo picture" width="300"/>

## 使用說明
1. 安裝python。[教學連結](https://www.codingspace.school/blog/2021-04-07)
2. 安裝pip。[教學連結](https://www.maxlist.xyz/2019/07/13/pip-install-python/)
3. 利用pip安裝程式所需的套件(html5lib, requests, bs4)。在terminal或是cmd中輸入

        pip install html5lib
        pip install requests
        pip install bs4 

4. 到LINE Notify取得權杖。[教學連結](https://blog.mrat.io/%E5%A6%82%E4%BD%95%E7%94%B3%E8%AB%8Bline%E6%AC%8A%E6%9D%96%E6%8F%90%E4%BE%9B%E7%A8%8B%E5%BC%8F%E4%BA%A4%E6%98%93%E6%8E%A5%E6%94%B6%E5%8D%B3%E6%99%82%E8%A8%8A%E6%81%AF/)
5. 將Line Notify 邀請至群組中。
6. 利用文字編輯器將程式打開，並將取得權杖貼入myToken中。

        8) myToken = ["replace_this_with_your_own_token"]
7. 輸入搭配圖片傳送的訊息msg中的內容，預設是「親愛的朋友早安，祝福你有美好的一天。」
        
        42) lineNotify(token = token, msg = '親愛的朋友早安，祝福你有美好的一天。', picURI='./temp.jpg')
8. 執行程式，在terminal或cmd中輸入：
        
        python hello_my_friend.py
    Mac系統請改輸入：
    
        python3 hello_my_friend.py
## 進階排程使用
- Windows系統請參考[教學](https://pixnashpython.pixnet.net/blog/post/41511724-%E3%80%90win10%E6%8E%92%E7%A8%8B%E3%80%91%E4%BD%BF%E7%94%A8windows%E6%8E%92%E7%A8%8B%E5%99%A8%E8%AE%93python%E8%87%AA%E5%B7%B1%E5%8B%95%E8%B5%B7)
- Mac請自求多福。。。
