### python-pixabay
Python 3 interface to Pixabay API.

### SYNOPSIS
```python3

from python_pixabay import Pixabay

pix = Pixabay('my_pixabay_api_key')

# default image search
img_search = pix.image_search()

# default video search
vid_search = pix.video_search()

# view the content of the searches
print(img_search)
print(vid_search)

# custom image search

cis = pix.image_search(q = 'cats dogs',
					   lang = 'es',
					   response_group = 'high_resolution',
					   image_type = 'photo',
					   orientation = 'horizontal',
					   category = 'animals',
					   safesearch = 'true',
					   order = 'latest',
					   page = 2,
					   per_page = 3
					   )

print(cis)

# custom video search

cvs = pix.video_search(q = 'cats',
					   lang = 'fr',
					   video_type = 'animation',
					   category = 'animals',
					   page = 1,
					   per_page = 4
					   )

print(cvs)

```

### SEE ALSO
[Pixabay API documentations](https://pixabay.com/api/docs)
