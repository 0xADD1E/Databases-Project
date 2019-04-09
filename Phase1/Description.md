# Description
**Platforms**
>The Platforms entity serves to convey which Nintendo platform the Pok�mon game appeared on. This Entity's only attribute is the name of the platform.

**Games**
>The Games entity describes the publication of the game. This entity's attributes are the title of the game, its initial release date, and the platform for which the game was initially developed.

**Pok�monApperance**
>The Pok�monAppearance entity contains the data belonging to the Pok�mon appearing in a certain game. Each game can contain different Pok�mon, and Pok�mon can appear in more than one game. This entity�s attributes are the Pok�mon�s ID, base health points, base speed, base attack, base defense, base special attack, base special defense, its name, and finally the game in which it appears.  

**Pok�monCanLearn**
>The Pok�monCanLearn entity coveys which abilities, at a certain level, a Pok�mon is capable of learning. This Entity�s attributes are the Pok�mon�s required level, the appearance, and the attack�s name.

**Attacks**
>The Attacks entity describes the attack abilities which Pok�mon can use. This entity�s attributes are the name of the attack, the priority which decides who attacks first, the accuracy or likelihood of it hitting, the TM number which is its id when on a technical machine in the game, the PP or power points which is the cost to use the attack, and its power which is the damage the attack can do.

**AttackTypes**
>The AttackTypes entity contains the details of what Pok�mon type an attack is considered. This entity�s attributes are the name of the attack, and the attack�s type.

**Types**
>The Types entity describes the name of a type. Currently in Pok�mon there are normal, fighting, flying, poison, ground, rock, bug, ghost, steel, fire, water, grass, electric, psychic, ice, dragon, dark, and fairy types. These types describe what are considered to be �*elemental*� properties.

**TypeMatchups**
>The TypeMatchups entity describes which types are strong against, or are weaker to other types. This entity�s attributes are the effectiveness multiplier given to an attack when there is a type advantage, the self-attribute which indicates if the damage is against the player�s Pok�mon, and the Other attribute which indicates if the damage is against the opponent.

**Pok�mon**
>The Pok�mon entity details an individual Pok�mon�s characteristics. This entity�s attributes are the Pok�mon�s ID, its name, the gender of the Pok�mon, if it is shiny, and whether it is considered to be of a legendary variety.

**Pok�monEvolutions**
>The Pok�monEvolutions entity contains the evolution information for a Pok�mon. This entity�s attributes are the base evolution which is the Pok�mon�s current form, and it�s evolution which is the form it can become.

**Media**
>The Media entity details the?????? 

**MIMETypes**
>The MIMETypes entity contains the????