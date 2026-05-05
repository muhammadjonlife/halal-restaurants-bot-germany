cities = ["Berlin", "Hamburg", "München", "Köln", "Frankfurt"]

restaurants = {
    "Berlin": [
        {
            "name": "Hasir Restaurant",
            "address": "Adalbertstraße 10",
            "phone": "+49 30 123456",
            "delivery": True,
            "menu": [
                {"name": "Döner", "price": "6€"},
                {"name": "Chicken Döner", "price": "6.5€"},
                {"name": "Adana Kebab", "price": "12€"},
                {"name": "Iskender Kebab", "price": "13€"},
                {"name": "Grill Teller", "price": "15€"},
                {"name": "Lahmacun", "price": "5€"},
                {"name": "Falafel Teller", "price": "7€"},
                {"name": "Pommes", "price": "3€"},
                {"name": "Ayran", "price": "2€"},
                {"name": "Baklava", "price": "4€"}
            ],
            "link": "https://maps.google.com/?q=Hasir+Berlin"
        },
        {
            "name": "Imren Grill",
            "address": "Karl-Marx-Straße",
            "phone": "+49 30 222222",
            "delivery": True,
            "menu": [
                {"name": "Döner", "price": "6.5€"},
                {"name": "Chicken Döner", "price": "6€"},
                {"name": "Kebab Teller", "price": "11€"},
                {"name": "Adana Teller", "price": "12€"},
                {"name": "Falafel", "price": "5€"},
                {"name": "Linsensuppe", "price": "4€"},
                {"name": "Salat", "price": "4€"},
                {"name": "Reis", "price": "3€"},
                {"name": "Cola", "price": "2€"},
                {"name": "Fanta", "price": "2€"}
            ],
            "link": "https://maps.google.com/?q=Imren+Berlin"
        },
        {
            "name": "Navat",
            "address": "Berlin Zentrum",
            "phone": "+49 30 333333",
            "delivery": False,
            "menu": [
                {"name": "Plov (Osh)", "price": "12€"},
                {"name": "Lagman", "price": "10€"},
                {"name": "Manty", "price": "11€"},
                {"name": "Shashlik (Rind)", "price": "13€"},
                {"name": "Shashlik (Hähnchen)", "price": "12€"},
                {"name": "Samsa", "price": "4€"},
                {"name": "Borschtsch", "price": "5€"},
                {"name": "Salat Achichuk", "price": "4€"},
                {"name": "Tee", "price": "2€"},
                {"name": "Kompot", "price": "3€"}
            ],
            "link": "https://maps.google.com/?q=Navat+Berlin"
        },
        {
            "name": "Aspendos",
            "address": "Kreuzberg",
            "phone": "+49 30 444444",
            "delivery": True,
            "menu": [
                {"name": "Pizza Margherita", "price": "8€"},
                {"name": "Pizza Salami", "price": "9€"},
                {"name": "Pide Käse", "price": "7€"},
                {"name": "Pide Hackfleisch", "price": "8€"},
                {"name": "Döner", "price": "6€"},
                {"name": "Lahmacun", "price": "5€"},
                {"name": "Calzone", "price": "9€"},
                {"name": "Pommes", "price": "3€"},
                {"name": "Ayran", "price": "2€"},
                {"name": "Baklava", "price": "4€"}
            ],
            "link": "https://maps.google.com/?q=Aspendos+Berlin"
        },
        {
            "name": "Tadim Grill",
            "address": "Berlin Mitte",
            "phone": "+49 30 555555",
            "delivery": False,
            "menu": [
                {"name": "Kebab", "price": "7€"},
                {"name": "Chicken Grill", "price": "12€"},
                {"name": "Mixed Grill", "price": "14€"},
                {"name": "Reis", "price": "4€"},
                {"name": "Salat", "price": "4€"},
                {"name": "Pommes", "price": "3€"},
                {"name": "Ayran", "price": "2€"},
                {"name": "Cola", "price": "2€"}
            ],
            "link": "https://maps.google.com/?q=Tadim+Berlin"
        }
    ],

    "Hamburg": [
        {
            "name": "Batman Restaurant",
            "address": "Hamburg Mitte",
            "phone": "+49 40 111111",
            "delivery": True,
            "menu": [
                {"name": "Kebab", "price": "7€"},
                {"name": "Adana Kebab", "price": "12€"},
                {"name": "Chicken Kebab", "price": "11€"},
                {"name": "Grill Teller", "price": "14€"},
                {"name": "Lahmacun", "price": "5€"},
                {"name": "Pommes", "price": "3€"},
                {"name": "Salat", "price": "4€"},
                {"name": "Ayran", "price": "2€"}
            ],
            "link": "https://maps.google.com/?q=Batman+Hamburg"
        },
        {
            "name": "Mardin Grill",
            "address": "Hamburg",
            "phone": "+49 40 222222",
            "delivery": True,
            "menu": [
                {"name": "Döner", "price": "6€"},
                {"name": "Chicken Döner", "price": "6€"},
                {"name": "Kebab Teller", "price": "11€"},
                {"name": "Falafel", "price": "5€"},
                {"name": "Soup", "price": "4€"},
                {"name": "Pommes", "price": "3€"},
                {"name": "Cola", "price": "2€"}
            ],
            "link": "https://maps.google.com/?q=Mardin+Hamburg"
        },
        {
            "name": "Köz Ocakbasi",
            "address": "Hamburg",
            "phone": "+49 40 333333",
            "delivery": False,
            "menu": [
                {"name": "Grill Mix", "price": "15€"},
                {"name": "Adana", "price": "12€"},
                {"name": "Chicken", "price": "11€"},
                {"name": "Reis", "price": "4€"},
                {"name": "Salat", "price": "4€"},
                {"name": "Ayran", "price": "2€"}
            ],
            "link": "https://maps.google.com/?q=Koz+Hamburg"
        },
        {
            "name": "Sarajevo Grill",
            "address": "Hamburg",
            "phone": "+49 40 444444",
            "delivery": True,
            "menu": [
                {"name": "Cevapi", "price": "10€"},
                {"name": "Pljeskavica", "price": "11€"},
                {"name": "Soup", "price": "4€"},
                {"name": "Salat", "price": "4€"},
                {"name": "Pommes", "price": "3€"},
                {"name": "Cola", "price": "2€"}
            ],
            "link": "https://maps.google.com/?q=Sarajevo+Hamburg"
        },
        {
            "name": "Istanbul Kebab",
            "address": "Hamburg",
            "phone": "+49 40 555555",
            "delivery": True,
            "menu": [
                {"name": "Döner", "price": "6€"},
                {"name": "Pizza", "price": "8€"},
                {"name": "Lahmacun", "price": "5€"},
                {"name": "Falafel", "price": "5€"},
                {"name": "Pommes", "price": "3€"},
                {"name": "Ayran", "price": "2€"}
            ],
            "link": "https://maps.google.com/?q=Istanbul+Hamburg"
        }
    ],

    "München": [
        {
            "name": "Dilan MezeBar",
            "address": "Zentrum",
            "phone": "+49 89 111111",
            "delivery": False,
            "menu": [
                {"name": "Grill Teller", "price": "15€"},
                {"name": "Meze Mix", "price": "12€"},
                {"name": "Salat", "price": "5€"},
                {"name": "Soup", "price": "4€"},
                {"name": "Ayran", "price": "2€"}
            ],
            "link": "https://maps.google.com/?q=Dilan+Munich"
        },
        {
            "name": "Kent Restaurant",
            "address": "München",
            "phone": "+49 89 222222",
            "delivery": True,
            "menu": [
                {"name": "Döner", "price": "7€"},
                {"name": "Adana", "price": "12€"},
                {"name": "Kebab Teller", "price": "11€"},
                {"name": "Pommes", "price": "3€"},
                {"name": "Cola", "price": "2€"}
            ],
            "link": "https://maps.google.com/?q=Kent+Munich"
        },
        {
            "name": "Sultanahmet",
            "address": "München",
            "phone": "+49 89 333333",
            "delivery": False,
            "menu": [
                {"name": "Köfte", "price": "12€"},
                {"name": "Soup", "price": "4€"},
                {"name": "Salat", "price": "5€"}
            ],
            "link": "https://maps.google.com/?q=Sultanahmet+Munich"
        },
        {
            "name": "Anatolia Grill",
            "address": "München",
            "phone": "+49 89 444444",
            "delivery": True,
            "menu": [
                {"name": "Chicken Grill", "price": "10€"},
                {"name": "Mixed Grill", "price": "14€"},
                {"name": "Reis", "price": "4€"},
                {"name": "Salat", "price": "4€"}
            ],
            "link": "https://maps.google.com/?q=Anatolia+Munich"
        },
        {
            "name": "Orient Haus",
            "address": "München",
            "phone": "+49 89 555555",
            "delivery": True,
            "menu": [
                {"name": "Falafel", "price": "5€"},
                {"name": "Wrap", "price": "6€"},
                {"name": "Pommes", "price": "3€"},
                {"name": "Cola", "price": "2€"}
            ],
            "link": "https://maps.google.com/?q=Orient+Munich"
        }
    ],

    "Köln": [
        {
            "name": "Mangal Döner",
            "address": "Zentrum",
            "phone": "+49 221 111111",
            "delivery": True,
            "menu": [
                {"name": "Döner", "price": "6.5€"},
                {"name": "Chicken Döner", "price": "6.5€"},
                {"name": "Lahmacun", "price": "5€"},
                {"name": "Pommes", "price": "3€"},
                {"name": "Ayran", "price": "2€"}
            ],
            "link": "https://maps.google.com/?q=Mangal+Koln"
        },
        {
            "name": "Haus des Döners",
            "address": "Köln",
            "phone": "+49 221 222222",
            "delivery": True,
            "menu": [
                {"name": "Döner", "price": "6€"},
                {"name": "Pizza", "price": "8€"},
                {"name": "Falafel", "price": "5€"}
            ],
            "link": "https://maps.google.com/?q=Haus+des+Doners+Koln"
        },
        {
            "name": "Bona'me",
            "address": "Köln",
            "phone": "+49 221 333333",
            "delivery": False,
            "menu": [
                {"name": "Pide", "price": "7€"},
                {"name": "Salat", "price": "5€"}
            ],
            "link": "https://maps.google.com/?q=Boname+Koln"
        },
        {
            "name": "Saray Restaurant",
            "address": "Köln",
            "phone": "+49 221 444444",
            "delivery": True,
            "menu": [
                {"name": "Kebab", "price": "10€"},
                {"name": "Soup", "price": "4€"}
            ],
            "link": "https://maps.google.com/?q=Saray+Koln"
        },
        {
            "name": "Antep Sofrasi",
            "address": "Köln",
            "phone": "+49 221 555555",
            "delivery": False,
            "menu": [
                {"name": "Grill Mix", "price": "14€"},
                {"name": "Adana", "price": "12€"}
            ],
            "link": "https://maps.google.com/?q=Antep+Koln"
        }
    ],

    "Frankfurt": [
        {
            "name": "Ariana Restaurant",
            "address": "Frankfurt",
            "phone": "+49 69 111111",
            "delivery": True,
            "menu": [
                {"name": "Kabuli Palau", "price": "13€"},
                {"name": "Kebab", "price": "11€"},
                {"name": "Soup", "price": "4€"},
                {"name": "Salat", "price": "4€"}
            ],
            "link": "https://maps.google.com/?q=Ariana+Frankfurt"
        },
        {
            "name": "Pak Choi",
            "address": "Frankfurt",
            "phone": "+49 69 222222",
            "delivery": True,
            "menu": [
                {"name": "Chicken Curry", "price": "10€"},
                {"name": "Rice", "price": "4€"}
            ],
            "link": "https://maps.google.com/?q=PakChoi+Frankfurt"
        },
        {
            "name": "Alim Restaurant",
            "address": "Frankfurt",
            "phone": "+49 69 333333",
            "delivery": False,
            "menu": [
                {"name": "Lagman", "price": "10€"},
                {"name": "Manty", "price": "11€"}
            ],
            "link": "https://maps.google.com/?q=Alim+Frankfurt"
        },
        {
            "name": "Sultan Palace",
            "address": "Frankfurt",
            "phone": "+49 69 444444",
            "delivery": True,
            "menu": [
                {"name": "Kebab", "price": "11€"},
                {"name": "Chicken", "price": "10€"}
            ],
            "link": "https://maps.google.com/?q=Sultan+Frankfurt"
        },
        {
            "name": "Central Grill",
            "address": "Frankfurt",
            "phone": "+49 69 555555",
            "delivery": True,
            "menu": [
                {"name": "Döner", "price": "6€"},
                {"name": "Pizza", "price": "8€"}
            ],
            "link": "https://maps.google.com/?q=Central+Frankfurt"
        }
    ]
}