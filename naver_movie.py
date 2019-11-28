import requests
from bs4 import BeautifulSoup
import time
from csv_save import save_to_file

def get_last_page(M_ID):
    URL = f"https://movie.naver.com/movie/point/af/list.nhn?st=mcode&sword={M_ID}&target=after"
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, "html.parser")

    pagination = soup.find("div", {"class": "h5_right_txt"})
    if pagination:
        num = pagination.find("strong").string
        # print(num)
        max_page = int(num) / 10 + 1
        # print(int(page))
        return int(max_page)
    else:
        return None


def extract_comm(html, title, genre):
    comment = html.get_text('|', strip=True).split('|')[3]
    score = html.find("em").string
    return {'title': title, 'score': score, 'genre': genre, 'comment': comment}


def extract_comms(last_page,M_ID):
    URL = f"https://movie.naver.com/movie/point/af/list.nhn?st=mcode&sword={M_ID}&target=after"
    comments_info = []
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, "html.parser")
    info = soup.find("div", {"class": "choice_movie_info"})
    title = info.find("h5").get_text(strip=True)
    genre = soup.find("td").get_text(strip=True).split('|')[0]
    if '개봉' in genre:
        return

    for page in range(last_page):
        print(f"Scrapping naver page {page+1}")
        result = requests.get(f"{URL}&page={page+1}")
        soup = BeautifulSoup(result.text, "html.parser")
        results = soup.find_all("td", {"class": "title"})
        # print(results[0].get_text(strip=True))
        for result in results:
            # comments['title']=title
            comm = extract_comm(result, title, genre)
            # comments.update(extract_comm(result))
            comments_info.append(comm)
        # print(comments_info)
    return comments_info


# extract_comms(1)


def get_movie_comm(i):
    last_page = get_last_page(i)
    if last_page is None:
        return None
    
    if last_page<120:
        comments = extract_comms(last_page,i)
    else:
        comments = extract_comms(120,i)

    if len(comments) is not 0:
        # print(comments)
        save_to_file(comments)
    return comments
