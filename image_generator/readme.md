1. 创建scrapy项目  
`python -m scrapy startproject FigureScrapy`

2. 生成一个爬虫figure  
`python -m scrapy genspider figure figure.com`

3. 忽略日志   
在setting.py中引入  
`LOG_LEVEL = 'WARNING'`  
`ROBOTSTXT_OBEY = False`

4. 中文乱码问题   
在setting.py中引入  
`FEED_EXPORT_ENCODING = 'UTF-8'`

5. 示例教程：https://www.runoob.com/w3cnote/scrapy-detail.html；  
其中`open(filename, 'w').write(response.body)` `修改成open(filename, 'wb+').write(response.body)`

6. 运行爬虫  
`python -m scrapy crawl figure`

