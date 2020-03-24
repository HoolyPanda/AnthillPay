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

dKB = {
    'one_time': True,
    'buttons':
    [        
        [
            {
                "action":
                    {
                        "type":"text",
                        "payload": "{\"homeDistrict\":\"Фавеллы\"}",
                        "label": "Фавеллы"
                    },
                "color": "secondary"
            },
            {
                "action":
                    {
                        "type":"text",
                        "payload": "{\"homeDistrict\":\"Ист-Енд\"}",
                        "label": "Ист-Енд"
                    },
                "color": "secondary"
            },
            {
                "action":
                    {
                        "type":"text",
                        "payload": "{\"homeDistrict\":\"Коулун\"}",
                        "label": "Коулун"
                    },
                "color": "secondary"
            }               
        ],
        [
            {
                "action":
                    {
                        "type":"text",
                        "payload": "{\"homeDistrict\":\"Тобэй\"}",
                        "label": "Тобэй"
                    },
                "color": "secondary"
            },
            {
                "action":
                    {
                        "type":"text",
                        "payload": "{\"homeDistrict\":\"Доминго\"}",
                        "label": "Доминго"
                    },
                "color": "secondary"
            },
            {
                "action":
                    {
                        "type":"text",
                        "payload": "{\"homeDistrict\":\"Дурбан\"}",
                        "label": "Дурбан"
                    },
                "color": "secondary"
            }               
        ],
        [
            {
                "action":
                    {
                        "type":"text",
                        "payload": "{\"homeDistrict\":\"Кангване\"}",
                        "label": "Кангване"
                    },
                "color": "secondary"
            } 
        ]
        
    ]
}

heKB = {
    'one_time': True,
    'buttons':
    [
        [
            {
                "action":
                    {
                        "type":"text",
                        "payload": "{\"height\":\"short\"}",
                        "label": "Низкий"
                    },
                "color": "secondary"
            },
            {
                "action":
                    {
                        "type":"text",
                        "payload": "{\"height\":\"medium\"}",
                        "label": "Средний"
                    },
                "color": "secondary"
            }
        ],
        [
            {
                "action":
                    {
                        "type":"text",
                        "payload": "{\"height\":\"tall\"}",
                        "label": "Высокий"
                    },
                "color": "secondary"
            }         
        ]
    ]
}

nKB = {
    'one_time': True,
    'buttons':[]
}
bKB = {
    'one_time': True,
    'buttons':
    [ 
        [
            {
                "action":
                    {
                        "type":"text",
                        "payload": "{\"--\":\"--\"}",
                        "label": "Начать"
                    },
                "color": "secondary"
            }               
        ]   
    ]
}
wKB = {
    'one_time': True,
    'buttons':
    [        
        [
            {
                "action":
                    {
                        "type":"text",
                        "payload": "{\"workPlace\":\"shogun\"}",
                        "label": "ShoGun"
                    },
                "color": "secondary"
            },
            {
                "action":
                    {
                        "type":"text",
                        "payload": "{\"workPlace\":\"sintech\"}",
                        "label": "SinTech"
                    },
                "color": "secondary"
            },
            {
                "action":
                    {
                        "type":"text",
                        "payload": "{\"workPlace\":\"cybersteel\"}",
                        "label": "CyberSteel"
                    },
                "color": "secondary"
            }               
        ],
        [
            {
                "action":
                    {
                        "type":"text",
                        "payload": "{\"workPlace\":\"c-corp\"}",
                        "label": "C-Corp"
                    },
                "color": "secondary"
            },
            {
                "action":
                    {
                        "type":"text",
                        "payload": "{\"workPlace\":\"dell\"}",
                        "label": "Dell"
                    },
                "color": "secondary"
            },
            {
                "action":
                    {
                        "type":"text",
                        "payload": "{\"workPlace\":\"obsnews\"}",
                        "label": "OBS News"
                    },
                "color": "secondary"
            }               
        ],
        [
            {
                "action":
                    {
                        "type":"text",
                        "payload": "{\"workPlace\":\"workless\"}",
                        "label": "Безработный"
                    },
                "color": "secondary"
            } 
        ]
        
    ]
}

