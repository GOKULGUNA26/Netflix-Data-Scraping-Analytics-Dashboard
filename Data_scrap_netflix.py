def get_title(new_soup):
  try:
    title = new_soup.find('h2')
    title_value = title.text
    title_string = title_value.strip()

  except AttributeError:
    title_string = ''

  return title_string


def get_releaseyear(new_soup):
    try:
      year = new_soup.find_all('li', class_='default-ltr-cache-op52f4 e15y75hc0')[0].text.strip()

    except AttributeError:
      year = ''
    return year

def get_genre(new_soup):
    try:
      genre = new_soup.find_all('li', class_='default-ltr-cache-op52f4 e15y75hc0')[2].text.strip()

    except AttributeError:
      genre = ''
    return genre


def get_cast(new_soup):
    try:
      cast = new_soup.find('span', class_='default-ltr-cache-h4l35x euy28770').text.strip()

    except AttributeError:
      cast = ''
    return cast

def get_desc(new_soup):
    try:
      desc = new_soup.find('span', class_='default-ltr-cache-6cq6mb euy28770').text.strip()

    except AttributeError:
      desc = ''
    return desc

def get_status(new_soup):
    try:
      status = new_soup.find('span', class_='default-ltr-cache-1r926vp euy28770').text

    except AttributeError:
      status = ''
    return status





if __name__ == '__main__':
  HEADERS = ({'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36', 'Accept-Language': 'en-US, en;q=0.5'})
  URL ='https://www.netflix.com/in/browse/genre/34399'



  webpage = requests.get(URL, headers=HEADERS)
  soup = BeautifulSoup(webpage.content, 'html.parser')
  links = soup.find_all('a', attrs={'class':'nm-collections-title nm-collections-link'})
  links_list = []

  for link in links:
    links_list.append(link.get('href'))

  d = {'title':[], 'release_year':[], 'genre':[], 'cast':[], 'description':[], 'status':[]}


  for link in links_list[:2]:
    new_webpage = requests.get(link, headers=HEADERS)
    new_soup = BeautifulSoup(new_webpage.content, 'html.parser')
    

    try:
        d['title'].append(get_title(new_soup))
    except:
        d['title'].append(None)

    try:
        d['release_year'].append(get_releaseyear(new_soup))
    except:
        d['release_year'].append(None)

    try:
        d['genre'].append(get_genre(new_soup))
    except:
        d['genre'].append(None)

    try:
        d['cast'].append(get_cast(new_soup))
    except:
        d['cast'].append(None)


    try:
        d['description'].append(get_desc(new_soup))
    except:
        d['description'].append(None)

    try:
        d['status'].append(get_status(new_soup))
    except:
        d['status'].append(None)


netflix_df = pd.DataFrame.from_dict(d)
netflix_df['title'] = netflix_df['title'].replace('', np.nan)
netflix_df = netflix_df.dropna(subset=['title'])
netflix_df.to_csv('netflix_data.csv', header=True, index=False)
