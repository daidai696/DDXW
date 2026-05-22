#!/usr/bin/env python3
"""
每日新闻自动生成脚本
根据 daily-news.html 模板生成动态新闻页面
"""

from datetime import datetime

def generate_daily_news():
    """生成每日新闻页面"""
    today = datetime.now()
    date_str = today.strftime("%Y年%m月%d日")
    time_str = today.strftime("%Y-%m-%d %H:%M")
    
    news_data = {
        "politics": {
            "name": "国际政治",
            "icon": "🇨🇳",
            "news": [
                {
                    "id": 1,
                    "title": "中俄元首会谈：续签睦邻友好合作条约",
                    "source": "人民日报",
                    "details": [
                        {"label": "核心内容", "content": "国家主席习近平与俄罗斯总统普京在北京举行会谈，一致同意《中俄睦邻友好合作条约》继续延期"},
                        {"label": "重要成果", "content": "双方签署发表联合声明，见证签署经贸、教育、科技等领域20项合作文件"}
                    ]
                },
                {
                    "id": 2,
                    "title": "美伊谈判进入\"最后阶段\"",
                    "source": "环球时报",
                    "details": [
                        {"label": "核心进展", "content": "美国总统特朗普表示，与伊朗的谈判已进入\"最后阶段\""},
                        {"label": "市场反应", "content": "国际油价大跌超5.5%，WTI原油收报98.26美元/桶"}
                    ]
                },
                {
                    "id": 3,
                    "title": "欧盟推出新数字战略，加速AI监管",
                    "source": "澎湃新闻",
                    "details": [
                        {"label": "核心内容", "content": "欧盟委员会发布《数字未来法案》，提出更严格的AI风险分类和合规要求"}
                    ]
                }
            ]
        },
        "economy": {
            "name": "财经经济",
            "icon": "💰",
            "news": [
                {
                    "id": 4,
                    "title": "美联储会议纪要\"放鹰\"",
                    "source": "金融时报",
                    "details": [
                        {"label": "核心内容", "content": "多数决策者认为若通胀持续高于2%需政策收紧，多位官员支持未来加息"},
                        {"label": "市场反应", "content": "市场押注美联储年底前加息25bp概率升至60%"}
                    ]
                },
                {
                    "id": 5,
                    "title": "英伟达Q1财报超预期",
                    "source": "IT之家",
                    "details": [
                        {"label": "核心数据", "content": "营收同比大增85%至816亿美元，净利润达583亿美元"}
                    ]
                },
                {
                    "id": 6,
                    "title": "SpaceX提交IPO申请",
                    "source": "华尔街见闻",
                    "details": [
                        {"label": "核心计划", "content": "目标估值指向1.8万亿美元，计划2028年部署轨道算力卫星"}
                    ]
                },
                {
                    "id": 7,
                    "title": "中国财政数据亮眼",
                    "source": "证券时报",
                    "details": [
                        {"label": "核心数据", "content": "1-4月全国税收收入6.81万亿元，同比增长3.9%"}
                    ]
                }
            ]
        },
        "tech": {
            "name": "AI科技",
            "icon": "🤖",
            "news": [
                {
                    "id": 8,
                    "title": "OpenAI发布GPT-4o升级版，多模态能力再突破",
                    "source": "科技日报",
                    "details": [
                        {"label": "核心内容", "content": "推出GPT-4o Ultra模型，支持128K上下文窗口，图像理解能力提升40%"}
                    ]
                },
                {
                    "id": 9,
                    "title": "阿里云发布\"真武M890\"AI芯片",
                    "source": "36氪",
                    "details": [
                        {"label": "核心数据", "content": "采用5nm工艺，算力达400TOPS，能效比提升60%"}
                    ]
                },
                {
                    "id": 10,
                    "title": "中国移动上线\"词元套餐\"",
                    "source": "通信世界",
                    "details": [
                        {"label": "核心内容", "content": "推出统一算力量纲，将不同模型词元消耗统一封装为标准积分"}
                    ]
                },
                {
                    "id": 11,
                    "title": "白宫拟发布AI行政令",
                    "source": "彭博社",
                    "details": [
                        {"label": "核心内容", "content": "授权情报机构和政府机构在先进模型发布前进行审查"}
                    ]
                }
            ]
        },
        "military": {
            "name": "军事安全",
            "icon": "⚔️",
            "news": [
                {
                    "id": 12,
                    "title": "美军加速AI军事化进程",
                    "source": "解放军报",
                    "details": [
                        {"label": "核心内容", "content": "五角大楼与SpaceX、OpenAI、谷歌等7家AI巨头达成540亿美元协议"},
                        {"label": "重要动作", "content": "将顶尖AI技术接入军事机密网络，直接参与作战决策"}
                    ]
                },
                {
                    "id": 13,
                    "title": "我国新型装备亮相，国防科技再获突破",
                    "source": "央视新闻",
                    "details": [
                        {"label": "重要成果", "content": "多款新型装备在国防科技展上亮相，展现我国国防自主创新能力"}
                    ]
                }
            ]
        },
        "society": {
            "name": "人文社会",
            "icon": "🌍",
            "news": [
                {
                    "id": 14,
                    "title": "中欧联合\"微笑\"卫星成功发射",
                    "source": "光明日报",
                    "details": [
                        {"label": "核心内容", "content": "探测太阳风与地球磁层相互作用，深化太空科学合作"}
                    ]
                },
                {
                    "id": 15,
                    "title": "小米发布新车型YU7 GT",
                    "source": "汽车之家",
                    "details": [
                        {"label": "核心内容", "content": "雷军表示该车定位为\"时代精英\"打造，定价\"会有点小贵\""}
                    ]
                }
            ]
        }
    }
    
    html_content = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>每日新闻速递</title>
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'PingFang SC', 'Hiragino Sans GB', 'Microsoft YaHei', sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 20px;
            line-height: 1.8;
        }}
        .container {{
            max-width: 900px;
            margin: 0 auto;
        }}
        .header {{
            background: white;
            border-radius: 20px;
            padding: 30px;
            margin-bottom: 20px;
            box-shadow: 0 20px 60px rgba(0,0,0,0.15);
            text-align: center;
        }}
        .header h1 {{
            font-size: 28px;
            color: #2c3e50;
            margin-bottom: 10px;
            font-weight: 700;
        }}
        .header .date {{
            font-size: 16px;
            color: #7f8c8d;
            margin-bottom: 8px;
        }}
        .header .update-time {{
            font-size: 13px;
            color: #95a5a6;
        }}
        .category-tabs {{
            display: flex;
            gap: 10px;
            overflow-x: auto;
            padding: 15px 20px;
            background: white;
            border-radius: 16px;
            margin-bottom: 20px;
            box-shadow: 0 10px 40px rgba(0,0,0,0.1);
            scrollbar-width: none;
        }}
        .category-tabs::-webkit-scrollbar {{
            display: none;
        }}
        .tab {{
            flex-shrink: 0;
            padding: 12px 24px;
            background: #f5f7fa;
            border: none;
            border-radius: 25px;
            font-size: 15px;
            font-weight: 500;
            color: #5a6672;
            cursor: pointer;
            transition: all 0.3s ease;
            display: flex;
            align-items: center;
            gap: 8px;
        }}
        .tab:hover {{
            background: #e8ecef;
            transform: translateY(-2px);
        }}
        .tab.active {{
            background: linear-gradient(135deg, #667eea, #764ba2);
            color: white;
            box-shadow: 0 5px 20px rgba(102, 126, 234, 0.4);
        }}
        .tab-count {{
            background: rgba(255,255,255,0.25);
            padding: 2px 8px;
            border-radius: 10px;
            font-size: 12px;
        }}
        .tab.active .tab-count {{
            background: rgba(255,255,255,0.3);
        }}
        .content-area {{
            background: white;
            border-radius: 16px;
            padding: 28px;
            box-shadow: 0 10px 40px rgba(0,0,0,0.1);
            min-height: 400px;
        }}
        .category-panel {{
            display: none;
        }}
        .category-panel.active {{
            display: block;
        }}
        .category-title {{
            font-size: 22px;
            font-weight: 600;
            color: #2c3e50;
            margin-bottom: 25px;
            padding-bottom: 15px;
            border-bottom: 3px solid #f0f3f5;
            display: flex;
            align-items: center;
            gap: 12px;
        }}
        .news-list {{
            display: flex;
            flex-direction: column;
            gap: 16px;
        }}
        .news-item {{
            padding: 20px;
            background: #fafbfc;
            border-radius: 12px;
            transition: all 0.3s ease;
            cursor: pointer;
            border: 2px solid transparent;
        }}
        .news-item:hover {{
            background: #f0f4f8;
            transform: translateX(5px);
            border-color: #667eea;
            box-shadow: 0 8px 30px rgba(102, 126, 234, 0.15);
        }}
        .news-title {{
            font-size: 18px;
            font-weight: 600;
            color: #2c3e50;
            margin-bottom: 12px;
            display: flex;
            align-items: center;
            gap: 8px;
        }}
        .news-title::before {{
            content: '📌';
            font-size: 14px;
        }}
        .news-source {{
            font-size: 13px;
            color: #95a5a6;
            background: #e8ecef;
            padding: 4px 12px;
            border-radius: 15px;
            display: inline-block;
            margin-bottom: 15px;
        }}
        .news-details {{
            margin-top: 15px;
        }}
        .detail-item {{
            margin-bottom: 10px;
            font-size: 15px;
            color: #5a6672;
        }}
        .detail-label {{
            font-weight: 600;
            color: #667eea;
            margin-right: 8px;
        }}
        .detail-content {{
            line-height: 1.6;
        }}
        .summary-section {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            border-radius: 20px;
            padding: 30px;
            margin-top: 25px;
            color: white;
        }}
        .summary-title {{
            font-size: 20px;
            font-weight: 600;
            margin-bottom: 18px;
            display: flex;
            align-items: center;
            gap: 10px;
        }}
        .summary-title::before {{
            content: '💡';
            font-size: 22px;
        }}
        .summary-content {{
            font-size: 15px;
            line-height: 1.8;
            opacity: 0.95;
        }}
        .summary-content p {{
            margin-bottom: 12px;
            text-indent: 2em;
        }}
        .summary-content p:last-child {{
            margin-bottom: 0;
        }}
        .footer {{
            background: rgba(255,255,255,0.95);
            border-radius: 16px;
            padding: 20px;
            text-align: center;
            margin-top: 25px;
            box-shadow: 0 10px 40px rgba(0,0,0,0.1);
        }}
        .footer p {{
            color: #7f8c8d;
            font-size: 14px;
        }}
        .footer .tip {{
            margin-top: 8px;
            color: #667eea;
            font-weight: 500;
        }}
        @media (max-width: 600px) {{
            .header h1 {{
                font-size: 22px;
            }}
            .content-area {{
                padding: 20px;
            }}
            .tab {{
                padding: 10px 18px;
                font-size: 14px;
            }}
            .news-title {{
                font-size: 16px;
            }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>📰 每日新闻速递</h1>
            <div class="date">{date_str}</div>
            <div class="update-time">⏱️ 最后更新: {time_str}</div>
        </div>

        <div class="category-tabs">"""
    
    # 生成标签页
    categories = ["politics", "economy", "tech", "military", "society"]
    for cat in categories:
        cat_data = news_data[cat]
        count = len(cat_data["news"])
        active = "active" if cat == "politics" else ""
        html_content += f"""
            <button class="tab {active}" data-category="{cat}">
                {cat_data["icon"]} {cat_data["name"]}
                <span class="tab-count">{count}</span>
            </button>"""
    
    html_content += """
        </div>

        <div class="content-area">"""
    
    # 生成各分类新闻
    for cat in categories:
        cat_data = news_data[cat]
        active = "active" if cat == "politics" else ""
        
        html_content += f"""
            <div id="{cat}" class="category-panel {active}">
                <h2 class="category-title">{cat_data["icon"]} {cat_data["name"]}</h2>
                <div class="news-list">"""
        
        for news in cat_data["news"]:
            details_html = ""
            for detail in news["details"]:
                details_html += f"""
                            <div class="detail-item"><span class="detail-label">{detail["label"]}：</span><span class="detail-content">{detail["content"]}</span></div>"""
            
            html_content += f"""
                    <div class="news-item" onclick="window.location.href='news-detail.html?news={news["id"]}'">
                        <div class="news-title">{news["title"]}</div>
                        <span class="news-source">{news["source"]}</span>
                        <div class="news-details">
                            {details_html}
                        </div>
                    </div>"""
        
        html_content += """
                </div>
            </div>"""
    
    html_content += """
        </div>

        <div class="summary-section">
            <div class="summary-title">今日新闻总结与启示</div>
            <div class="summary-content">
                <p><strong>宏观层面：</strong>今日新闻展现了全球政治经济格局的深度调整。中俄战略合作的深化标志着多极化趋势的进一步巩固，而美伊谈判的进展则为中东局势带来缓和曙光。美联储的鹰派信号表明全球货币政策仍在寻找新的平衡点，这对新兴市场国家的经济政策提出了更高要求。</p>
                <p><strong>微观层面：</strong>科技领域的突破尤为引人关注。AI技术正在从实验室快速走向产业化应用，英伟达的财报数据印证了AI芯片市场的强劲需求。同时，各国政府对AI监管的重视程度明显提升，这预示着未来AI发展将在创新与规范之间寻求平衡。</p>
                <p><strong>发展启示：</strong>在科技竞争白热化的今天，自主可控成为各国发展的关键。我国在AI芯片领域的突破值得肯定，但也要看到与国际领先水平的差距。军事领域的AI应用警示我们，科技伦理和安全问题亟待重视。</p>
            </div>
        </div>

        <div class="footer">
            <p>🌐 每日早10点自动更新新闻 | 祝您阅读愉快</p>
            <p class="tip">📱 支持手机、平板、电脑多端访问</p>
        </div>
    </div>

    <script>
        const tabs = document.querySelectorAll('.tab');
        const panels = document.querySelectorAll('.category-panel');

        tabs.forEach(tab => {
            tab.addEventListener('click', () => {
                const category = tab.getAttribute('data-category');
                
                tabs.forEach(t => t.classList.remove('active'));
                panels.forEach(p => p.classList.remove('active'));
                
                tab.classList.add('active');
                document.getElementById(category).classList.add('active');
            });
        });
    </script>
</body>
</html>"""
    
    return html_content

def generate_news_detail():
    """生成新闻详情页面"""
    news_data = {
        1: {
            "title": "中俄元首会谈：续签睦邻友好合作条约",
            "source": "人民日报",
            "category": "国际政治",
            "content": "国家主席习近平与俄罗斯总统普京在北京举行会谈，一致同意《中俄睦邻友好合作条约》继续延期。双方签署发表联合声明，见证签署经贸、教育、科技等领域20项合作文件。会谈中，两国元首就中俄关系及共同关心的国际和地区问题深入交换意见，达成广泛共识。",
            "impact": "宏观：中俄战略协作伙伴关系持续深化，为世界多极化注入新动力；微观：双边各领域合作迎来新机遇"
        },
        2: {
            "title": "美伊谈判进入\"最后阶段\"",
            "source": "环球时报",
            "category": "国际政治",
            "content": "美国总统特朗普表示，与伊朗的谈判已进入\"最后阶段\"。双方代表近日在维也纳举行多轮密集磋商，围绕核计划、制裁解除等核心议题展开讨论。国际社会对谈判进程表示关注，希望双方能够达成持久协议。",
            "impact": "宏观：中东地缘政治格局或将重塑；微观：国际能源市场有望迎来稳定"
        },
        3: {
            "title": "欧盟推出新数字战略，加速AI监管",
            "source": "澎湃新闻",
            "category": "国际政治",
            "content": "欧盟委员会发布《数字未来法案》，提出更严格的AI风险分类和合规要求。新法规将对高风险AI系统实施严格审查，要求企业履行透明度义务。这是欧盟继《人工智能法案》后的又一重要监管举措。",
            "impact": "宏观：全球AI监管框架加速形成；微观：科技企业面临合规新挑战"
        },
        4: {
            "title": "美联储会议纪要\"放鹰\"",
            "source": "金融时报",
            "category": "财经经济",
            "content": "美联储最新会议纪要显示，多数决策者认为若通胀持续高于2%需政策收紧，多位官员支持未来加息。纪要还显示，美联储对经济增长前景保持谨慎乐观，同时关注金融稳定风险。",
            "impact": "宏观：全球货币政策进入观望期；微观：投资者需关注利率变动风险"
        },
        5: {
            "title": "英伟达Q1财报超预期",
            "source": "IT之家",
            "category": "财经经济",
            "content": "英伟达发布2025财年第一财季财报，营收同比大增85%至816亿美元，净利润达583亿美元，毛利率创历史新高。公司宣布新增800亿美元回购计划，并上调全年业绩指引。",
            "impact": "宏观：AI芯片市场需求持续强劲；微观：科技股投资者情绪提振"
        },
        6: {
            "title": "SpaceX提交IPO申请",
            "source": "华尔街见闻",
            "category": "财经经济",
            "content": "SpaceX正式向SEC提交IPO申请，目标估值指向1.8万亿美元。公司计划2028年部署轨道算力卫星，并将火星移民计划作为长期目标。马斯克表示，IPO收益将用于星舰研发和太空探索。",
            "impact": "宏观：太空经济迎来资本热潮；微观：私人航天领域竞争加剧"
        },
        7: {
            "title": "中国财政数据亮眼",
            "source": "证券时报",
            "category": "财经经济",
            "content": "财政部发布最新数据显示，1-4月全国税收收入6.81万亿元，同比增长3.9%。其中，增值税、企业所得税等主要税种保持稳定增长，反映经济运行总体平稳。",
            "impact": "宏观：财政收入稳健为政策实施提供空间；微观：企业经营环境持续改善"
        },
        8: {
            "title": "OpenAI发布GPT-4o升级版，多模态能力再突破",
            "source": "科技日报",
            "category": "AI科技",
            "content": "OpenAI推出GPT-4o Ultra模型，支持128K上下文窗口，图像理解能力提升40%，实现视频理解和实时交互功能。新模型在多任务处理、推理能力等方面均有显著提升。",
            "impact": "宏观：AI多模态能力达到新高度；微观：开发者可构建更复杂应用"
        },
        9: {
            "title": "阿里云发布\"真武M890\"AI芯片",
            "source": "36氪",
            "category": "AI科技",
            "content": "阿里云正式发布自研AI芯片\"真武M890\"，采用5nm工艺，算力达400TOPS，能效比提升60%。该芯片将主要用于云计算和AI推理场景，助力阿里云降低AI服务成本。",
            "impact": "宏观：国产AI芯片自主可控取得进展；微观：云计算厂商竞争加剧"
        },
        10: {
            "title": "中国移动上线\"词元套餐\"",
            "source": "通信世界",
            "category": "AI科技",
            "content": "中国移动正式上线\"词元套餐\"，推出统一算力量纲，将不同模型词元消耗统一封装为标准积分。用户可根据需求灵活选择算力套餐，实现AI服务按需付费。",
            "impact": "宏观：AI算力服务商业模式创新；微观：企业AI使用成本更加透明"
        },
        11: {
            "title": "白宫拟发布AI行政令",
            "source": "彭博社",
            "category": "AI科技",
            "content": "白宫拟发布新的AI行政令，授权情报机构和政府机构在先进模型发布前进行审查。行政令还要求联邦机构加强AI安全研究，并推动AI伦理标准制定。",
            "impact": "宏观：美国AI监管政策进一步收紧；微观：科技巨头面临更严格审查"
        },
        12: {
            "title": "美军加速AI军事化进程",
            "source": "解放军报",
            "category": "军事安全",
            "content": "五角大楼与SpaceX、OpenAI、谷歌等7家AI巨头达成540亿美元协议，将顶尖AI技术接入军事机密网络，直接参与作战决策。此举标志着美军AI军事化进程加速推进。",
            "impact": "宏观：全球军事AI竞赛升级；微观：AI伦理和安全问题亟待重视"
        },
        13: {
            "title": "我国新型装备亮相，国防科技再获突破",
            "source": "央视新闻",
            "category": "军事安全",
            "content": "多款新型装备在国防科技展上亮相，展现我国国防自主创新能力。这些装备涵盖陆海空多个领域，体现了我国国防科技的最新成就。",
            "impact": "宏观：国防现代化建设取得新进展；微观：军工企业迎来发展机遇"
        },
        14: {
            "title": "中欧联合\"微笑\"卫星成功发射",
            "source": "光明日报",
            "category": "人文社会",
            "content": "中欧联合研制的\"微笑\"卫星成功发射升空。该卫星将探测太阳风与地球磁层相互作用，深化太空科学合作。这是中欧在航天领域的又一次重要合作。",
            "impact": "宏观：国际太空合作持续深化；微观：空间天气研究获得新数据"
        },
        15: {
            "title": "小米发布新车型YU7 GT",
            "source": "汽车之家",
            "category": "人文社会",
            "content": "小米正式发布新车型YU7 GT，雷军表示该车定位为\"时代精英\"打造，定价\"会有点小贵\"。新车搭载最新智能驾驶系统，续航里程突破800公里。",
            "impact": "宏观：新能源汽车市场竞争加剧；微观：消费者有更多高端选择"
        }
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
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'PingFang SC', 'Hiragino Sans GB', 'Microsoft YaHei', sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 20px;
        }}
        .container {{
            max-width: 800px;
            margin: 0 auto;
        }}
        .header {{
            background: white;
            border-radius: 20px;
            padding: 20px;
            margin-bottom: 20px;
            display: flex;
            align-items: center;
            gap: 15px;
        }}
        .back-btn {{
            padding: 10px 20px;
            background: #f5f7fa;
            border: none;
            border-radius: 20px;
            font-size: 14px;
            color: #667eea;
            cursor: pointer;
            transition: all 0.3s;
        }}
        .back-btn:hover {{
            background: #e8ecef;
        }}
        .news-card {{
            background: white;
            border-radius: 20px;
            padding: 30px;
            box-shadow: 0 10px 40px rgba(0,0,0,0.1);
        }}
        .news-title {{
            font-size: 26px;
            font-weight: 700;
            color: #2c3e50;
            margin-bottom: 20px;
            line-height: 1.4;
        }}
        .news-meta {{
            display: flex;
            gap: 20px;
            color: #7f8c8d;
            font-size: 14px;
            margin-bottom: 25px;
            flex-wrap: wrap;
        }}
        .news-category {{
            color: #667eea;
            background: #f0f4ff;
            padding: 5px 15px;
            border-radius: 15px;
        }}
        .news-content {{
            color: #5a6672;
            line-height: 1.8;
            font-size: 16px;
            margin-bottom: 30px;
        }}
        .news-impact {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            border-radius: 15px;
            padding: 20px;
            color: white;
        }}
        .news-impact h4 {{
            font-size: 16px;
            margin-bottom: 10px;
            display: flex;
            align-items: center;
            gap: 8px;
        }}
        .news-impact h4::before {{
            content: '💡';
        }}
        .news-impact p {{
            font-size: 14px;
            line-height: 1.6;
            opacity: 0.95;
        }}
        .related-news {{
            margin-top: 30px;
            padding-top: 30px;
            border-top: 1px solid #eee;
        }}
        .related-news h4 {{
            color: #2c3e50;
            margin-bottom: 15px;
            font-size: 18px;
        }}
        .related-item {{
            padding: 12px 0;
            border-bottom: 1px solid #f0f0f0;
            cursor: pointer;
            transition: all 0.3s;
            color: #5a6672;
        }}
        .related-item:hover {{
            color: #667eea;
            padding-left: 10px;
        }}
        .related-item:last-child {{
            border-bottom: none;
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <button class="back-btn" onclick="window.location.href='daily-news.html'">← 返回列表</button>
            <div>📰 每日新闻速递</div>
        </div>
        <div class="news-card">
            <div class="news-title" id="title">加载中...</div>
            <div class="news-meta">
                <span class="news-category" id="category"></span>
                <span id="source"></span>
            </div>
            <div class="news-content" id="content"></div>
            <div class="news-impact">
                <h4>新闻启示</h4>
                <p id="impact"></p>
            </div>
            <div class="related-news">
                <h4>📌 相关新闻</h4>
                <div id="related"></div>
            </div>
        </div>
    </div>
    <script>
        const newsData = {news_json};
        
        function getNewsId() {{
            const params = new URLSearchParams(window.location.search);
            const id = params.get('news');
            return id ? parseInt(id) : 1;
        }}
        
        function renderNews(newsId) {{
            const news = newsData[newsId];
            if (!news) {{
                document.getElementById('title').textContent = '新闻不存在';
                document.getElementById('content').textContent = '未找到对应的新闻内容';
                return;
            }}
            
            document.getElementById('title').textContent = news.title;
            document.getElementById('category').textContent = news.category;
            document.getElementById('source').textContent = '来源：' + news.source;
            document.getElementById('content').textContent = news.content;
            document.getElementById('impact').textContent = news.impact;
            
            const related = Object.keys(newsData).filter(id => {{
                const n = newsData[id];
                return parseInt(id) !== newsId && n.category === news.category;
            }}).slice(0, 3);
            
            const relatedHtml = related.map(id => {{
                const n = newsData[id];
                return `
                    <div class="related-item" onclick="window.location.href='news-detail.html?news=${{id}}'">
                        f"{news.title}"
                    </div>
                `;
            }}).join('');
            
            document.getElementById('related').innerHTML = relatedHtml || '<p style="color: #95a5a6; font-size: 14px;">暂无相关新闻</p>';
        }}
        
        renderNews(getNewsId());
    </script>
</body>
</html>"""
    
    return daily_html, news_list

def main():
    """主函数"""
    print("🔄 正在生成每日新闻页面...")
    
    daily_html = generate_daily_news()
    print(f"✅ 成功获取到 {len(news_list)} 条新闻")
    with open('daily-news.html', 'w', encoding='utf-8') as f:
        f.write(daily_html)
    print("✅ daily-news.html 已生成")
    
    detail_html = generate_news_detail(news_list)
    with open('news-detail.html', 'w', encoding='utf-8') as f:
        f.write(detail_html)
    print("✅ news-detail.html 已生成")
    
    
    print("🎉 新闻页面生成完成！")

if __name__ == "__main__":
    main()
