# Schemas
- Platforms(__Name__:TEXT)
- Games(__GameName__:TEXT, _PlatformName_:TEXT, ReleaseDate:DATE)
- PokemonAppearance(__ID__:INTEGER, _GameName_:TEXT, _PokedexID_:INTEGER, BaseHP:INTEGER, BaseSpeed:INTEGER, BaseAttack:INTEGER, BaseDefence:INTEGER, BaseSpAttack:INTEGER, BaseSpDefence:INTEGER)
- Pokemon(__PokedexID__:INTEGER, Name:TEXT, GenderDistribution:INTEGER, Legendary:BOOLEAN)
- Media(__ID__:INTEGER, _PokedexID_:INTEGER, _MIMEString_:TEXT, Filename:TEXT, Data:BLOB)
- MIMETypes(__MIMEString__:TEXT, FriendlyName:TEXT, Extension:TEXT)
- Types(__Name__:TEXT)
- Attacks(__Name__:TEXT, Priority:INTEGER, Accuracy:INTEGER, TMNumber:INTEGER?, PP:INTEGER, Power:INTEGER)

## Relationship-Only Tables
- AttackTypes(_AttackName_:TEXT, _TypeName_:TEXT)
- PokemonEvolutions(_PokemonBaseID_:INTEGER, _PokemonEvolutionID_:INTEGER)
- TypesMatchups(_SelfName_:TEXT, _OtherName_:TEXT , EffectivenessMultiplier:INTEGER)
- PokemonCanLearn(_PokemonID_:INTEGER, _AttackName_:TEXT, AtLevel:INTEGER)
