from operator import itemgetter

from plotly.graph_objs import Bar
from plotly import offline

import requests

# Make an API call and store the response.
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print(f"Status code: {r.status_code}")

# Process information about each submission. 
submission_ids = r.json()
submission_dicts = []
for submission_id in submission_ids[:30]:
    # Make a separate API call for each submission.
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    response_dict = r.json()
    
    # Build a dictionary for each article.
    submission_dict = {
        'title': response_dict['title'],
        'hn_link':f"http://ycombinator.com/item?id={submission_id}",
        'comments':response_dict['descendants'],
    }
    submission_dicts.append(submission_dict)
    
submission_dicts = sorted(
    submission_dicts, key=itemgetter('comments'), reverse=True
    )
    
article_links, comments = [], []
for submission_dict in submission_dicts:
    article_name = submission_dict['title']
    article_url = submission_dict['hn_link']
    article_link = f"<a href='{article_url}'>{article_name}</a>"
    article_links.append(article_link)
    comments.append(submission_dict['comments'])
    
# Make visualization.
data = [{
    'type':'bar',
    'x':article_links,
    'y':comments,
}]

my_layout = {
    'title':'Most commented new on www.haker-news.com',
    'titlefont':{'size':28},
    'xaxis':{
        'title':'Articles',
        'titlefont':{'size':24},
        'tickfont':{'size':14},
    },
    'yaxis':{'title':'Number of comments'}
}

fig = {'data':data, 'layout':my_layout}
offline.plot(fig, filename='hn_barchart.html')