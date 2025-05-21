import requests

def generate_blog_on_title(title):
    prompt = "Generate a nice looking blog with some emojis scattered throughout but not too many, use the english language, be polite and respectful, be nice to the viewers and address them when you see fit, it should not be an overly long blog post but also not very short, the topic of the blog post should be: " + title 

    response = requests.post(
        "http://localhost:11434/api/generate".
        json = {
                "model": "gemma",
                "prompt": prompt,
                "stream": False
        }
    )

    if response.status_code == 200:
        result = response.json()
        print("=== Blog Output ===\n")
        print(result['response'])
    else:
        print("Error:", response.status_code, response.text)

def 
