from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
import json 
LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])
class Snippet:
    def __init__(self,id,title,code,linenos,language,style,created):
        self.id = id
        self.title = title
        self.code = code
        self.linenos = linenos
        self.language = language
        self.style = style
        self.created=created
    @classmethod
    def from_json(cls, json_string):
        json_dict = json.loads(json_string)
        return cls(**json_dict)
class Flower:
    def __init__(self,id,flowername,flowercolor,isSingle):
        self.id = id
        self.flowername = flowername
        self.flowercolor = flowercolor
        self.isSingle = isSingle
        
    @classmethod
    def from_json(cls, json_string):
        json_dict = json.loads(json_string)
        return cls(**json_dict)

# json_string='''
#     {'id': 1, 
#     'title': 'Title 1',
#     'code': 'courselist=course.objects.all()',
#     'linenos': False, 'style': 'friendly', 'language': 'python'}
    
#     '''
#user = Snippet.from_json(json_string)
#print(user)
#print(user.title)
#print(user.email)
#print(user.phone)