import os
import re
import requests
from urllib.parse import urlencode
from multiprocessing.pool import Pool


def get_page(offset):
    params = {
        'include': 'data[*].is_normal,admin_closed_comment,reward_info,is_collapsed,annotation_action,annotation_detail,collapse_reason,is_sticky,collapsed_by,suggest_edit,comment_count,can_comment,content,editable_content,voteup_count,reshipment_settings,comment_permission,created_time,updated_time,review_info,relevant_info,question,excerpt,relationship.is_authorized,is_author,voting,is_thanked,is_nothelp,is_labeled;data[*].mark_infos[*].url;data[*].author.follower_count,badge[*].topics',
        'limit': 5,
        'offset': offset,
        'platform': 'desktop',
        'sort_by': 'default'
    }

    url = 'https://www.zhihu.com/api/v4/questions/26297181/answers?' + urlencode(params)

    try:
        response = requests.get(url, headers={
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36'
        })
        if response.status_code == 200:
            return response.json()
    except requests.ConnectionError:
        return None


def get_images(json):
    if json.get('data'):
        for item in json['data']:
            content = item['content']
            user = item['author']['name']
            imgs = set(re.findall('<img.*? data-original="(.*?)".*?>', content, re.S))
            if len(imgs) > 0:
                yield {
                    'user': user,
                    'imgs': imgs
                }


def save_img(item):
    if not os.path.exists('imgs/' + item['user']):
        os.mkdir('imgs/' + item['user'])

    for img in item['imgs']:
        try:
            response = requests.get(img)
            if response.status_code == 200:
                file_path = 'imgs/{}/{}'.format(item['user'], os.path.basename(img))
                if not os.path.exists(file_path):
                    with open(file_path, 'wb') as f:
                        f.write(response.content)
        except requests.ConnectionError:
            print('Failed to Save Image: ', img)


def main(offset):
    json = get_page(offset)
    for item in get_images(json):
        save_img(item)


if __name__ == '__main__':
    pool = Pool()
    groups = ([x * 20 for x in range(10)])
    pool.map(main, groups)
    pool.close()
    pool.join()
