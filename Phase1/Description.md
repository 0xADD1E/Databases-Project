# Description
**Platforms**
>*The Platforms entity serves to convey which Nintendo platform the Pokémon game appeared on.*
- This Entity's only attribute is the name of the platform.

**Games**
>*The Games entity describes the publication of the game.* 
- The Name attribute is the title of the game
- The ReleaseDate attribute is the game's initial release date
- The Platform attribute refers to the platform for which the game was initially developed.

**PokemonApperance**
>*The PokemonAppearance entity contains the data belonging to the Pokémon appearing in a certain game. Each game can contain different Pokémon, and Pokémon can appear in more than one game.*
- The ID attribute is the Pokémon's designated number
- The BaseHp attribute is the base health points stat the Pokémon begins with
- The BaseSpeed attribute is the Pokémon's initial speed stat
- The BaseAttack attribute is the Pokémon's initial attack stat
- The BaseDefence attribute is the Pokémon's initial defense stat
- The BaseSpAttack attribute is the Pokémon's initial special attack stat
- The BaseSpDefence attribute is the Pokémon's initial special defense stat
- The Pokemon attribute is a package containing Pokemon, it is the many end of the relation
- The Game attribute is a package containing Game, it is the many end of the relation
 
**PokemonCanLearn**
>*The PokemonCanLearn entity coveys which abilities, at a certain level, a Pokémon is capable of learning.*
- The AtLevel attribute states the level at which an attack can be learned
- The Appearance attribute is a package containing PokemonAppearance, it is the many end of the relation
- The Attack attribute is a package containing Attacks, it is the many end of the relation

**Attacks**
>*The Attacks entity describes the attack abilities which Pokémon can use.*
- The Name attribute is the name of the attack
- The Priority attribute value decides who attacks first
- The Accuracy attribute is the likelihood of it hitting the opponent
- The TMNumber attribute is an attack's id when on a technical machine in the game
- The PP attribute refers to power points, which are the cost to use the attack
- The Power attribute is the damage the attack can do.

**AttackTypes**
>*The AttackTypes entity contains the details of what Pokémon type an attack is considered.*
- The Attack attribute is a package containing Attacks, it is the many end of the relation
- The Type attribute is a package containing Types, it is the many end of the relation

**Types**
>*The Types entity contains the name of the type. Currently in Pokémon there are normal, fighting, flying, poison, ground, rock, bug, ghost, steel, fire, water, grass, electric, psychic, ice, dragon, dark, and fairy types. These types describe what are considered to be “elemental” properties.*
- The only attribute is Name which states the name of the type

**TypeMatchups**
>*The TypeMatchups entity describes which types are strong against, or are weaker to other types. This entity’s attributes are the effectiveness multiplier given to an attack when there is a type advantage, the self-attribute which indicates if the damage is against the player’s Pokémon, and the Other attribute which indicates if the damage is against the opponent.*
- The EffectivenessMultiplier attribute contains the value that the effectiveness is modified by
- The self attribute contains whether the advantage is with or against the player
- The Other attribute contains whether the advantage is with or against the opponent

**Pokémon**
>*The Pokémon entity details an individual Pokémon’s characteristics.*
- The PokedexID attribute is the Pokémon’s ID given by the in game Pokédex tool
- The Name attribute is the Pokémon's name
- The GenderDistribution is the gender of the Pokémon
- The Legendary attribute states whether the Pokémon is considered to be of a legendary variety

**PokemonEvolutions**
>*The PokemonEvolutions entity contains the evolution information for a Pokémon.* 
- The Base attribute is the Pokémon’s current form
- The Evolution attribute is the form the Pokémon can become.

## Could we remove Media and MIMETypes if we aren't going to use them?
**Media**
>*The Media entity details the media in which a Pokémon is featured.*
- The IntegerId attribute contains the Pokémon Id the media is about
- The FileName attribute contains the name of the file in which the media is stored
- The BLOBdata attribute is the media data stored in the database
- The Pokémon attribute is a package containing Pokemon, it is the many end of the relation
- The MIMEType attribute is a package containing MIMETypes, it is the many end of the relation

**MIMETypes**
>*The MIMETypes entity contains the Multipurpose Internet Mail Extension for the database which indicates the format of documents, files, or assorted bytes.*
- The MIMEString attribute 
- The FriendlyName attribute
- The Extension attribute
