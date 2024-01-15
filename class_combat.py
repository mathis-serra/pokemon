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
        with open('Data/Pokemon/Type_chart.json','r',encoding='utf-8') as file:
            types_pokemon = json.load(file)
        return types_pokemon

    def charger_pokemon(self, pokemon_id):
        with open('Data/Pokemon/Pokedex.json','r',encoding='utf-8') as file:
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
    
    def vainqueur_dresseur(self, dresseur_en_face):
        if self.pokemon1['base']['HP'] <= 0:
            vainqueur = dresseur_en_face
        else:
            vainqueur = "Steve"
        return vainqueur
    
    def effectuer_tour(self):
        if self.combat_en_cours:
            print(f"\nTour {self.tour_actuel} du combat :")

            attaquants = [self.pokemon1, self.pokemon2]
            defenseurs = [self.pokemon2, self.pokemon1]

            for attaquant, defenseur in zip(attaquants, defenseurs):
                degats_infliges = self.enlever_pv(attaquant, defenseur)

                print(f"{attaquant['name']['french']} a infligé {degats_infliges} dégâts.")
                print(defenseur['name']['french'])
                print("HP:", defenseur['health'])

                if not self.combat_en_cours:
                    print(f"Le vainqueur est {self.pokemon_vainqueur()}")
                    break
                
            self.tour_actuel += 1
    
    def enregistrer_dans_pokedex(self, pokemon):
        pokemon_id = pokemon['id']
        if pokemon_id not in [p['id'] for p in self.pokedex]:
            self.pokedex.append(pokemon)
            print(f"{pokemon['name']['french']} a été ajouté à votre Pokédex !")
        else:
            print(f"{pokemon['name']['french']} est déjà dans votre Pokédex.")
        

combat_test = Combat(2, 123)

while combat_test.combat_en_cours:
    combat_test.effectuer_tour()