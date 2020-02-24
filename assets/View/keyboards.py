import json


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