# -*- coding: utf-8 -*-

from grequests import get, map

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
        print 'https://www.graphicsprings.com/filestorage/stencils/{filename}'.format(filename=item['filename'])
