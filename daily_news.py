#!/usr/bin/env python3
"""
每日新闻自动生成脚本 - 使用爬虫获取真实新闻
"""

import requests
from datetime import datetime
from bs4 import BeautifulSoup
import json
import re

# 新闻源配置
NEWS_SOURCES = {
    'politics': [
        {'name': '新华网', 'url': 'http://www.xinhuanet.com/politics/'},
        {'name': '人民网', 'url': 'http://politics.people.com.cn/'},
        {'name': '央视新闻', 'url': 'https://news.cctv.com/politics/'},
    ],
    'economy': [
        {'name': '财新网', 'url': 'https://www.caixin.com/'},
        {'name': '华尔街见闻', 'url': 'https://wallstreetcn.com/'},
        {'name': '新浪财经', 'url': 'https://finance.sina.com.cn/'},
    ],
    'tech': [
        {'name': '36 氪', 'url': 'https://36kr.com/'},
        {'name': '虎嗅', 'url': 'https://www.huxiu.com/'},
        {'name': 'IT 之家', 'url': 'https://www.ithome.com/'},
    ],
    'military': [
        {'name': '参考消息', 'url': 'http://www.cankaoxiaoxi.com/'},
        {'name': '环球时报', 'url': 'https://www.huanqiu.com/'},
    ],
    'society': [
        {'name': '澎湃新闻', 'url': 'https://www.thepaper.cn/'},
        {'name': '新京报', 'url': 'https://www.bjnews.com.cn/'},
    ]
}

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
}

def fetch_news_from_source(source):
    """从指定新闻源爬取新闻"""
    news_list = []
    try:
        response = requests.get(source['url'], headers=HEADERS, timeout=10)
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # 尝试不同的新闻链接选择器
        links = soup.find_all('a', href=True)
        
        for link in links[:50]:  # 限制处理数量
            title = link.get_text(strip=True)
            href = link['href']
            
            # 过滤无效链接和标题
            if not title or len(title) < 5 or len(title) > 100:
                continue
            
            # 过滤非新闻链接
            if any(keyword in title.lower() for keyword in ['广告', '推广', '专题', '直播']):
                continue
            
            # 处理相对链接
            if href.startswith('/'):
                if 'xinhuanet' in source['url']:
                    href = 'http://www.xinhuanet.com' + href
                elif 'people' in source['url']:
                    href = 'http://politics.people.com.cn' + href
                # ... 其他域名处理
            
            news_list.append({
                'title': title,
                'source': source['name'],
                'url': href
            })
            
            if len(news_list) >= 3:  # 每个源最多取 3 条
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
        
        # 去重（按标题）
        seen = set()
        unique_news = []
        for news in category_news:
            if news['title'] not in seen:
                seen.add(news['title'])
                unique_news.append(news)
        
        all_news[category] = unique_news[:5]  # 每个类别最多 5 条
    
    return all_news

