import playwright
import mysql.connector

# MySQL 데이터베이스 연결 설정
db = mysql.connector.connect(
    host="localhost",
    user="your_username",
    password="your_password",
    database="your_database"
)
cursor = db.cursor()

# Playwright 초기화
with playwright.sync_playwright() as p:
    browser = p.chromium.launch()
    context = browser.new_context()

    # 크롤링할 YouTube 동영상 링크
    video_link = "https://www.youtube.com/watch?v=your_video_id"

    # YouTube 동영상 페이지 열기
    page = context.new_page()
    page.goto(video_link)

    # 댓글 크롤링
    comments = page.query_selector_all('#comments #content-text')
    for comment in comments:
        comment_text = comment.inner_text()
        # 댓글 데이터를 데이터베이스에 저장
        sql = "INSERT INTO comments (comment_text) VALUES (%s)"
        val = (comment_text,)
        cursor.execute(sql, val)
        db.commit()

    # 조회수 크롤링
    views_element = page.query_selector('#count > yt-view-count-renderer > span.view-count')
    views = views_element.inner_text()
    # 조회수 데이터를 데이터베이스에 저장
    sql = "INSERT INTO video_stats (views) VALUES (%s)"
    val = (views,)
    cursor.execute(sql, val)
    db.commit()

    # 좋아요 수 크롤링
    like_button = page.query_selector('#top-level-buttons > ytd-toggle-button-renderer:nth-child(1)')
    likes = like_button.attribute('aria-label')
    # 좋아요 데이터를 데이터베이스에 저장
    sql = "INSERT INTO video_stats (likes) VALUES (%s)"
    val = (likes,)
    cursor.execute(sql, val)
    db.commit()

    # 브라우저 종료
    context.close()
    browser.close()

# 데이터베이스 연결 종료
cursor.close()
db.close()