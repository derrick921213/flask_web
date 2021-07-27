# _*使用 python 控制服務器 (重製版)*_

### **原始碼在 docker 資料夾下**

## 需求

- <a href="https://git-scm.com/downloads">Git</a>
- <a href="https://www.python.org/">python3</a>
- <a href="https://medium.com/tsungs-blog/python-%E8%AE%93pipenv-%E5%B9%AB%E4%BD%A0%E5%81%9A%E5%A5%97%E4%BB%B6%E7%AE%A1%E7%90%86-bb284e865dc1">pipenv</a>
- <a href="https://www.docker.com/get-started">Docker</a>

## 安裝

1. 第一步
   1. 確定 **Docker daemon** 在執行中.
   2. 複製這個倉儲
2. 第二步
   1. 更改目錄至 first_install `cd first_install`
   2. 執行 Shell 腳本 `./install.sh`

## 解除安裝

- 執行 Shell 腳本 `./uninstall.sh`

## 自行編譯

1. 第一步
   1. 確定 <a href="https://medium.com/tsungs-blog/python-%E8%AE%93pipenv-%E5%B9%AB%E4%BD%A0%E5%81%9A%E5%A5%97%E4%BB%B6%E7%AE%A1%E7%90%86-bb284e865dc1">**pipenv**</a> 已經安裝在系統上了
2. 第二部
   1. 打開終端機, 切到本專案的目錄下.
   2. 在終端機內打上`pipenv --python 3.8 install`
   3. 如果程序完成, 就可以接著打 `pipenv shell`, 之後你就可自己編譯代碼
3. ### _*恭喜!!!*_
