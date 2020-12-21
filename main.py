import pprint

with open('input.txt', 'r') as input_data:
	input_data = input_data.read()

allergens_set = set(['shellfish', 'soy', 'peanuts', 'nuts', 'sesame', 'eggs', 'fish', 'wheat'])
ingrediants_set = set([])
def_not_allergen = set([])

ingrediant_count = {}

allergens_dictionary = {
	'shellfish': {'seen': False, 'ingrediants': []},
	'soy': {'seen': False, 'ingrediants': []},
	'peanuts': {'seen': False, 'ingrediants': []},
	'nuts': {'seen': False, 'ingrediants': []},
	'sesame': {'seen': False, 'ingrediants': []},
	'eggs': {'seen': False, 'ingrediants': []},
	'fish': {'seen': False, 'ingrediants': []},
	'wheat': {'seen': False, 'ingrediants': []},
	'dairy': {'seen': False, 'ingrediants': []}
}

for food in input_data.replace(',', '').replace(')', '').split('\n'):
	ingrediants, allergens = food.split(' (contains ')
	ingrediants = ingrediants.split(' ')
	ingrediants_set.update(ingrediants)
    
	for i in ingrediants:
		if i not in ingrediant_count:
			ingrediant_count[i] = 0
		ingrediant_count[i] += 1

	for allergens in allergens.split(' '):
		if allergens_dictionary[allergens]['seen']:
			new_list_of_possible_allergen = []
			for possible_allergen in allergens_dictionary[allergens]['ingrediants']:
				if possible_allergen in ingrediants:
					new_list_of_possible_allergen.append(possible_allergen)
			allergens_dictionary[allergens]['ingrediants'] = new_list_of_possible_allergen
		else:
			allergens_dictionary[allergens]['ingrediants'] = ingrediants
			allergens_dictionary[allergens]['seen'] = True
	
possible_allergen_set = set([])

for allergen in allergens_dictionary:
	possible_allergen_set.update(allergens_dictionary[allergen]['ingrediants'])

def_not_allergen = ingrediants_set - possible_allergen_set
print(def_not_allergen)
pprint.pprint(allergens_dictionary)


running_count = 0
for not_allergen in def_not_allergen:
	running_count += ingrediant_count[not_allergen]

print(running_count)

"""

I hand solved  the second half 

first figured out which ingrediant correlates with which allergen (this was mostly trial and error + me testing things in my head)

{'dairy': {'ingrediants': [], 'seen': False},
 'eggs': {'ingrediants': ['hkflr', 'srxphcm', 'bd'], 'seen': True},
 'fish': {'ingrediants': ['ctmcqjf', 'hkflr', 'mqvk', 'zvx'], 'seen': True},
 'nuts': {'ingrediants': ['bfrq'], 'seen': True},
 'peanuts': {'ingrediants': ['srxphcm', 'bfrq'], 'seen': True},
 'sesame': {'ingrediants': ['snmxl', 'zvx', 'mqvk'], 'seen': True},
 'shellfish': {'ingrediants': ['zvx', 'mqvk', 'srxphcm'], 'seen': True},
 'soy': {'ingrediants': ['srxphcm', 'snmxl', 'bd'], 'seen': True},
 'wheat': {'ingrediants': ['srxphcm', 'mqvk'], 'seen': True}}

 'eggs' ['hkflr', 'srxphcm', 'bd']
 'fish' ['ctmcqjf', 'hkflr', 'mqvk', 'zvx']
 'nuts' ['bfrq']
 'peanuts' ['srxphcm', 'bfrq']
 'sesame' ['snmxl', 'zvx', 'mqvk']
 'shellfish' ['zvx', 'mqvk', 'srxphcm']
 'soy' ['srxphcm', 'snmxl', 'bd']
 'wheat' ['srxphcm', 'mqvk']

 'eggs' 'hkflr'
 'fish' 'ctmcqjf'
 'nuts' 'bfrq'
 'peanuts' 'srxphcm'
 'sesame' 'snmxl'
 'shellfish' 'zvx', 
 'soy'  'bd'
 'wheat'  'mqvk'

hkflr,ctmcqjf,bfrq,srxphcm,snmxl,zvx,bd,mqvk
 
"""