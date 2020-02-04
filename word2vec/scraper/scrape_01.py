import os
import re
import requests
from bs4 import BeautifulSoup
import pandas as pd

realpath = os.path.dirname(os.path.realpath(__file__))
folderpath = realpath + "/scrap-results"

def scrap_tirto(query, category_list = None):
    url_base = "https://tirto.id"
    url_query = url_base + "/search?q=" + str(query)
    req = requests.get(url_query)
    soup = BeautifulSoup(req.content, "html5lib")

    # get total page number
    try:
        find_pagination = soup.findAll("li", attrs = {"class": "pagination-item"})
        pagination_list = [row.a.text for row in find_pagination]
        total_page = int(pagination_list[-2])
    except:
        print("Article Not Found")
        return None

    # iterate each page number, to get the title and url
    articles = []
    for page_num in range(1, total_page+1):
        url = url_query + "&p=" + str(page_num)
        r = requests.get(url)
        s = BeautifulSoup(r.content, "html5lib")

        find_article = s.findAll("div", attrs = {"class": "news-list-fade"})
        for row in find_article:
            article = {}
            article['title'] = row.h1.text
            article['url'] = url_base + row.a['href']
            articles.append(article)

    # loop through each stored url
    counter = 0
    for article in articles:
        counter += 1

        # access the article url
        req_article = requests.get(article['url'])
        soup_article = BeautifulSoup(req_article.content, "html5lib")

        # get article category
        find_category = soup_article.findAll("a", attrs = {"itemprop": "item"})
        if len(find_category):
            article['category'] = find_category[-1].text
        else:
            article['category'] = "Unknown"

        # skip the scrapping if category is not on the list
        if article['category'] not in category_list:
            article.clear()
            continue
        
        # get author name and posted date
        find_author_date = soup_article.find("span", attrs = {"class": "detail-date"})

        match = re.search(":[a-zA-Z\\. ]+-", find_author_date.text)
        if match is not None:
            article['author_name'] = match.group(0)[2:-2].title()

        match = re.search("\\d{1,2} [a-zA-Z]+ \\d{4}", find_author_date.text)
        if match is not None:
            article['posted_date'] = match.group(0)

        # get article content (but exclude the "Baca juga" section)
        find_baca_juga_section = soup_article.find("div", attrs = {"class": "baca-holder"})
        if find_baca_juga_section is not None:
            for row in find_baca_juga_section:
                row.decompose()

        content = ""
        article_table = soup_article.findAll("div", attrs = {"class": "content-text-editor"})[:-1]
        for row in article_table:
            content += re.sub(r'\s+', ' ', row.text) + " "
        article['content'] = content

        print(counter, "out of", len(articles))

    # remove empty dictionary from the list
    articles = list(filter(None, articles))

    # return the dictionary
    return articles

def save_complete_content2tsv(dictionary, filename):
    df = pd.DataFrame(dictionary)
    df.to_csv(folderpath + "/" + filename, sep = "\t", index = False)

def save_content2txt(dictionary, filename):
    with open(folderpath + "/" + filename, "w", encoding = "utf-8") as file:
        for d in dictionary:
            file.write(d['content'] + "\n")

def convert_tsv2txt(source_filename, destination_filename):
    df = pd.read_csv(folderpath + "/" + source_filename, sep = '\t', encoding = "utf-8")

    with open(folderpath + "/" + destination_filename, "w", encoding = "utf-8") as file:
        for row in df['content']:
            file.write(row + "\n")

# tirto_category = \
# ['Bisnis', 'Current Issue', 'Ekonomi', 'Film', 'Foto', 'Foto Arta', 'Foto Raga', 'Gaya Hidup', \
# 'Hobi', 'Hukum', 'Humaniora', 'Indepth', 'Kesehatan', 'Marketing', 'Musik', 'News', 'Olahraga', \
# 'Pendidikan', 'Politik', 'Sosial Budaya', 'Teknologi']

if __name__ == '__main__':
    # input
    query = "bca"
    category_list = ["Ekonomi"]

    # scrap
    result = scrap_tirto(query, category_list)

    # save to file (tsv for complete data, txt for content only)
    filename = "tirto_" + query + "_" + '_'.join(category_list).lower()
    save_complete_content2tsv(result, filename + ".tsv")
    save_content2txt(result, filename + ".txt")

    #convert_tsv2txt("tirto_bank_bisnis_ekonomi.tsv", "tirto_bank_bisnis_ekonomi.txt")