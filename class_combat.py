import json
import random
import os

class Combat:
    def __init__(self):
        self.id_pokemon = 148
        self.id_pokemon2 = random.randint(1, 386)
        self.pokemon1_evolution()
        self.pokemon1 = self.charger_pokemon(self.id_pokemon)
        self.pokemon2 = self.charger_pokemon(self.id_pokemon2)
        self.types_pokemon = self.charger_types_pokemon()
        self.tour_actuel = 1
        self.combat_en_cours = True
        self.vainqueur = None
        self.pokemon1['health'] = self.pokemon1['base']['HP']
        self.pokemon2['health'] = self.pokemon2['base']['HP']
        self.lvl_pokemon1=self.pokemon1["level"]
        self.lvl_pokemon2=random.randint(1,10)
        self.xp_gain = 10

    def pokemon1_get(self):
        return self.id_pokemon
    
    def pokemon1_evolution(self):
        pokemon =self.charger_pokemon(148)
        pokemon2=self.charger_pokemon(2)
        if pokemon['level']== 55 and pokemon2["level"] < 10:
            new = self.id_pokemon+1
            self.id_pokemon=new
        elif pokemon["level"]==5 and pokemon2["level"]==10 :
            new = self.id_pokemon+2
            self.id_pokemon=new

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
            
    def update_pokedex_levels(self):
        with open("Data/Pokedex.json", "r+", encoding="utf8") as json_file:
            pokedex_data = json.load(json_file)
            for pokemon in pokedex_data:
                if pokemon["name"]["french"] == "Draco":
                    pokemon["level"] = 54
                if pokemon["name"]["french"] == "Dracolosse":
                    pokemon["level"] = 55

            json_file.seek(0)
            json_file.truncate()
            json.dump(pokedex_data, json_file, indent=4)
            
    def enregistrer_pokemon_vu(self, pokemon):
        pokedex_see_path = 'Data/Pokedex_see.json'

        if os.path.isfile(pokedex_see_path) and os.path.getsize(pokedex_see_path) > 0:
            with open(pokedex_see_path, 'r', encoding='utf-8') as file:
                pokedex_see = json.load(file)
        else:
            pokedex_see = []

        if pokemon['id'] not in {p['id'] for p in pokedex_see}:
            pokedex_see.append(pokemon)

            with open(pokedex_see_path, 'w', encoding='utf-8') as file:
                json.dump(pokedex_see, file, ensure_ascii=False, indent=2)

    def vider_fichier_json(self, chemin_fichier):
        with open(chemin_fichier, 'w') as file:
            file.write('')
            
    def sauvegarder_pokemon(self, pokemon):
        with open('Data/Pokedex.json', 'r', encoding='utf-8') as file:
            pokedex = json.load(file)

        for p in pokedex:
            if p['id'] == pokemon['id']:
                p['experience'] = pokemon['experience']
                p['level'] = pokemon['level']
                p['experience_to_next_level'] = pokemon['experience_to_next_level']

        with open('Data/Pokedex.json', 'w', encoding='utf-8') as file:
            json.dump(pokedex, file, ensure_ascii=False, indent=2)
            
    def calcul_degats(self,attaquant,defenseur):
        type_attaque = attaquant['type'][0]
        type_defenseur = defenseur['type'][0]
        types_pokemon = self.types_pokemon
        multiplicateur_type=types_pokemon[type_attaque.lower()][type_defenseur.lower()]
        efficacite_type=multiplicateur_type 
        cm=efficacite_type*random.uniform(0.85, 1)
        lvl_attaquant = self.lvl_pokemon1 if attaquant == self.pokemon1 else self.lvl_pokemon2

        pv_perdus = ((((((lvl_attaquant*0.4+2)*attaquant['base']['Attack']*100)/defenseur['base']['Defense'] )/50)+2)*cm)
        pv_perdus = max(1, round(pv_perdus))
        
        return pv_perdus
    
    def enlever_pv(self, attaquant, defenseur):
        if self.combat_en_cours and self.attaque_reussie(attaquant, defenseur):
            degats = self.calcul_degats(attaquant, defenseur)
            pv_actuels = defenseur['health']

            defenseur['health'] = max(0, pv_actuels - degats)

            if defenseur['health'] <= 0:
                self.combat_en_cours = False
                defenseur['health'] = 0
                
            return degats
        else:
            return 0

    def attaque_reussie(self,attaquant,defenseur):
        chance_attaque = random.uniform(0, 1)
        chance_esquive = 0.1

        if chance_attaque > chance_esquive:
            return True
        else:
            return False

    def gagner_experience(self):
        self.pokemon1['experience'] += self.xp_gain
        print(self.pokemon1['experience'])

        if self.pokemon1['experience'] >= self.pokemon1['experience_to_next_level']:
            self.monter_niveau(self.pokemon1)

        self.sauvegarder_pokemon(self.pokemon1)

    def monter_niveau(self, pokemon):
        pokemon['level'] += 1
        pokemon['experience_to_next_level'] = 20

    def pokemon_vainqueur(self):
        if self.pokemon1['health'] <= 0:
            self.vainqueur=self.pokemon2['name']['french']
        else:
            self.vainqueur=self.pokemon1['name']['french']
            self.gagner_experience()

        self.enregistrer_pokemon_vu(self.pokemon1)
        self.enregistrer_pokemon_vu(self.pokemon2)
        return self.vainqueur
    
    def combat_fini(self):
        return self.pokemon1['health'] <= 0 or self.pokemon2['health'] <= 0
    
    def vainqueur_dresseur(self, dresseur_en_face):
        if self.pokemon1['base']['HP'] <= 0:
            vainqueur = dresseur_en_face
        else:
            vainqueur = "Steve"
        return vainqueur