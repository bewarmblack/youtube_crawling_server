# youtube_crawling_server
현재 파일 2개 있는데, 한개는 sync(동기) 방식이고 다른 하나는 async(비동기) 방식임
async/await 구문 사용 시, time sleep을 활용해 로딩 시간을 조절하고 사람인 것처럼 구현할 수 있따.

mysql서버에 연결 현재 안된 상태.
연결 됬다는 가정 하에, playwright 사용하여 입력해 놓은 youtube link에 접속하여, 각각의 댓글, 조회수 등등을 
crawling 해오는 과정임.
