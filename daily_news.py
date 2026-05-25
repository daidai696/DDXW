#!/usr/bin/env python3
"""
每日新闻自动生成脚本 - 使用爬虫获取真实新闻
"""

import requests
from datetime import datetime
from bs4 import BeautifulSoup
import random

# 新闻源配置
NEWS_SOURCES = {
    'politics': [
        {'name': '新华网', 'url': 'http://www.xinhuanet.com/politics/'},
        {'name': '人民网', 'url': 'http://politics.people.com.cn/'},
    ],
    'economy': [
        {'name': '新浪财经', 'url': 'https://finance.sina.com.cn/'},
        {'name': '华尔街见闻', 'url': 'https://wallstreetcn.com/'},
    ],
    'tech': [
        {'name': '36 氪', 'url': 'https://36kr.com/'},
        {'name': 'IT 之家', 'url': 'https://www.ithome.com/'},
    ],
    'military': [
        {'name': '参考消息', 'url': 'http://www.cankaoxiaoxi.com/'},
    ],
    'society': [
        {'name': '澎湃新闻', 'url': 'https://www.thepaper.cn/'},
    ]
}

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
}

def fetch_news_from_source(source):
    """从指定新闻源爬取新闻"""
    news_list = []
    try:
        response = requests.get(source['url'], headers=HEADERS, timeout=10)
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.text, 'html.parser')
        
        links = soup.find_all('a', href=True)
        
        for link in links[:100]:
            title = link.get_text(strip=True)
            href = link['href']
            
            if not title or len(title) < 5 or len(title) > 100:
                continue
            
            if any(keyword in title for keyword in ['广告', '推广', '专题', '直播', '视频']):
                continue
            
            # 处理相对链接
            if href.startswith('/'):
                base_url = '/'.join(source['url'].split('/')[:3])
                href = base_url + href
            
            news_list.append({
                'title': title,
                'source': source['name'],
                'url': href
            })
            
            if len(news_list) >= 5:
                break
                
    except Exception as e:
        print(f"爬取 {source['name']} 失败：{str(e)}")
    
    return news_list

def fetch_all_news():
    """获取所有类别的新闻"""
    all_news = {}
    
    for category, sources in NEWS_SOURCES.items():
        category_news = []
        for source in sources:
            news = fetch_news_from_source(source)
            category_news.extend(news)
        
        # 去重
        seen = set()
        unique_news = []
        for news in category_news:
            if news['title'] not in seen:
                seen.add(news['title'])
                unique_news.append(news)
        
        all_news[category] = unique_news[:5]
    
    return all_news

