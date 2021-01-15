# pythonPDFDemo
打开pdf文档以及txt文档等等

* 编译器:PyCharm

* Python版本:3.8/3.9

* 涉及到的库:pdfminer3、json、requests、multiprocessing - Process，Queue、threading - Thread、threading - Lock、smtplib、email、urllib.parse、http.client、PIL - Image，ImageFilter、openpyxl、python-docx

* 使用的功能:

  - 发送邮件，并带有附件 （smtplib、email）
  - 网络请求 （json、requests）
  - 写入文件
  - 读取pdf文件 （pdfminer3）
  - 建立进程 （multiprocessing - Process）
  - 建立线程 （threading - Thread）
  - 使用锁和线程搭配 （threading - Thread、threading - Lock）
  - 利用多进程进行数据切片 （multiprocessing - Process，Queue）
  - 发送短信验证码（urllib.parse、http.client）：使用[互亿无线](http://www.ihuyi.com)的接口
  - 裁剪、缩放、旋转图片等，对图片加滤镜 （PIL - Image，ImageFilter）
  - 生成xlsx和word文档 （openpyxl、python-docx）
  
