# Animal

animals = {
    ('vertebrado', 'mamifero', 'onivoro'): 'homem',
    ('vertebrado', 'mamifero', 'herbivoro'): 'vaca',
    ('vertebrado', 'ave', 'onivoro'): 'pomba',
    ('vertebrado', 'ave', 'carnivoro'): 'aguia',
    ('invertebrado', 'inseto', 'hematofago'): 'pulga',
    ('invertebrado', 'inseto', 'herbivoro'): 'lagarta',
    ('invertebrado', 'anelideo', 'hematofago'): 'sanguessuga',
    ('invertebrado', 'anelideo', 'onivoro'): 'minhoca',
}
category1 = input()
category2 = input()
category3 = input()

print(animals[(category1, category2, category3)])
