import random

def seperate(x):
    list = []
    word = ''
    for i in x:
        if i == ' ' or i == ',' or i == '.':
            list.append(word)
            word = ''
        else:
            word += i
    list.append(word)
    return list

def combine(x):
    end = ''
    for i in x:
        end += i
        end += ' '
    return end


def translator(s):
    s = seperate(s)
    like_emojis = ['💙', '❤️', '👍', '😍', '😀', '🤩']
    like_words = ['like', 'love', 'adore', 'nice', 'noice', 'fire', 'loving', 'loved', 'loves', 'liked', 'likes', 'linking', 'adores', 'adoring', 'adorred']
    for i in like_words:
        for n in range(len(s)):
            if s[n].upper() == i.upper():
                s[n] = random.choice(like_emojis)

    dog = ['🐶', '🐕', '🐕‍🦺']
    dog_words = ['dogs', 'dog', 'corgi']
    for i in dog_words:
        for n in range(len(s)):
            if s[n].upper() == i.upper():
                s[n] = random.choice(dog)

    ball = ['🏀', '⚽', '🏈']
    ball_words = ['balls', 'ball', 'soccer', 'football', 'sport']
    for i in ball_words:
        for n in range(len(s)):
            if s[n].upper() == i.upper():
                s[n] = random.choice(ball)

    hate_emojis = ['😡', '🤬', '🥵', '🤢', '🤮', '👹', '👎 ']
    hate_words = ['hate', 'dislike', 'dispise', 'hated', 'hates', 'hating', 'dislikes', 'disliked', 'disliking', 'dispises', 'dispised', 'dispising']
    for i in hate_words:
        for n in range(len(s)):
            if s[n].upper() == i.upper():
                s[n] = random.choice(hate_emojis)
    cat_emojis = ['🐱', '🐈', '🐈‍⬛', '😸', '😻', '😺', '🐾']
    cat_words = ['cat', 'cats', 'feline', 'lion', 'tiger', 'panther']
    for i in cat_words:
        for n in range(len(s)):
            if s[n].upper() == i.upper():
                s[n] = random.choice(cat_emojis)
    
    man_emojis = ['👨']
    man_words = ['man', 'men', 'person', 'people', 'human', 'I', 'you', 'me', 'my', 'your']
    for i in man_words:
        for n in range(len(s)):
            if s[n].upper() == i.upper():
                s[n] = random.choice(man_emojis)
    
    woman_emojis = ['👩']
    woman_words = ['woman', 'women', 'girl', 'girls', 'miss']
    for i in woman_words:
        for n in range(len(s)):
            if s[n].upper() == i.upper():
                s[n] = random.choice(woman_emojis)

    
    corn_emojis = ['🌽']
    corn_words = ['corn']
    for i in corn_words:
        for n in range(len(s)):
            if s[n].upper() == i.upper():
                s[n] = random.choice(corn_emojis)

    cornball_emojis = ['🌽🏀']
    cornball_words = ['cornball']
    for i in cornball_words:
        for n in range(len(s)):
            if s[n].upper() == i.upper():
                s[n] = random.choice(cornball_emojis)
    
    old_emojis = ['👴']
    old_words = ['old', 'olds', 'oldhead']
    for i in old_words:
        for n in range(len(s)):
            if s[n].upper() == i.upper():
                s[n] = random.choice(old_emojis)
    
    our_emojis = ['👯‍♂️', '👬', '👭']
    our_words = ['our', 'they', 'them', 'we', 'us']
    for i in our_words:
        for n in range(len(s)):
            if s[n].upper() == i.upper():
                s[n] = random.choice(our_emojis)

    animal_emojis = ['🐹', '🐻', '🐻‍❄️', '🦁', '🦊', '🐢']
    animal_words = ['animal', 'animals', 'creature']
    for i in animal_words:
        for n in range(len(s)):
            if s[n].upper() == i.upper():
                s[n] = random.choice(animal_emojis)
    
    laughing_emojis = ['😂', '🤣', '😅', '😹', '💀', '💀😭🙏', '😭']
    laughing_words = ['laughing', 'laugh', 'lol', 'lmao', 'laughed', 'laughs']
    for i in laughing_words:
        for n in range(len(s)):
            if s[n].upper() == i.upper():
                s[n] = random.choice(laughing_emojis)
    
    usa_emojis = ['🦅🦅']
    usa_words = ['usa', 'america', 'trump', 'patriot', 'patriotic', 'united states']
    for i in usa_words:
        for n in range(len(s)):
            if s[n].upper() == i.upper():
                s[n] = random.choice(usa_emojis)

    negative_emojis = ['👎']
    negative_words = ['negative', 'not', 'no', 'cannot', "can't", "didn't", "false"]
    for i in negative_words:
        for n in range(len(s)):
            if s[n].upper() == i.upper():
                s[n] = random.choice(negative_emojis)
    return combine(s)

    




