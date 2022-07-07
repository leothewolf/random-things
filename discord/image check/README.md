Use the following code to check if the image URL given is a valid discord image URL for passing to embeds and within message : 

<br>

> Discord accepts `png,jpg,jpeg,webp,gif` as stated here : https://discord.com/developers/docs/reference#image-formatting-image-formats and embeds accept URLs starting with `http/https`. Further in the function we are checking if the URL we found is a valid URL using headers we recieved on requesting the image.

<br>

```
def img_url_checker(url):
    import requests
    
    if not url.startswith("http"):
        return False
    
    r = requests.get(url)
    
    if r.status_code != 304 and r.status_code != 200:
        return False
    
    valid_img_prefix = ['image/png','image/jpg','image/jpeg','image/webp','image/gif']
    
    if r.headers['Content-Type'] in valid_img_prefix:
        return True
    else:
        return False
```
