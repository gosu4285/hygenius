from PyQt5.QtCore import QRectF


element_info = \
    {
        'H': {
            'number': '1',
            'name': 'Hydrogen',
            'rect': QRectF(30, 59, 82, 81),  # 사각형 왼쪽위(x좌표, y좌표, 넓이, 높이)
            'description': '(1) 한글이름 : 탄소\n'
                           '(2) 영문이름 : \n'
                           '(3) 설명 : polymer PR, Color filter 등에 많이 포함되어있으며 어쩌고\n'
                           '(4) 연관공정 : 한자 다\n'
                           '(5) 불량 분석 이력 Link',
            'link_url': ['https://en.wikipedia.org/wiki/Hydrogen', 'https://en.wikipedia.org/wiki/Lithium']
        },
        'Li': {
            'number': '3',
            'name': 'Lithium',
            'rect': QRectF(30, 156, 82, 81),
            'description': '리튬에 대한 설명',
            'link_url': ['https://en.wikipedia.org/wiki/Lithium']
        }
    }
