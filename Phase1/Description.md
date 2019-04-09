# Description
**Platforms**
>The Platforms entity serves to convey which Nintendo platform the Pokémon game appeared on. This Entity's only attribute is the name of the platform.

**Games**
>The Games entity describes the publication of the game. This entity's attributes are the title of the game, its initial release date, and the platform for which the game was initially developed.

**PokémonApperance**
>The PokémonAppearance entity contains the data belonging to the Pokémon appearing in a certain game. Each game can contain different Pokémon, and Pokémon can appear in more than one game. This entity’s attributes are the Pokémon’s ID, base health points, base speed, base attack, base defense, base special attack, base special defense, its name, and finally the game in which it appears.  

**PokémonCanLearn**
>The PokémonCanLearn entity coveys which abilities, at a certain level, a Pokémon is capable of learning. This Entity’s attributes are the Pokémon’s required level, the appearance, and the attack’s name.

**Attacks**
>The Attacks entity describes the attack abilities which Pokémon can use. This entity’s attributes are the name of the attack, the priority which decides who attacks first, the accuracy or likelihood of it hitting, the TM number which is its id when on a technical machine in the game, the PP or power points which is the cost to use the attack, and its power which is the damage the attack can do.

**AttackTypes**
>The AttackTypes entity contains the details of what Pokémon type an attack is considered. This entity’s attributes are the name of the attack, and the attack’s type.

**Types**
>The Types entity describes the name of a type. Currently in Pokémon there are normal, fighting, flying, poison, ground, rock, bug, ghost, steel, fire, water, grass, electric, psychic, ice, dragon, dark, and fairy types. These types describe what are considered to be “*elemental*” properties.

**TypeMatchups**
>The TypeMatchups entity describes which types are strong against, or are weaker to other types. This entity’s attributes are the effectiveness multiplier given to an attack when there is a type advantage, the self-attribute which indicates if the damage is against the player’s Pokémon, and the Other attribute which indicates if the damage is against the opponent.

**Pokémon**
>The Pokémon entity details an individual Pokémon’s characteristics. This entity’s attributes are the Pokémon’s ID, its name, the gender of the Pokémon, if it is shiny, and whether it is considered to be of a legendary variety.

**PokémonEvolutions**
>The PokémonEvolutions entity contains the evolution information for a Pokémon. This entity’s attributes are the base evolution which is the Pokémon’s current form, and it’s evolution which is the form it can become.

**Media**
>The Media entity details the?????? 

**MIMETypes**
>The MIMETypes entity contains the????