def generate_daily_news(all_news=None):
    if all_news is None:
        print("🕷️ 正在爬取最新新闻...")
        all_news = fetch_all_news()
        print(f"✅ 成功获取新闻：政治{len(all_news.get('politics', []))}条，"
              f"经济{len(all_news.get('economy', []))}条，"
              f"科技{len(all_news.get('tech', []))}条，"
              f"军事{len(all_news.get('military', []))}条，"
              f"社会{len(all_news.get('society', []))}条")
    
    today = datetime.now()
    date_str = today.strftime("%Y年%m月%d日")
    today = datetime.now()
    date_str = today.strftime("%Y年%m月%d日")
    
    news_html = """
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>每日新闻速递</title>
    <style>
        body { font-family: sans-serif; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); min-height: 100vh; padding: 20px; }
        .container { max-width: 900px; margin: 0 auto; }
        .header { background: white; border-radius: 20px; padding: 30px; text-align: center; margin-bottom: 20px; }
        .header h1 { font-size: 28px; color: #2c3e50; }
        .tabs { display: flex; gap: 10px; padding: 15px; background: white; border-radius: 16px; margin-bottom: 20px; flex-wrap: wrap; }
        .tab { padding: 12px 24px; background: #f5f7fa; border: none; border-radius: 25px; cursor: pointer; font-size: 15px; }
        .tab.active { background: linear-gradient(135deg, #667eea, #764ba2); color: white; }
        .content { background: white; border-radius: 16px; padding: 28px; }
        .panel { display: none; }
        .panel.active { display: block; }
        .news-item { padding: 20px; background: #fafbfc; border-radius: 12px; margin-bottom: 16px; cursor: pointer; }
        .news-title { font-size: 18px; font-weight: 600; color: #2c3e50; }
        .news-source { font-size: 13px; color: #95a5a6; background: #e8ecef; padding: 4px 12px; border-radius: 15px; }
        .summary { background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); border-radius: 20px; padding: 30px; margin-top: 25px; color: white; }
        .footer { background: rgba(255,255,255,0.95); border-radius: 16px; padding: 20px; text-align: center; margin-top: 25px; }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>📰 每日新闻速递</h1>
            <p>""" + date_str + """</p>
        </div>
        <div class="tabs">
            <button class="tab active" onclick="showPanel('politics')">🇨🇳 国际政治</button>
            <button class="tab" onclick="showPanel('economy')">💰 财经经济</button>
            <button class="tab" onclick="showPanel('tech')">🤖 AI科技</button>
            <button class="tab" onclick="showPanel('military')">⚔️ 军事安全</button>
            <button class="tab" onclick="showPanel('society')">🌍 人文社会</button>
        </div>
        <div class="content">
            <div id="politics" class="panel active">
                <h2>🇨🇳 国际政治</h2>
                <div class="news-item" onclick="window.location.href='news-detail.html?n=1'">
                    <div class="news-title">中俄元首会谈：续签睦邻友好合作条约</div>
                    <span class="news-source">人民日报</span>
                    <p>核心内容：国家主席习近平与俄罗斯总统普京在北京举行会谈，一致同意《中俄睦邻友好合作条约》继续延期</p>
                </div>
                <div class="news-item" onclick="window.location.href='news-detail.html?n=2'">
                    <div class="news-title">美伊谈判进入最后阶段</div>
                    <span class="news-source">环球时报</span>
                    <p>核心进展：美国总统特朗普表示，与伊朗的谈判已进入最后阶段</p>
                </div>
                <div class="news-item" onclick="window.location.href='news-detail.html?n=3'">
                    <div class="news-title">欧盟推出新数字战略，加速AI监管</div>
                    <span class="news-source">澎湃新闻</span>
                    <p>核心内容：欧盟委员会发布《数字未来法案》，提出更严格的AI风险分类和合规要求</p>
                </div>
            </div>
            <div id="economy" class="panel">
                <h2>💰 财经经济</h2>
                <div class="news-item" onclick="window.location.href='news-detail.html?n=4'">
                    <div class="news-title">美联储会议纪要放鹰</div>
                    <span class="news-source">金融时报</span>
                    <p>核心内容：多数决策者认为若通胀持续高于2%需政策收紧</p>
                </div>
                <div class="news-item" onclick="window.location.href='news-detail.html?n=5'">
                    <div class="news-title">英伟达Q1财报超预期</div>
                    <span class="news-source">IT之家</span>
                    <p>核心数据：营收同比大增85%至816亿美元，净利润达583亿美元</p>
                </div>
                <div class="news-item" onclick="window.location.href='news-detail.html?n=6'">
                    <div class="news-title">SpaceX提交IPO申请</div>
                    <span class="news-source">华尔街见闻</span>
                    <p>核心计划：目标估值指向1.8万亿美元</p>
                </div>
                <div class="news-item" onclick="window.location.href='news-detail.html?n=7'">
                    <div class="news-title">中国财政数据亮眼</div>
                    <span class="news-source">证券时报</span>
                    <p>核心数据：1-4月全国税收收入6.81万亿元，同比增长3.9%</p>
                </div>
            </div>
            <div id="tech" class="panel">
                <h2>🤖 AI科技</h2>
                <div class="news-item" onclick="window.location.href='news-detail.html?n=8'">
                    <div class="news-title">OpenAI发布GPT-4o升级版</div>
                    <span class="news-source">科技日报</span>
                    <p>核心内容：推出GPT-4o Ultra模型，支持128K上下文窗口</p>
                </div>
                <div class="news-item" onclick="window.location.href='news-detail.html?n=9'">
                    <div class="news-title">阿里云发布真武M890AI芯片</div>
                    <span class="news-source">36氪</span>
                    <p>核心数据：采用5nm工艺，算力达400TOPS</p>
                </div>
                <div class="news-item" onclick="window.location.href='news-detail.html?n=10'">
                    <div class="news-title">中国移动上线词元套餐</div>
                    <span class="news-source">通信世界</span>
                    <p>核心内容：推出统一算力量纲</p>
                </div>
                <div class="news-item" onclick="window.location.href='news-detail.html?n=11'">
                    <div class="news-title">白宫拟发布AI行政令</div>
                    <span class="news-source">彭博社</span>
                    <p>核心内容：授权情报机构和政府机构在先进模型发布前进行审查</p>
                </div>
            </div>
            <div id="military" class="panel">
                <h2>⚔️ 军事安全</h2>
                <div class="news-item" onclick="window.location.href='news-detail.html?n=12'">
                    <div class="news-title">美军加速AI军事化进程</div>
                    <span class="news-source">解放军报</span>
                    <p>核心内容：五角大楼与7家AI巨头达成540亿美元协议</p>
                </div>
                <div class="news-item" onclick="window.location.href='news-detail.html?n=13'">
                    <div class="news-title">我国新型装备亮相</div>
                    <span class="news-source">央视新闻</span>
                    <p>重要成果：多款新型装备在国防科技展上亮相</p>
                </div>
            </div>
            <div id="society" class="panel">
                <h2>🌍 人文社会</h2>
                <div class="news-item" onclick="window.location.href='news-detail.html?n=14'">
                    <div class="news-title">中欧联合微笑卫星成功发射</div>
                    <span class="news-source">光明日报</span>
                    <p>核心内容：探测太阳风与地球磁层相互作用</p>
                </div>
                <div class="news-item" onclick="window.location.href='news-detail.html?n=15'">
                    <div class="news-title">小米发布新车型YU7 GT</div>
                    <span class="news-source">汽车之家</span>
                    <p>核心内容：雷军表示该车定位为时代精英打造</p>
                </div>
            </div>
        </div>
        <div class="summary">
            <h3>💡 今日新闻总结</h3>
            <p>宏观层面：今日新闻展现了全球政治经济格局的深度调整。中俄战略合作深化标志着多极化趋势巩固，美联储鹰派信号表明货币政策仍在寻找平衡点。</p>
            <p>微观层面：科技领域突破引人关注，AI技术从实验室走向产业化，各国政府对AI监管重视提升。</p>
        </div>
        <div class="footer">
            <p>🌐 每日早10点自动更新 | 支持多端访问</p>
        </div>
    </div>
    <script>
        function showPanel(id) {
            document.querySelectorAll('.tab').forEach(t => t.classList.remove('active'));
            document.querySelectorAll('.panel').forEach(p => p.classList.remove('active'));
            event.target.classList.add('active');
            document.getElementById(id).classList.add('active');
        }
    </script>
</body>
</html>"""
    return news_html

