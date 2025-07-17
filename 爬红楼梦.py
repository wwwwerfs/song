import pymysql
from fake_useragent import UserAgent
import requests
from bs4 import BeautifulSoup
import re
import time

# 数据库配置 - 创建新的数据库
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': '2487628032kg',
    'charset': 'utf8'
}

# 1. 创建数据库和表
def create_database_and_table():
    try:
        # 连接到MySQL服务器
        conn = pymysql.connect(**DB_CONFIG)
        cursor = conn.cursor()
        
        # 创建数据库
        cursor.execute("CREATE DATABASE IF NOT EXISTS hongloumeng DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci")
        print("数据库 'hongloumeng' 创建成功")
        
        # 使用新数据库
        cursor.execute("USE hongloumeng")
        
        # 创建章节表
        create_table_sql = """
        CREATE TABLE IF NOT EXISTS chapters (
            id INT AUTO_INCREMENT PRIMARY KEY COMMENT '主键ID',
            chapter_number INT NOT NULL COMMENT '章节编号',
            title VARCHAR(255) NOT NULL COMMENT '章节标题',
            content TEXT NOT NULL COMMENT '章节内容',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间'
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='红楼梦章节表'
        """
        cursor.execute(create_table_sql)
        print("表 'chapters' 创建成功")
        
        # 提交事务
        conn.commit()
        
    except pymysql.Error as e:
        print(f"数据库操作失败: {e}")
        if conn:
            conn.rollback()
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

# 2. 爬取小说内容并存入数据库
def crawl_and_store_novel():
    ua = UserAgent()
    header = {'User-Agent': ua.random}
    base_url = "https://hongloumeng.5000yan.com/"
    
    # 获取目录页
    response = requests.get(base_url, headers=header)
    if response.status_code == 200:
        response.encoding = 'utf-8'  
        content = response.text
    response.close()
    
    soup = BeautifulSoup(content, 'lxml')
    con_titles = soup.find('div', class_='container mt-md-2')
    titles = con_titles.find_all('li', class_='p-2')
    
    # 连接到新数据库
    try:
        conn = pymysql.connect(
            host='localhost',
            user='root',
            password='2487628032kg',
            database='hongloumeng',
            charset='utf8'
        )
        cursor = conn.cursor()
        
        chapter_count = 0
        
        for title in titles:
            a = title.find('a')
            if a:
                tit = a.get('title', a.get_text(strip=True))
                href = a.get('href', '')
                
                # 提取章节编号
                match = re.search(r'第([一二三四五六七八九十百]+)回', tit)
                chapter_number = 0
                if match:
                    chinese_num = match.group(1)
                    chapter_number = convert_chinese_number(chinese_num)
                else:
                    # 如果无法提取，使用递增编号
                    chapter_count += 1
                    chapter_number = chapter_count
                
                # 确保URL完整
                if not href.startswith('http'):
                    href = base_url + href.lstrip('/')
                
                # 获取章节内容
                try:
                    titlerespon = requests.get(href, headers=header)
                    if titlerespon.status_code == 200:
                        titlerespon.encoding = 'utf-8'  
                        titcontent = titlerespon.text
                        
                        titsoup = BeautifulSoup(titcontent, 'lxml')
                        content_div = titsoup.find('div', class_='grap')
                        
                        if content_div:
                            chapter_text = ""
                            for element in content_div.children:
                                if element.name == 'div':
                                    div_text = element.get_text(strip=False)
                                    # 清理多余空白和换行
                                    div_text = re.sub(r'\s+', ' ', div_text)
                                    chapter_text += div_text + "\n"
                            
                            # 插入数据库
                            insert_sql = """
                            INSERT INTO chapters (chapter_number, title, content)
                            VALUES (%s, %s, %s)
                            """
                            cursor.execute(insert_sql, (chapter_number, tit, chapter_text.strip()))
                            
                            # 提交每个章节的事务
                            conn.commit()
                            
                            print(f"成功存储: 第{chapter_number}回 - {tit}")
                    
                    titlerespon.close()
                    time.sleep(0.5)  # 添加延时防止请求过快
                    
                except Exception as e:
                    print(f"处理章节 {tit} 时出错: {e}")
        
        print("所有章节已成功存入数据库")
        
    except pymysql.Error as e:
        print(f"数据库操作失败: {e}")
        if conn:
            conn.rollback()
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

# 中文数字转阿拉伯数字的映射
chinese_to_arabic = {
    '一': 1, '二': 2, '三': 3, '四': 4, '五': 5,
    '六': 6, '七': 7, '八': 8, '九': 9, '十': 10,
    '百': 100
}

def convert_chinese_number(chinese_str):
    """将中文数字转换为阿拉伯数字"""
    if chinese_str == '十':
        return 10
    
    # 处理带"十"的数字
    if '十' in chinese_str:
        parts = chinese_str.split('十')
        if len(parts) == 1:  # 如"十"
            return 10
        elif not parts[0]:   # 如"十一"
            return 10 + chinese_to_arabic.get(parts[1], 0)
        elif not parts[1]:   # 如"二十"
            return chinese_to_arabic.get(parts[0], 0) * 10
        else:                # 如"二十一"
            return chinese_to_arabic.get(parts[0], 0) * 10 + chinese_to_arabic.get(parts[1], 0)
    
    # 处理带"百"的数字
    if '百' in chinese_str:
        parts = chinese_str.split('百')
        if len(parts) == 1:  # 如"百"
            return 100
        elif not parts[0]:   # 如"百一"
            return 100 + chinese_to_arabic.get(parts[1], 0)
        elif not parts[1]:   # 如"二百"
            return chinese_to_arabic.get(parts[0], 0) * 100
        else:                # 如"二百一十"
            return chinese_to_arabic.get(parts[0], 0) * 100 + convert_chinese_number(parts[1])
    
    # 处理个位数
    return chinese_to_arabic.get(chinese_str, 0)

# 主程序
if __name__ == "__main__":
    # 创建数据库和表
    create_database_and_table()
    
    # 爬取小说并存入数据库
    crawl_and_store_novel()
    
    print("程序执行完毕")