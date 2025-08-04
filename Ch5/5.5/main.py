import requests
from bs4 import BeautifulSoup

def main():
    print("Hey!")
    words, images = CountWordsAndImages("https://www.espn.com")
    print(f"Words: {words}\tImages: {images}\n")

def CountWordsAndImages(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/115.0.0.0 Safari/537.36"
    }
    try:
        resp = requests.get(url, headers=headers)
        resp.raise_for_status()

        doc = BeautifulSoup(resp.text, 'html.parser')
    except requests.RequestException as e:
        print(f"Execption: {e}")
        doc = None
    except Exception as e:
        print(f"Exception during doc traversal: {e}")
        doc = None
    return countWordsAndImages(doc)
    
def countWordsAndImages(doc):
    numImgs = len(doc.find_all("img"))
    numWords = 0
    for text_node in doc.find_all(string=True):
        numWords += len(text_node.split())
    return numWords, numImgs

main()   

#  CountWordsAndImages does an HTTP GET request for the HTML
#  document url and returns the number of words and images in it.
# func CountWordsAndImages(url string) (words, images int, err error) {
# 	resp, err := http.Get(url)
# 	if err != nil {
# 		return
# 	}
# 	doc, err := html.Parse(resp.Body)
# 	resp.Body.Close()
# 	if err != nil {
# 		err = fmt.Errorf("parsing HTML: %s", err)
# 		return
# 	}
# 	words, images = countWordsAndImages(doc)
# 	return
# }