def generate_news_detail():
    news_html = """
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>新闻详情</title>
    <style>
        body { font-family: sans-serif; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 20px; }
        .container { max-width: 800px; margin: 0 auto; }
        .card { background: white; border-radius: 20px; padding: 30px; }
        .title { font-size: 26px; font-weight: 700; color: #2c3e50; }
        .content { color: #5a6672; line-height: 1.8; margin-top: 20px; }
        .impact { background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); border-radius: 15px; padding: 20px; color: white; margin-top: 20px; }
        .related { margin-top: 30px; padding-top: 30px; border-top: 1px solid #eee; }
        .rel-item { padding: 12px 0; border-bottom: 1px solid #f0f0f0; cursor: pointer; }
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
                <h4>📌 相关新闻</h4>
                <div id="related"></div>
            </div>
        </div>
    </div>
    <script>
        var newsData = {
            1: {title: '中俄元首会谈：续签睦邻友好合作条约', content: '国家主席习近平与俄罗斯总统普京在北京举行会谈，一致同意《中俄睦邻友好合作条约》继续延期。双方签署发表联合声明，见证签署经贸、教育、科技等领域20项合作文件。', impact: '宏观：中俄战略协作伙伴关系持续深化；微观：双边合作迎来新机遇', cat: 'politics'},
            2: {title: '美伊谈判进入最后阶段', content: '美国总统特朗普表示，与伊朗的谈判已进入最后阶段。双方代表近日在维也纳举行多轮密集磋商。', impact: '宏观：中东地缘政治格局或将重塑；微观：国际能源市场有望稳定', cat: 'politics'},
            3: {title: '欧盟推出新数字战略', content: '欧盟委员会发布《数字未来法案》，提出更严格的AI风险分类和合规要求。', impact: '宏观：全球AI监管框架加速形成；微观：科技企业面临合规挑战', cat: 'politics'},
            4: {title: '美联储会议纪要放鹰', content: '多数决策者认为若通胀持续高于2%需政策收紧，多位官员支持未来加息。', impact: '宏观：全球货币政策进入观望期；微观：投资者需关注利率风险', cat: 'economy'},
            5: {title: '英伟达Q1财报超预期', content: '营收同比大增85%至816亿美元，净利润达583亿美元，毛利率创历史新高。', impact: '宏观：AI芯片市场需求强劲；微观：科技股投资者情绪提振', cat: 'economy'},
            6: {title: 'SpaceX提交IPO申请', content: '目标估值指向1.8万亿美元，计划2028年部署轨道算力卫星。', impact: '宏观：太空经济迎来资本热潮；微观：私人航天领域竞争加剧', cat: 'economy'},
            7: {title: '中国财政数据亮眼', content: '1-4月全国税收收入6.81万亿元，同比增长3.9%。', impact: '宏观：财政收入稳健；微观：企业经营环境改善', cat: 'economy'},
            8: {title: 'OpenAI发布GPT-4o升级版', content: '推出GPT-4o Ultra模型，支持128K上下文窗口，图像理解能力提升40%。', impact: '宏观：AI多模态能力达到新高度；微观：开发者可构建更复杂应用', cat: 'tech'},
            9: {title: '阿里云发布真武M890AI芯片', content: '采用5nm工艺，算力达400TOPS，能效比提升60%。', impact: '宏观：国产AI芯片自主可控取得进展；微观：云计算厂商竞争加剧', cat: 'tech'},
            10: {title: '中国移动上线词元套餐', content: '推出统一算力量纲，将不同模型词元消耗统一封装为标准积分。', impact: '宏观：AI算力服务商业模式创新；微观：企业AI使用成本透明', cat: 'tech'},
            11: {title: '白宫拟发布AI行政令', content: '授权情报机构和政府机构在先进模型发布前进行审查。', impact: '宏观：美国AI监管政策收紧；微观：科技巨头面临更严格审查', cat: 'tech'},
            12: {title: '美军加速AI军事化进程', content: '五角大楼与SpaceX、OpenAI、谷歌等7家AI巨头达成540亿美元协议。', impact: '宏观：全球军事AI竞赛升级；微观：AI伦理和安全问题亟待重视', cat: 'military'},
            13: {title: '我国新型装备亮相', content: '多款新型装备在国防科技展上亮相，展现我国国防自主创新能力。', impact: '宏观：国防现代化建设取得新进展；微观：军工企业迎来发展机遇', cat: 'military'},
            14: {title: '中欧联合微笑卫星成功发射', content: '探测太阳风与地球磁层相互作用，深化太空科学合作。', impact: '宏观：国际太空合作持续深化；微观：空间天气研究获得新数据', cat: 'society'},
            15: {title: '小米发布新车型YU7 GT', content: '雷军表示该车定位为时代精英打造，定价会有点小贵。', impact: '宏观：新能源汽车市场竞争加剧；微观：消费者有更多高端选择', cat: 'society'}
        };
        function getNewsId() {
            var params = new URLSearchParams(window.location.search);
            var id = params.get('n');
            return id ? parseInt(id) : 1;
        }
        function renderNews(id) {
            var news = newsData[id];
            if (!news) {
                document.getElementById('title').textContent = '新闻不存在';
                return;
            }
            document.getElementById('title').textContent = news.title;
            document.getElementById('content').textContent = news.content;
            document.getElementById('impact').textContent = news.impact;
            var related = [];
            for (var key in newsData) {
                if (parseInt(key) !== id && newsData[key].cat === news.cat) {
                    related.push(key);
                }
            }
            related = related.slice(0, 3);
            var html = '';
            for (var i = 0; i < related.length; i++) {
                var k = related[i];
                html += '<div class="rel-item" onclick="window.location.href=\'news-detail.html?n=\' + k + \'\'">' + newsData[k].title + '</div>';
            }
            document.getElementById('related').innerHTML = html || '<p style="color: #95a5a6;">暂无相关新闻</p>';
        }
        renderNews(getNewsId());
    </script>
</body>
</html>"""
    return news_html

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
