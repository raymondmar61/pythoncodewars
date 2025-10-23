#https://www.codewars.com/kata/514a024011ea4fb54200004b/train/python
'''
Extract the domain name from a URL 5kyu

Write a function that when given a URL as a string, parses out just the domain name and returns it as a string. For example:

* url = "http://github.com/carbonfive/raygun" -> domain name = "github"
* url = "http://www.zombie-bites.com"         -> domain name = "zombie-bites"
* url = "https://www.cnet.com"                -> domain name = cnet"

test.assert_equals(domain_name("http://google.com"), "google")
test.assert_equals(domain_name("http://google.co.jp"), "google")
test.assert_equals(domain_name("https://123.net"), "123")
test.assert_equals(domain_name("https://hyphen-site.org"), "hyphen-site")
test.assert_equals(domain_name("http://codewars.com"), "codewars")
test.assert_equals(domain_name("www.xakep.ru"), "xakep")
test.assert_equals(domain_name("https://youtube.com"), "youtube")
test.assert_equals(domain_name("http://www.codewars.com/kata/"), "codewars")
test.assert_equals(domain_name("icann.org"), "icann")
'''
import re
def domain_name(url):
    eachurllist = url
    compileprefix = re.compile(r"(https://www.\w+(-)?\w+)|(http://www.\w+(-)?\w+)|(https://\w+(-)?\w+)|(http://\w+(-)?\w+)|(www.\w+(-)?\w+)|(\w+(-)?\w+)") #The (-)? means the hypen is optional between the letters and numbers \w+.
    finddomainname = compileprefix.search(eachurllist)
    extractactualdomain = finddomainname.group()
    if "." in extractactualdomain:
        return (extractactualdomain[extractactualdomain.index(".") + 1:])
    elif "//" in extractactualdomain:
        return (extractactualdomain[extractactualdomain.index("//") + 2:])
    else:
        return (extractactualdomain)


urllist = ["http://github.com/carbonfive/raygun", "http://www.zombie-bites.com", "https://www.cnet.com", "http://google.com", "http://google.co.jp", "https://123.net", "https://hyphen-site.org", "http://codewars.com", "www.xakep.ru", "https://youtube.com", "http://www.codewars.com/kata/", "icann.org"]
for eachurllist in urllist:
    print(domain_name(eachurllist))
    '''
    github
    zombie-bites
    cnet
    google
    google
    123
    hyphen-site
    codewars
    xakep
    youtube
    codewars
    icann
    '''

#Review regular expressions
link = "https://www.cnet.com"
print(re.search(link, "https://www.")) #print None
print(re.search(link, "https://www.") is True) #print False
if re.search(link, "https://www."):
    print("True")
else:
    print("False") #print False
print(re.match("https://www.", link)) #print <re.Match object; span=(0, 12), match='https://www.'>
print(re.search("https://www.", link)) #print <re.Match object; span=(0, 12), match='https://www.'>
compilerobjectfindme = re.compile(link)
print(compilerobjectfindme.findall("https://www.")) #print []
# searchgroupobject = compilerobjectfindme.search("https://www.")
# print(searchgroupobject.group()) #AttributeError: 'NoneType' object has no attribute 'group'
# searchgroupobject = compilerobjectfindme.match("https://www.")
# print(searchgroupobject.group()) #AttributeError: 'NoneType' object has no attribute 'group'
# searchgroupobject = compilerobjectfindme.findall("https://www.")
# print(searchgroupobject.group()) #AttributeError: 'list' object has no attribute 'group'
compileprefix = re.compile(r"(https://www.\w+)|(http://www.\w+)|(https://\w+)|(http://\w+)|(www\w+)")
print(compileprefix.findall(link)) #print [('https://www.cnet', '', '', '', '')]
print(compileprefix.search(link)) #print <re.Match object; span=(0, 16), match='https://www.cnet'>
finddomainname = compileprefix.search(link)
print(finddomainname.group()) #print https://www.cnet
print(finddomainname.group(1)) #print https://www.cnet
print(finddomainname.groups()) #print ('https://www.cnet', None, None, None, None)

#Other solutions
def domain_name(url):
    return url.split("//")[-1].split("www.")[-1].split(".")[0]

import re
def domain_name(url):
    return re.search('(https?://)?(www\d?\.)?(?P<name>[\w-]+)\.', url).group('name')

def domain_name(url): #RM:  think simple.  I didn't need regular expressions.
    url = url.replace('www.','')
    url = url.replace('https://','')
    url = url.replace('http://','')
    
    return url[0:url.find('.')]