def year(x):
    """
    <integer> -> void
    
    >>> year returns the element and the animal signs by recogonizing the last
        digit
        
    >>> year(1920)
        metal
        strong and hard, but will adapt and change when put under pressure
        good: courageous, ambitious, and competitive
        bad: lacks communication skills
        animal
        monkey
        monkey_personality: clever, witty, always the life of the party
        monkey_professions: the media, advertising, and design
     """
    diff = int(x) - 1912
    year_index = diff % 12
    animals = ['Rat', 'Ox', 'Tiger', 'Rabbit', 'Dragon', 'Snake', 'Horse', 'Goat', 'Monkey', 'Rooster', 'Dog', 'Pig']
    animal = animals[year_index]


    rat_personality = "sharp wits and even sharper tongues"
    rat_profession = "real estate, public relations, and advertising"

    ox_personality = "strong, conservative, is born to lead"
    ox_profession = "military careers or other careers where leadership is required"

    tiger_personality = "courageous and noble soul,but also highly sensitive and quick to take offence"
    tiger_profession = "a career where they can be boss, or strike out on their own with no one to give them orders"

    rabbit_personality = "elegant, peace-loving, the soul of tact"
    rabbit_profession = "law, acting, or diplomacy"

    dragon_personality = "talented, artistic, influential"
    dragon_profession = "performing or creative arts, or politics"

    snake_personality = "enticing, alluring and highly intelligent"
    snake_profession = "academic or scientific careers"

    horse_personality = "hard working, confident, elegant, and strong"
    horse_profession = "sports, the military and politics"

    goat_personality = "very agile and loves to climb, but tends to worry a lot"
    goat_profession = "caring professions, where they can worry for profit"

    monkey_personality = "clever, witty, always the life of the party"
    monkey_profession = "the media, advertising, and design"

    rooster_personality = "a shrewd, sharp, confident operator, who dreams big and looks to the stars"
    rooster_profession = "careers where they can show off: the entertainment industry or a business"

    dog_personality = "faithful, takes setbacks philosophically, and finds comfort in familiar, homely things"
    dog_profession = "caring for others: teaching or nursing"

    pig_personality = "honorable and scrupulous, but naive"
    pig_profession = "the arts"

    personalities = [rat_personality, ox_personality, tiger_personality, rabbit_personality,
                     dragon_personality, snake_personality, horse_personality, goat_personality,
                     monkey_personality, rooster_personality, dog_personality, pig_personality ]
    professions = [rat_profession, ox_profession, tiger_profession, rabbit_profession, dragon_profession,
                   snake_profession, horse_profession, goat_profession, monkey_profession, rooster_profession,
                   dog_profession, "the arts"]


    personality = personalities[year_index]
    profession = professions[year_index]



    elements = ['metal','metal','water','water', 'wood','wood','fire','fire','earth','earth']

    metal = ['strong and hard, but will adapt and change when put under pressure',
             'good: courageous, ambitious, and competitive',
             'bad: lacks communication skills']

    water = ['flexible yet strong, flowing yet still, calm yet dangerous',
             'good: diplomatic, observant, empathetic',
             'bad: self-indulgent']

    wood = ['generous and expansive and cares deeply for others',
            'good: patient, understanding, and sociable',
            'bad: no boundaries or limits']

    fire = ['persistent and strong, but also spreads and wanders easily',
            'good: passionate and enthusiastic',
            'bad: attention seeker, impatient, and manipulative',
            ]

    earth = ['stabilizing and mediating, a natural born peace-keeper',
             'good: serious, practical, and logical',
             'bad: overprotective and conservative']

    element_list = [metal, metal, water,water, wood,wood, fire, fire,earth,earth]

    last_digit = int(str(x)[-1])

    our_element = elements[last_digit]
    
    our_element_list = element_list[last_digit]

    print (our_element)
    
    print(our_element_list[0])
    print(our_element_list[1])
    print(our_element_list[2])


    print(animal)
    print(personality)
    print(profession)
    

x = input("what is the year you born: ")
year(x)
    
    
