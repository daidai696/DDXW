name: Daily News Update

on:
  schedule:
    - cron: '0 2 * * *'  # 北京时间上午10点（UTC时间凌晨2点）
  push:
    branches:
      - main

jobs:
  update-news:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout repository
        uses: actions/checkout@v4
        with:
          fetch-depth: 0
          persist-credentials: false

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.10'

      - name: Install dependencies and run news generator
        run: |
          pip install requests beautifulsoup4
          python daily_news.py

      - name: Configure git
        run: |
          git config --global user.email "github-actions[bot]@users.noreply.github.com"
          git config --global user.name "github-actions[bot]"

      - name: Commit changes
        run: |
          git add daily-news.html news-detail.html
          git diff --cached --quiet || git commit -m "Auto update news - $(date +'%Y-%m-%d %H:%M:%S')"

      - name: Push changes
        uses: ad-m/github-push-action@master
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          branch: main

  deploy:
    runs-on: ubuntu-latest
    needs: update-news
    steps:
      - name: Checkout repository
        uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - name: Deploy to Netlify
        uses: netlify/actions/cli@master
        with:
          args: deploy --prod --dir=.
        env:
          NETLIFY_AUTH_TOKEN: ${{ secrets.NETLIFY_AUTH_TOKEN }}
          NETLIFY_SITE_ID: ${{ secrets.NETLIFY_SITE_ID }}
