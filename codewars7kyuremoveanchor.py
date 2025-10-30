#https://www.codewars.com/kata/51f2b4448cadf20ed0000386/train/python
'''
Remove anchor from URL 7kyu

Complete the function/method so that it returns the url with anything after the anchor (#) removed.

Examples
"www.codewars.com#about" --> "www.codewars.com"
"www.codewars.com?page=1" -->"www.codewars.com?page=1"

RM:  There is a regular expressions tag.
'''
def remove_url_anchor(url):
    if "#" in url:
        return url[0:url.index("#")]
    else:
        return url


print(remove_url_anchor("www.codewars.com#about")) #print www.codewars.com
print(remove_url_anchor("www.codewars.com?page=1")) #print www.codewars.com?page=1
print(remove_url_anchor("www.codewars.com/katas/?page=1#about")) #print www.codewars.com/katas/?page=1
print(remove_url_anchor("www.codewars.com/katas")) #print www.codewars.com/katas

import re
def remove_url_anchor(url):
    if "#" in url:
        beforeanchor = re.compile(r".*#")
        return beforeanchor.findall(url)[0][:-1]
    else:
        return url


print(remove_url_anchor("www.codewars.com#about")) #print www.codewars.com
print(remove_url_anchor("www.codewars.com?page=1")) #print www.codewars.com?page=1
print(remove_url_anchor("www.codewars.com/katas/?page=1#about")) #print www.codewars.com/katas/?page=1
print(remove_url_anchor("www.codewars.com/katas")) #print www.codewars.com/katas

#Use index or split to extract the url before anchor tag #
url = "www.codewars.com#about"
print(url.index("#")) #print 16
print(url[0:url.index("#")]) #print www.codewars.com
print(url.split("#")) #print ['www.codewars.com', 'about']

#Brief regular expressions example lessons
url = "www.codewars.com#about"
beforeanchor = re.compile(r".*#")
print(beforeanchor.findall(url)) #print ['www.codewars.com#']
print(type(beforeanchor.findall(url))) #print <class 'list'>
print(beforeanchor.findall(url)[0][:-1]) #print www.codewars.com
print(re.split(r"#", url)) #print ['www.codewars.com', 'about']
print(re.split(r"#", url)[0]) #print www.codewars.com
beforeanchor2 = r".*#"
print(re.search(beforeanchor2, url)) #print <re.Match object; span=(0, 17), match='www.codewars.com#'>
print(re.search(beforeanchor2, url).group()) #print www.codewars.com#
print(re.search(beforeanchor2, url).group()[:-1]) #print www.codewars.com

#User submissions
def remove_url_anchor(url):
    import re
    return re.sub('#.*$', '', url)
