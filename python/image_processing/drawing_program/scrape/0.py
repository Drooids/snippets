# -*- coding: utf-8 -*-

from grequests import get, map
import wget

for response in map(
    (
        get(
            url,
            headers={
                'X-Requested-With': 'XMLHttpRequest',
            },
        )
        for url in [
            'http://www.graphicsprings.com/ajax/fetch/normal/0/{page}'.format(page=page + 1)
            for page in range(1, 200)
        ]
    )
):
    for item in response.json()['data']['items']:
        down_url = 'https://www.graphicsprings.com/filestorage/stencils/{filename}'.format(filename=item['filename'])
        wget.download(down_url);
        print down_url
