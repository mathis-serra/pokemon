import json
import random

class Combat:
    def __init__(self,pokemon1_id,pokemon2_id):
        self.pokemon1 = self.charger_pokemon(pokemon1_id)
        self.pokemon2 = self.charger_pokemon(pokemon2_id)
        self.types_pokemon = self.charger_types_pokemon()
        self.tour_actuel = 1
        self.combat_en_cours = True
        self.vainqueur = None
        self.pokedex = []
        self.pokemon1['health'] = self.pokemon1['base']['HP']
        self.pokemon2['health'] = self.pokemon2['base']['HP']
        self.lvl=1

    def charger_types_pokemon(self):
        with open('Data/Type_chart.json','r',encoding='utf-8') as file:
            types_pokemon = json.load(file)
        return types_pokemon

    def charger_pokemon(self, pokemon_id):
        with open('Data/Pokedex.json','r',encoding='utf-8') as file:
            pokedex = json.load(file)
        for pokemon in pokedex:
            if pokemon['id'] == pokemon_id:
                return pokemon
            
    def calcul_degats(self,attaquant,defenseur):
        type_attaque = attaquant['type'][0]
        type_defenseur = defenseur['type'][0]
        types_pokemon = self.types_pokemon
        multiplicateur_type=types_pokemon[type_attaque.lower()][type_defenseur.lower()]
        attaque_pokemon=attaquant['base']['Attack']
        defense=defenseur['base']['Defense']   
        efficacite_type=multiplicateur_type 
        cm=efficacite_type*random.uniform(0.85, 1)

        pv_perdus = ((((((self.lvl*0.4+2)*attaque_pokemon*100)/defense)/50)+2)*cm)
        pv_perdus = max(1, round(pv_perdus))
        
        return pv_perdus
    
    def enlever_pv(self, attaquant, defenseur):
        if self.combat_en_cours:
            degats = self.calcul_degats(attaquant, defenseur)
            pv_actuels = defenseur['health']
            
            defenseur['health'] = max(0, pv_actuels - degats)

            if defenseur['health'] <= 0:
                self.combat_en_cours = False
                defenseur['health'] = 0

            return degats

    def pokemon_vainqueur(self):
        if self.pokemon1['health'] <= 0:
            self.vainqueur=self.pokemon2['name']['french']
        else:
            self.vainqueur=self.pokemon1['name']['french']

        return self.vainqueur
    
    def combat_fini(self):
        return self.pokemon1['health'] <= 0 or self.pokemon2['health'] <= 0
    
    def vainqueur_dresseur(self, dresseur_en_face):
        if self.pokemon1['base']['HP'] <= 0:
            vainqueur = dresseur_en_face
        else:
            vainqueur = "Steve"
        return vainqueur
    
    def enregistrer_dans_pokedex(self, pokemon):
        pokemon_id = pokemon['id']
        if pokemon_id not in [p['id'] for p in self.pokedex]:
            self.pokedex.append(pokemon)
        