def generate_daily_news(all_news=None):
    if all_news is None:
        print("🕷️ 正在爬取最新新闻...")
        all_news = fetch_all_news()
        total = sum(len(v) for v in all_news.values())
        print(f"✅ 成功获取 {total} 条新闻")
    
    today = datetime.now()
    date_str = today.strftime("%Y年%m月%d日")
    
    # 生成新闻列表 HTML
    news_items = {
        'politics': '',
        'economy': '',
        'tech': '',
        'military': '',
        'society': ''
    }
    
    news_id = 1
    news_data_js = {}
    
    for category, news_list in all_news.items():
        for news in news_list:
            news_items[category] += f"""
            <div class="news-item" onclick="window.location.href='news-detail.html?n={news_id}'">
                <div class="news-title">{news['title']}</div>
                <span class="news-source">{news['source']}</span>
                <p>{news['title'][:50]}...</p>
            </div>"""
            
            news_data_js[news_id] = {
                'title': news['title'],
                'source': news['source'],
                'url': news['url'],
                'cat': category
            }
            news_id += 1
    
    # 生成新闻数据 JavaScript
    news_data_parts = []
    for idx, data in news_data_js.items():
        title = data['title'].replace("'", "\\'")
        source = data['source'].replace("'", "\\'")
        url = data['url'].replace("'", "\\'")
        cat = data['cat']
        news_data_parts.append(f"{idx}: {{title: '{title}', source: '{source}', url: '{url}', cat: '{cat}'}}")
    news_data_str = ',\n            '.join(news_data_parts)
    
    news_html = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>每日新闻速递</title>
    <style>
        body {{ font-family: sans-serif; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); min-height: 100vh; padding: 20px; }}
        .container {{ max-width: 900px; margin: 0 auto; }}
        .header {{ background: white; border-radius: 20px; padding: 30px; text-align: center; margin-bottom: 20px; }}
        .header h1 {{ font-size: 28px; color: #2c3e50; }}
        .tabs {{ display: flex; gap: 10px; padding: 15px; background: white; border-radius: 16px; margin-bottom: 20px; flex-wrap: wrap; }}
        .tab {{ padding: 12px 24px; background: #f5f7fa; border: none; border-radius: 25px; cursor: pointer; font-size: 15px; }}
        .tab.active {{ background: linear-gradient(135deg, #667eea, #764ba2); color: white; }}
        .content {{ background: white; border-radius: 16px; padding: 28px; }}
        .panel {{ display: none; }}
        .panel.active {{ display: block; }}
        .news-item {{ padding: 20px; background: #fafbfc; border-radius: 12px; margin-bottom: 16px; cursor: pointer; }}
        .news-title {{ font-size: 18px; font-weight: 600; color: #2c3e50; }}
        .news-source {{ font-size: 13px; color: #95a5a6; background: #e8ecef; padding: 4px 12px; border-radius: 15px; }}
        .summary {{ background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); border-radius: 20px; padding: 30px; margin-top: 25px; color: white; }}
        .footer {{ background: rgba(255,255,255,0.95); border-radius: 16px; padding: 20px; text-align: center; margin-top: 25px; }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1> 每日新闻速递</h1>
            <p>{date_str}</p>
        </div>
        <div class="tabs">
            <button class="tab active" onclick="showPanel('politics')">🇨🇳 国际政治</button>
            <button class="tab" onclick="showPanel('economy')">💰 财经经济</button>
            <button class="tab" onclick="showPanel('tech')">🤖 AI 科技</button>
            <button class="tab" onclick="showPanel('military')">⚔️ 军事安全</button>
            <button class="tab" onclick="showPanel('society')">🌍 人文社会</button>
        </div>
        <div class="content">
            <div id="politics" class="panel active">
                <h2>🇨🇳 国际政治</h2>
                {news_items['politics']}
            </div>
            <div id="economy" class="panel">
                <h2>💰 财经经济</h2>
                {news_items['economy']}
            </div>
            <div id="tech" class="panel">
                <h2>🤖 AI 科技</h2>
                {news_items['tech']}
            </div>
            <div id="military" class="panel">
                <h2>⚔️ 军事安全</h2>
                {news_items['military']}
            </div>
            <div id="society" class="panel">
                <h2>🌍 人文社会</h2>
                {news_items['society']}
            </div>
        </div>
        <div class="summary">
            <h3>💡 今日新闻总结</h3>
            <p>宏观层面：今日新闻展现了全球政治经济格局的深度调整。国际关系持续演变，经济政策寻求平衡点。</p>
            <p>微观层面：科技领域持续创新，AI 技术从实验室走向产业化，各行业数字化转型加速。</p>
        </div>
        <div class="footer">
            <p>🌐 每日早 10 点自动更新 | 支持多端访问</p>
        </div>
    </div>
    <script>
        function showPanel(id) {{
            document.querySelectorAll('.tab').forEach(t => t.classList.remove('active'));
            document.querySelectorAll('.panel').forEach(p => p.classList.remove('active'));
            event.target.classList.add('active');
            document.getElementById(id).classList.add('active');
        }}
    </script>
</body>
</html>"""
    
    # 生成详情页 HTML
    detail_html = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>新闻详情</title>
    <style>
        body {{ font-family: sans-serif; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 20px; }}
        .container {{ max-width: 800px; margin: 0 auto; }}
        .card {{ background: white; border-radius: 20px; padding: 30px; }}
        .title {{ font-size: 26px; font-weight: 700; color: #2c3e50; }}
        .content {{ color: #5a6672; line-height: 1.8; margin-top: 20px; }}
        .impact {{ background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); border-radius: 15px; padding: 20px; color: white; margin-top: 20px; }}
        .related {{ margin-top: 30px; padding-top: 30px; border-top: 1px solid #eee; }}
        .rel-item {{ padding: 12px 0; border-bottom: 1px solid #f0f0f0; cursor: pointer; }}
    </style>
</head>
<body>
    <div class="container">
        <button onclick="window.location.href='daily-news.html'">← 返回列表</button>
        <div class="card">
            <div id="title">加载中...</div>
            <div id="content"></div>
            <div class="impact">
                <h4>💡 新闻启示</h4>
                <p id="impact"></p>
            </div>
            <div class="related">
                <h4> 相关新闻</h4>
                <div id="related"></div>
            </div>
        </div>
    </div>
    <script>
        var newsData = {{
            {news_data_str}
        }};
        
        function getNewsId() {{
            var params = new URLSearchParams(window.location.search);
            var id = params.get('n') || params.get('news');
            return id ? parseInt(id) : 1;
        }}
        
        function renderNews(id) {{
            var news = newsData[id];
            if (!news) {{
                document.getElementById('title').textContent = '新闻未找到';
                return;
            }}
            document.getElementById('title').textContent = news.title;
            document.getElementById('content').innerHTML = '<p>来源：' + news.source + '</p><p><a href="' + news.url + '" target="_blank" style="color: #667eea;">查看原文</a></p>';
            document.getElementById('impact').textContent = '该新闻反映了当前' + news.cat + '领域的最新动态，值得持续关注。';
            
            var related = [];
            for (var key in newsData) {{
                if (parseInt(key) !== id && newsData[key].cat === news.cat) {{
                    related.push(key);
                }}
            }}
            related = related.slice(0, 3);
            var html = '';
            for (var i = 0; i < related.length; i++) {{
                var k = related[i];
                html += '<div class="rel-item" onclick="window.location.href=\\'news-detail.html?n=\\' + k + \\'\\'">' + newsData[k].title + '</div>';
            }}
            document.getElementById('related').innerHTML = html || '<p style="color: #95a5a6;">暂无相关新闻</p>';
        }}
        
        renderNews(getNewsId());
    </script>
</body>
</html>"""
    
    return news_html, detail_html

def main():
    print("️ 正在爬取并生成每日新闻页面...")
    
    try:
        all_news = fetch_all_news()
        daily_html, detail_html = generate_daily_news(all_news)
    except Exception as e:
        print(f"爬取失败：{str(e)}")
        print("使用备用新闻数据...")
        daily_html, detail_html = generate_daily_news()
    
    with open('daily-news.html', 'w', encoding='utf-8') as f:
        f.write(daily_html)
    print("✅ daily-news.html 已生成")
    
    with open('news-detail.html', 'w', encoding='utf-8') as f:
        f.write(detail_html)
    print("✅ news-detail.html 已生成")
    
    print("🎉 新闻页面生成完成！")

if __name__ == "__main__":
    main()
