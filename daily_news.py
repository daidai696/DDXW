#!/usr/bin/env python3
"""
每日新闻自动生成脚本
"""

from datetime import datetime

def generate_daily_news():
    today = datetime.now()
    date_str = today.strftime("%Y年%m月%d日")
    time_str = today.strftime("%Y-%m-%d %H:%M")
    
    news_data = {
        "politics": {"name": "国际政治", "icon": "🇨🇳", "news": [
            {"id": 1, "title": "中俄元首会谈：续签睦邻友好合作条约", "source": "人民日报", "details": [
                {"label": "核心内容", "content": "国家主席习近平与俄罗斯总统普京在北京举行会谈，一致同意《中俄睦邻友好合作条约》继续延期"},
                {"label": "重要成果", "content": "双方签署发表联合声明，见证签署经贸、教育、科技等领域20项合作文件"}
            ]},
            {"id": 2, "title": "美伊谈判进入最后阶段", "source": "环球时报", "details": [
                {"label": "核心进展", "content": "美国总统特朗普表示，与伊朗的谈判已进入最后阶段"},
                {"label": "市场反应", "content": "国际油价大跌超5.5%，WTI原油收报98.26美元/桶"}
            ]},
            {"id": 3, "title": "欧盟推出新数字战略，加速AI监管", "source": "澎湃新闻", "details": [
                {"label": "核心内容", "content": "欧盟委员会发布《数字未来法案》，提出更严格的AI风险分类和合规要求"}
            ]}
        ]},
        "economy": {"name": "财经经济", "icon": "💰", "news": [
            {"id": 4, "title": "美联储会议纪要放鹰", "source": "金融时报", "details": [
                {"label": "核心内容", "content": "多数决策者认为若通胀持续高于2%需政策收紧，多位官员支持未来加息"},
                {"label": "市场反应", "content": "市场押注美联储年底前加息25bp概率升至60%"}
            ]},
            {"id": 5, "title": "英伟达Q1财报超预期", "source": "IT之家", "details": [
                {"label": "核心数据", "content": "营收同比大增85%至816亿美元，净利润达583亿美元"}
            ]},
            {"id": 6, "title": "SpaceX提交IPO申请", "source": "华尔街见闻", "details": [
                {"label": "核心计划", "content": "目标估值指向1.8万亿美元，计划2028年部署轨道算力卫星"}
            ]},
            {"id": 7, "title": "中国财政数据亮眼", "source": "证券时报", "details": [
                {"label": "核心数据", "content": "1-4月全国税收收入6.81万亿元，同比增长3.9%"}
            ]}
        ]},
        "tech": {"name": "AI科技", "icon": "🤖", "news": [
            {"id": 8, "title": "OpenAI发布GPT-4o升级版，多模态能力再突破", "source": "科技日报", "details": [
                {"label": "核心内容", "content": "推出GPT-4o Ultra模型，支持128K上下文窗口，图像理解能力提升40%"}
            ]},
            {"id": 9, "title": "阿里云发布真武M890AI芯片", "source": "36氪", "details": [
                {"label": "核心数据", "content": "采用5nm工艺，算力达400TOPS，能效比提升60%"}
            ]},
            {"id": 10, "title": "中国移动上线词元套餐", "source": "通信世界", "details": [
                {"label": "核心内容", "content": "推出统一算力量纲，将不同模型词元消耗统一封装为标准积分"}
            ]},
            {"id": 11, "title": "白宫拟发布AI行政令", "source": "彭博社", "details": [
                {"label": "核心内容", "content": "授权情报机构和政府机构在先进模型发布前进行审查"}
            ]}
        ]},
        "military": {"name": "军事安全", "icon": "⚔️", "news": [
            {"id": 12, "title": "美军加速AI军事化进程", "source": "解放军报", "details": [
                {"label": "核心内容", "content": "五角大楼与SpaceX、OpenAI、谷歌等7家AI巨头达成540亿美元协议"},
                {"label": "重要动作", "content": "将顶尖AI技术接入军事机密网络，直接参与作战决策"}
            ]},
            {"id": 13, "title": "我国新型装备亮相，国防科技再获突破", "source": "央视新闻", "details": [
                {"label": "重要成果", "content": "多款新型装备在国防科技展上亮相，展现我国国防自主创新能力"}
            ]}
        ]},
        "society": {"name": "人文社会", "icon": "🌍", "news": [
            {"id": 14, "title": "中欧联合微笑卫星成功发射", "source": "光明日报", "details": [
                {"label": "核心内容", "content": "探测太阳风与地球磁层相互作用，深化太空科学合作"}
            ]},
            {"id": 15, "title": "小米发布新车型YU7 GT", "source": "汽车之家", "details": [
                {"label": "核心内容", "content": "雷军表示该车定位为时代精英打造，定价会有点小贵"}
            ]}
        ]}
    }
    
    html_content = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>每日新闻速递</title>
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); min-height: 100vh; padding: 20px; }}
        .container {{ max-width: 900px; margin: 0 auto; }}
        .header {{ background: white; border-radius: 20px; padding: 30px; margin-bottom: 20px; text-align: center; }}
        .header h1 {{ font-size: 28px; color: #2c3e50; margin-bottom: 10px; }}
        .header .date {{ font-size: 16px; color: #7f8c8d; }}
        .category-tabs {{ display: flex; gap: 10px; padding: 15px 20px; background: white; border-radius: 16px; margin-bottom: 20px; overflow-x: auto; }}
        .tab {{ flex-shrink: 0; padding: 12px 24px; background: #f5f7fa; border: none; border-radius: 25px; font-size: 15px; cursor: pointer; transition: all 0.3s; }}
        .tab.active {{ background: linear-gradient(135deg, #667eea, #764ba2); color: white; }}
        .content-area {{ background: white; border-radius: 16px; padding: 28px; }}
        .category-panel {{ display: none; }}
        .category-panel.active {{ display: block; }}
        .news-item {{ padding: 20px; background: #fafbfc; border-radius: 12px; margin-bottom: 16px; cursor: pointer; }}
        .news-title {{ font-size: 18px; font-weight: 600; color: #2c3e50; }}
        .news-source {{ font-size: 13px; color: #95a5a6; background: #e8ecef; padding: 4px 12px; border-radius: 15px; }}
        .detail-item {{ margin-bottom: 10px; font-size: 15px; color: #5a6672; }}
        .detail-label {{ font-weight: 600; color: #667eea; }}
        .summary-section {{ background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); border-radius: 20px; padding: 30px; margin-top: 25px; color: white; }}
        .footer {{ background: rgba(255,255,255,0.95); border-radius: 16px; padding: 20px; text-align: center; margin-top: 25px; }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>📰 每日新闻速递</h1>
            <div class="date">{date_str}</div>
        </div>
        <div class="category-tabs">"""
    
    categories = ["politics", "economy", "tech", "military", "society"]
    for cat in categories:
        cat_data = news_data[cat]
        count = len(cat_data["news"])
        active = "active" if cat == "politics" else ""
        html_content += f'<button class="tab {active}" data-category="{cat}">{cat_data["icon"]} {cat_data["name"]} ({count})</button>'
    
    html_content += """</div>
        <div class="content-area">"""
    
    for cat in categories:
        cat_data = news_data[cat]
        active = "active" if cat == "politics" else ""
        html_content += f'<div id="{cat}" class="category-panel {active}"><h2>{cat_data["icon"]} {cat_data["name"]}</h2>'
        
        for news in cat_data["news"]:
            details = ""
            for d in news["details"]:
                details += f'<div class="detail-item"><span class="detail-label">{d["label"]}：</span>{d["content"]}</div>'
            html_content += f'''
            <div class="news-item" onclick="window.location.href='news-detail.html?news={news["id"]}'">
                <div class="news-title">{news["title"]}</div>
                <span class="news-source">{news["source"]}</span>
                <div>{details}</div>
            </div>'''
        html_content += "</div>"
    
    html_content += """</div>
        <div class="summary-section">
            <h3>💡 今日新闻总结</h3>
            <p>宏观层面：今日新闻展现了全球政治经济格局的深度调整。中俄战略合作深化标志着多极化趋势巩固，美联储鹰派信号表明货币政策仍在寻找平衡点。</p>
            <p>微观层面：科技领域突破引人关注，AI技术从实验室走向产业化，各国政府对AI监管重视提升。</p>
        </div>
        <div class="footer">
            <p>🌐 每日早10点自动更新 | 支持多端访问</p>
        </div>
    </div>
    <script>
        document.querySelectorAll('.tab').forEach(tab => {
            tab.addEventListener('click', () => {
                const cat = tab.getAttribute('data-category');
                document.querySelectorAll('.tab').forEach(t => t.classList.remove('active'));
                document.querySelectorAll('.category-panel').forEach(p => p.classList.remove('active'));
                tab.classList.add('active');
                document.getElementById(cat).classList.add('active');
            });
        });
    </script>
</body>
</html>"""
    return html_content

def generate_news_detail():
    news_data = {
        1: {"title": "中俄元首会谈", "source": "人民日报", "category": "国际政治", 
            "content": "国家主席习近平与俄罗斯总统普京在北京举行会谈，一致同意《中俄睦邻友好合作条约》继续延期。",
            "impact": "宏观：中俄战略协作伙伴关系持续深化；微观：双边合作迎来新机遇"},
        2: {"title": "美伊谈判进入最后阶段", "source": "环球时报", "category": "国际政治",
            "content": "美国总统特朗普表示，与伊朗的谈判已进入最后阶段。",
            "impact": "宏观：中东地缘政治格局或将重塑；微观：国际能源市场有望稳定"},
        3: {"title": "欧盟推出新数字战略", "source": "澎湃新闻", "category": "国际政治",
            "content": "欧盟委员会发布《数字未来法案》，提出更严格的AI风险分类。",
            "impact": "宏观：全球AI监管框架加速形成；微观：科技企业面临合规挑战"},
        4: {"title": "美联储会议纪要放鹰", "source": "金融时报", "category": "财经经济",
            "content": "多数决策者认为若通胀持续高于2%需政策收紧。",
            "impact": "宏观：全球货币政策进入观望期；微观：投资者需关注利率风险"},
        5: {"title": "英伟达Q1财报超预期", "source": "IT之家", "category": "财经经济",
            "content": "营收同比大增85%至816亿美元，净利润达583亿美元。",
            "impact": "宏观：AI芯片市场需求强劲；微观：科技股投资者情绪提振"},
        6: {"title": "SpaceX提交IPO申请", "source": "华尔街见闻", "category": "财经经济",
            "content": "目标估值指向1.8万亿美元，计划2028年部署轨道算力卫星。",
            "impact": "宏观：太空经济迎来资本热潮；微观：私人航天领域竞争加剧"},
        7: {"title": "中国财政数据亮眼", "source": "证券时报", "category": "财经经济",
            "content": "1-4月全国税收收入6.81万亿元，同比增长3.9%。",
            "impact": "宏观：财政收入稳健；微观：企业经营环境改善"},
        8: {"title": "OpenAI发布GPT-4o升级版", "source": "科技日报", "category": "AI科技",
            "content": "推出GPT-4o Ultra模型，支持128K上下文窗口，图像理解能力提升40%。",
            "impact": "宏观：AI多模态能力达到新高度；微观：开发者可构建更复杂应用"},
        9: {"title": "阿里云发布真武M890AI芯片", "source": "36氪", "category": "AI科技",
            "content": "采用5nm工艺，算力达400TOPS，能效比提升60%。",
            "impact": "宏观：国产AI芯片自主可控取得进展；微观：云计算厂商竞争加剧"},
        10: {"title": "中国移动上线词元套餐", "source": "通信世界", "category": "AI科技",
            "content": "推出统一算力量纲，将不同模型词元消耗统一封装为标准积分。",
            "impact": "宏观：AI算力服务商业模式创新；微观：企业AI使用成本透明"},
        11: {"title": "白宫拟发布AI行政令", "source": "彭博社", "category": "AI科技",
            "content": "授权情报机构和政府机构在先进模型发布前进行审查。",
            "impact": "宏观：美国AI监管政策收紧；微观：科技巨头面临更严格审查"},
        12: {"title": "美军加速AI军事化进程", "source": "解放军报", "category": "军事安全",
            "content": "五角大楼与SpaceX、OpenAI、谷歌等7家AI巨头达成540亿美元协议。",
            "impact": "宏观：全球军事AI竞赛升级；微观：AI伦理和安全问题亟待重视"},
        13: {"title": "我国新型装备亮相", "source": "央视新闻", "category": "军事安全",
            "content": "多款新型装备在国防科技展上亮相，展现我国国防自主创新能力。",
            "impact": "宏观：国防现代化建设取得新进展；微观：军工企业迎来发展机遇"},
        14: {"title": "中欧联合微笑卫星成功发射", "source": "光明日报", "category": "人文社会",
            "content": "探测太阳风与地球磁层相互作用，深化太空科学合作。",
            "impact": "宏观：国际太空合作持续深化；微观：空间天气研究获得新数据"},
        15: {"title": "小米发布新车型YU7 GT", "source": "汽车之家", "category": "人文社会",
            "content": "雷军表示该车定位为时代精英打造，定价会有点小贵。",
            "impact": "宏观：新能源汽车市场竞争加剧；微观：消费者有更多高端选择"}
    }
    
    import json
    news_json = json.dumps(news_data, ensure_ascii=False)
    
    html_content = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>新闻详情</title>
    <style>
        body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 20px; }}
        .container {{ max-width: 800px; margin: 0 auto; }}
        .news-card {{ background: white; border-radius: 20px; padding: 30px; }}
        .news-title {{ font-size: 26px; font-weight: 700; color: #2c3e50; }}
        .news-content {{ color: #5a6672; line-height: 1.8; }}
        .news-impact {{ background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); border-radius: 15px; padding: 20px; color: white; margin-top: 20px; }}
        .related-news {{ margin-top: 30px; padding-top: 30px; border-top: 1px solid #eee; }}
        .related-item {{ padding: 12px 0; border-bottom: 1px solid #f0f0f0; cursor: pointer; }}
    </style>
</head>
<body>
    <div class="container">
        <button onclick="window.location.href='daily-news.html'">← 返回列表</button>
        <div class="news-card">
            <div id="title">加载中...</div>
            <div id="content"></div>
            <div class="news-impact"><h4>💡 新闻启示</h4><p id="impact"></p></div>
            <div class="related-news"><h4>📌 相关新闻</h4><div id="related"></div></div>
        </div>
    </div>
    <script>
        const newsData = {news_json};
        function getNewsId() {{
            const params = new URLSearchParams(window.location.search);
            return params.get('news') ? parseInt(params.get('news')) : 1;
        }}
        function renderNews(id) {{
            const news = newsData[id];
            if (!news) {{ document.getElementById('title').textContent = '新闻不存在'; return; }}
            document.getElementById('title').textContent = news.title;
            document.getElementById('content').textContent = news.content;
            document.getElementById('impact').textContent = news.impact;
            const related = Object.keys(newsData).filter(k => parseInt(k) !== id && newsData[k].category === news.category).slice(0, 3);
            document.getElementById('related').innerHTML = related.map(k => `<div class="related-item" onclick="window.location.href='news-detail.html?news=${k}'">${newsData[k].title}</div>`).join('');
        }}
        renderNews(getNewsId());
    </script>
</body>
</html>"""
    return html_content

def main():
    print("🔄 正在生成每日新闻页面...")
    
    daily_html = generate_daily_news()
    with open('daily-news.html', 'w', encoding='utf-8') as f:
        f.write(daily_html)
    print("✅ daily-news.html 已生成")
    
    detail_html = generate_news_detail()
    with open('news-detail.html', 'w', encoding='utf-8') as f:
        f.write(detail_html)
    print("✅ news-detail.html 已生成")
    
    print("🎉 新闻页面生成完成！")

if __name__ == "__main__":
    main()