trKB = {
    'one_time': True,
    'buttons':
    [        
        [
            {
                "action":
                    {
                        "type":"text",
                        "payload": "{\"additionalFunction\":\"Перевести деньги\"}",
                        "label": "Перевести деньги"
                    },
                "color": "secondary"
            },
            {
                "action":
                    {
                        "type":"text",
                        "payload": "{\"additionalFunction\":\"Валидация\"}",
                        "label": "Валидация"
                    },
                "color": "secondary"
            }                
        ]  
    ]
}

wKB = {
    'one_time': True,
    'buttons':
    [        
        [
            {
                "action":
                    {
                        "type":"text",
                        "payload": "{\"workPlace\":\"shogun\"}",
                        "label": "ShoGun"
                    },
                "color": "secondary"
            },
            {
                "action":
                    {
                        "type":"text",
                        "payload": "{\"workPlace\":\"sintech\"}",
                        "label": "SinTech"
                    },
                "color": "secondary"
            },
            {
                "action":
                    {
                        "type":"text",
                        "payload": "{\"workPlace\":\"cybersteel\"}",
                        "label": "CyberSteel"
                    },
                "color": "secondary"
            }               
        ],
        [
            {
                "action":
                    {
                        "type":"text",
                        "payload": "{\"workPlace\":\"c-corp\"}",
                        "label": "C-Corp"
                    },
                "color": "secondary"
            },
            {
                "action":
                    {
                        "type":"text",
                        "payload": "{\"workPlace\":\"dell\"}",
                        "label": "Dell"
                    },
                "color": "secondary"
            },
            {
                "action":
                    {
                        "type":"text",
                        "payload": "{\"workPlace\":\"obsnews\"}",
                        "label": "OBS News"
                    },
                "color": "secondary"
            }               
        ],
        [
            {
                "action":
                    {
                        "type":"text",
                        "payload": "{\"workPlace\":\"workless\"}",
                        "label": "Безработный"
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
                        "payload": "{\"eyeColor\":\"зеленые\"}",
                        "label": "Зеленый"
                    },
                "color": "secondary"
            },
            {
                "action":
                    {
                        "type":"text",
                        "payload": "{\"eyeColor\":\"Синие\"}",
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
                        "payload": "{\"eyeColor\":\"коричневые\"}",
                        "label": "Карий"
                    },
                "color": "secondary"
            }               
        ]   
    ]
}
hairKB = {
        'one_time': True,
        'buttons':
        [
            [
                {
                    "action":
                        {
                            "type":"text",
                            "payload": "{\"hairColor\":\"Русые\"}",
                            "label": "Русые"
                        },
                    "color": "secondary"
                },
                {
                    "action":
                        {
                            "type":"text",
                            "payload": "{\"hairColor\":\"Шатен\"}",
                            "label": "Шатен"
                        },
                    "color": "secondary"
                },
                {
                    "action":
                        {
                            "type":"text",
                            "payload": "{\"hairColor\":\"Рыжие\"}",
                            "label": "Рыжие"
                        },
                    "color": "secondary"
                }                     
            ],
            [
                {
                    "action":
                        {
                            "type":"text",
                            "payload": "{\"hairColor\":\"Брюнет\"}",
                            "label": "Брюнет"
                        },
                    "color": "secondary"
                },
                {
                    "action":
                        {
                            "type":"text",
                            "payload": "{\"hairColor\":\"Цветные\"}",
                            "label": "Цветные"
                        },
                    "color": "secondary"
                }                     
            ]
        ]
}
hCKB =  {
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
                            "payload": "{\"button\":\"work\"}",
                            "label": "Работа"
                        },
                    "color": "secondary"
                },
                {
                    "action":
                        {
                            "type":"text",
                            "payload": "{\"button\":\"district\"}",
                            "label": "Район"
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
                            "payload": "{\"button\":\"height\"}",
                            "label": "Рост"
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

beginKB  = json.dumps(bKB)
districtKB = json.dumps(dKB)
nullKB = json.dumps(nKB)
heightKB = json.dumps(heKB)
worksKB = json.dumps(wKB)
hairKB = json.dumps(hairKB)    
humanCreatorKB = json.dumps(hCKB)
eyeColorKB = json.dumps(eKB)
mainKB = json.dumps(mKB)
additionalFunctionsKB = json.dumps(trKB)