import re


def a():
    content = 'hello 1234 world'
    result = re.match(r'\w+\s(\d+)\s\w+', content, re.S)
    print(result.group())
    print(result.group(1))


def b():
    content = 'Hello, my phone number is 010-86432100 and email is cqc@cuiqingcai.com, and my website is http://cuiqingcai.com.'
    result = re.search(r'\d+-\d+', content)
    if result:
        print(result.group())

    results = re.findall(r'\w+', content)
    for result in results:
        print(result)


def c():
    content = 'Hello, my phone number is 010-86432100 and email is cqc@cuiqingcai.com, and my website is http://cuiqingcai.com.'
    content = re.sub(r'\d+-\d+', 'xxxx', content)
    print(content)


c()
