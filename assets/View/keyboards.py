import json

mKB = {
    'one_time': True,
    'buttons':
    [
        [
            {
                "action":
                    {
                        "type":"text",
                        "payload": "{\"mainMenu\":\"finances\"}",
                        "label": "Счет"
                    },
                "color": "secondary"
            },
            {
                "action":
                    {
                        "type":"text",
                        "payload": "{\"mainMenu\":\"profile\"}",
                        "label": "Профиль"
                    },
                "color": "secondary"
            }
        ],
        [
            {
                "action":
                    {
                        "type":"text",
                        "payload": "{\"mainMenu\":\"history\"}",
                        "label": "История"
                    },
                "color": "secondary"
            },
            {
                "action":
                    {
                        "type":"text",
                        "payload": "{\"mainMenu\":\"QR\"}",
                        "label": "Код"
                    },
                "color": "secondary"
            }          
        ]
    ]
}


eKB = {
    'one_time': True,
    'buttons':
    [        
        [
            {
                "action":
                    {
                        "type":"text",
                        "payload": "{\"eyeColor\":\"green\"}",
                        "label": "Зеленый"
                    },
                "color": "secondary"
            },
            {
                "action":
                    {
                        "type":"text",
                        "payload": "{\"eyeColor\":\"blue\"}",
                        "label": "Синий"
                    },
                "color": "secondary"
            }                
        ],
        [
            {
                "action":
                    {
                        "type":"text",
                        "payload": "{\"eyeColor\":\"brown\"}",
                        "label": "Карие"
                    },
                "color": "secondary"
            }               
        ]   
    ]
}

hCKB = {
        'one_time': True,
        'buttons':
        [
            [
                {
                    "action":
                        {
                            "type":"text",
                            "payload": "{\"button\":\"name\"}",
                            "label": "Имя"
                        },
                    "color": "secondary"
                },
                {
                    "action":
                        {
                            "type":"text",
                            "payload": "{\"button\":\"password\"}",
                            "label": "Пароль"
                        },
                    "color": "secondary"
                }                
            ],
            [
                {
                    "action":
                        {
                            "type":"text",
                            "payload": "{\"button\":\"eyes\"}",
                            "label": "Цвет Глаз"
                        },
                    "color": "secondary"
                },

                {
                    "action":
                        {
                            "type":"text",
                            "payload": "{\"button\":\"hair\"}",
                            "label": "Цвет волос"
                        },
                    "color": "secondary"
                }                
            ],
            [
                {
                "action":
                    {
                        "type":"text",
                        "payload": "{\"button\":\"end\"}",
                        "label": "Завершить"
                    },
                "color": "negative"
                },
                
                {
                "action":
                    {
                        "type":"text",
                        "payload": "{\"button\":\"confirm\"}",
                        "label": "Подтвердить"
                    },
                "color": "positive"
                }       
                
            ]
        ]
    }
humanCreatorKB = json.dumps(hCKB)
eyeColorKB = json.dumps(eKB)
mainKB = json.dumps(mKB)