from collections import OrderedDict

favorite_languages = OrderedDict()      #此Method將創建一個有序字典

favorite_languages['jen'] = 'python'
favorite_languages['sarah'] = 'c'
favorite_languages['edward'] = 'ruby'
favorite_languages['vincnet'] = 'python'

print(favorite_languages)

for name, language in favorite_languages.items():
    print(name.title()+ " 's favorite is " + language.title() + '.')

