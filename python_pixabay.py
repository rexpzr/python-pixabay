from requests import get

root_url="https://pixabay.com/api/"

class Pixabay:
    def __init__(self, api_key):
        self.api_key = api_key
        
    def image_search(self, q = 'yellow flower', lang = 'en', id = '',
                           response_group = 'image_details',
                           image_type = 'all',
                           orientation = 'all',
                           category = '',
                           min_width = 0,
                           min_height = 0,
                           editors_choice = 'false',
                           safesearch = 'false',
                           order = 'popular',
                           page = 1,
                           per_page = 20,
                           callback = '',
                           pretty = 'false'):

        payload = {'key': self.api_key, 'q': q, 'lang': lang, 'id': id,
                'response_group': response_group, 'image_type': image_type,
                'orientation': orientation, 'category': category,
                'min_width': min_width, 'min_height': min_height,
                'editors_choice': editors_choice, 'safesearch': safesearch,
                'order': order, 'page': page, 'per_page': per_page,
                'callback': callback, 'pretty': pretty
                }
        
        return get(root_url, params=payload).json()

    def video_search(self, q = 'yellow flower', lang = 'en', id = '',
                           video_type = 'all',
                           category = '',
                           min_width = 0,
                           min_height = 0,
                           editors_choice = 'false',
                           safesearch = 'false',
                           order = 'popular',
                           page = 1,
                           per_page = 20,
                           callback = '',
                           pretty = 'false'):

        payload = {'key': self.api_key, 'q': q, 'lang': lang, 'id': id,
                'video_type': video_type,
                'category': category,
                'min_width': min_width, 'min_height': min_height,
                'editors_choice': editors_choice, 'safesearch': safesearch,
                'order': order, 'page': page, 'per_page': per_page,
                'callback': callback, 'pretty': pretty}

        return get(root_url + "videos/", params=payload).json()
