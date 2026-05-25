#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
每日新闻爬虫脚本
职责：1. 爬取新闻数据 2. 处理数据 3. 读取HTML模板替换内容
"""

import requests
from datetime import datetime
from bs4 import BeautifulSoup
import json
import os

NEWS_SOURCES = {
    'politics': [
        {'name': '新华网', 'url': 'http://www.xinhuanet.com/politics/'},
    ],
    'economy': [
        {'name': '新浪财经', 'url': 'https://finance.sina.com.cn/'},
    ],
    'tech': [
        {'name': '36氪', 'url': 'https://36kr.com/'},
    ],
    'military': [
        {'name': '环球军事', 'url': 'https://mil.huanqiu.com/'},
    ],
    'society': [
        {'name': '澎湃新闻', 'url': 'https://www.thepaper.cn/'},
    ]
}

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
}

def fetch_news_from_source(source):
    news_list = []
    try:
        response = requests.get(source['url'], headers=HEADERS, timeout=15)
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.text, 'html.parser')
        links = soup.find_all('a', href=True)
        
        for link in links[:80]:
            title = link.get_text(strip=True)
            href = link['href']
            
            if not title or len(title) < 8 or len(title) > 80:
                continue
            if any(keyword in title for keyword in ['广告', '推广', '专题', '直播', '视频', '图片']):
                continue
            
            if href.startswith('/'):
                base_url = '/'.join(source['url'].split('/')[:3])
                href = base_url + href
            
            news_list.append({
                'title': title,
                'source': source['name'],
                'url': href
            })
            if len(news_list) >= 6:
                break
                
    except Exception as e:
        print(f"爬取 {source['name']} 失败: {str(e)[:50]}")
    
    return news_list

def fetch_all_news():
    all_news = {}
    for category, sources in NEWS_SOURCES.items():
        category_news = []
        for source in sources:
            news = fetch_news_from_source(source)
            category_news.extend(news)
        
        seen = set()
        unique_news = []
        for news in category_news:
            if news['title'] not in seen:
                seen.add(news['title'])
                unique_news.append(news)
        
        all_news[category] = unique_news[:5]
        print(f"✅ {category}: {len(unique_news[:5])} 条")
    
    return all_news

def get_fallback_news():
    return {
        'politics': [
            {'title': '新华社评论：推动高质量发展取得新成效', 'source': '新华网', 'url': '#'},
            {'title': '人民日报署名文章：中国式现代化是走和平发展道路的现代化', 'source': '人民网', 'url': '#'},
        ],
        'economy': [
            {'title': '中国经济韧性强活力足长期向好基本面不会改变', 'source': '经济日报', 'url': '#'},
            {'title': '金融支持实体经济力度持续加大', 'source': '证券时报', 'url': '#'},
        ],
        'tech': [
            {'title': '我国人工智能产业加速发展应用场景不断拓展', 'source': '科技日报', 'url': '#'},
            {'title': '新能源技术取得突破绿色转型步伐加快', 'source': 'IT之家', 'url': '#'},
        ],
        'military': [
            {'title': '国防和军队现代化建设迈出坚实步伐', 'source': '解放军报', 'url': '#'},
        ],
        'society': [
            {'title': '民生保障水平稳步提升人民群众获得感幸福感增强', 'source': '光明日报', 'url': '#'},
        ]
    }

def update_html_template(news_data):
    date_str = datetime.now().strftime("%Y年%m月%d日")
    
    category_map = {
        'politics': {'id': 'politics', 'name': '国际政治', 'icon': '🇨🇳'},
        'economy': {'id': 'economy', 'name': '财经经济', 'icon': '💰'},
        'tech': {'id': 'tech', 'name': 'AI科技', 'icon': '🤖'},
        'military': {'id': 'military', 'name': '军事安全', 'icon': '⚔️'},
        'society': {'id': 'society', 'name': '人文社会', 'icon': '🌍'}
    }
    
    news_items_html = {}
    news_details_js = {}
    news_id = 1
    
    for cat_key, cat_info in category_map.items():
        items = []
        for news in news_data.get(cat_key, []):
            item_html = f'''<div class="news-item" onclick="window.location.href='news-detail.html?n={news_id}'">
                <div class="news-title">{news['title']}</div>
                <span class="news-source">{news['source']}</span>
                <p>{news['title'][:40]}...</p>
            </div>'''
            items.append(item_html)
            
            news_details_js[news_id] = {
                'title': news['title'].replace("'", "\\'"),
                'source': news['source'],
                'url': news['url'],
                'cat': cat_key
            }
            news_id += 1
        
        if not items:
            items = ['<p style="color:#95a5a6;padding:20px;">暂无新闻</p>']
        
        news_items_html[cat_key] = '\n'.join(items)
    
    js_parts = []
    for idx, data in news_details_js.items():
        js_parts.append(f"{idx}: {{title: '{data['title']}', source: '{data['source']}', url: '{data['url']}', cat: '{data['cat']}'}}")
    js_news_data = ',\n            '.join(js_parts)
    
    html_path = os.path.join(os.path.dirname(__file__), 'daily-news.html')
    detail_path = os.path.join(os.path.dirname(__file__), 'news-detail.html')
    
    with open(html_path, 'r', encoding='utf-8') as f:
        main_html = f.read()
    
    main_html = main_html.replace('{{DATE}}', date_str)
    for cat in category_map:
        placeholder = f'{{{{NEWS_{cat.upper()}}}}}'
        main_html = main_html.replace(placeholder, news_items_html.get(cat, ''))
    
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(main_html)
    print("✅ daily-news.html 已更新")
    
    with open(detail_path, 'r', encoding='utf-8') as f:
        detail_html = f.read()
    
    if '// {{NEWS_DATA_PLACEHOLDER}}' in detail_html:
        detail_html = detail_html.replace('// {{NEWS_DATA_PLACEHOLDER}}', js_news_data if js_news_data else '1: {}')
    
    with open(detail_path, 'w', encoding='utf-8') as f:
        f.write(detail_html)
    print("✅ news-detail.html 已更新")

def main():
    print("="*50)
    print(f"📰 每日新闻更新 - {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print("="*50)
    
    try:
        news_data = fetch_all_news()
        total = sum(len(v) for v in news_data.values())
        if total < 5:
            print("⚠️ 爬取新闻太少，使用备用数据")
            news_data = get_fallback_news()
    except Exception as e:
        print(f"⚠️ 爬取出错: {str(e)}，使用备用数据")
        news_data = get_fallback_news()
    
    update_html_template(news_data)
    print("\n🎉 更新完成！")

if __name__ == "__main__":
    main()
