import json
from rich.progress import track
from rich import print as rprint 


class NigeriaLoader():
    def __init__(self, lga_file_path, state_file_path):
        lga_file_path = lga_file_path
        state_file_path = state_file_path
    
    def loadStates(self): 
        # create initial lists for entities
        states = []

        ### states data ###
        with open('source/states.json.txt', 'r') as file:
            # read
            states_data = json.load(file)
            
            # loop through the states 
            rprint('Adding parent states to object...')
            for state_item in track(states_data['features'], description='Loading states'):
                # append each state as a property to the states list
                states.append({
                    'state_name': state_item['properties']['NAME_1'].lower(),
                    'parent': {
                        **state_item['geometry']
                    },
                    'children': []
                })
            rprint('Added parents to states object ✅\n\n')



        '''
        returns an object with the schema 

        {
            'state_name' : string,
            'parent' : {
                'type': string,
                'coordiantes': array of coordinates ([[[lat, long], ...]], ...)
            },
            'children': []
        }[...]
        '''



        ### lga data ###
        with open('source/lga.json.txt', 'r') as file:
            # read
            lga_data = json.load(file)
            
            # loop through state list
            for state in states:
                # loop though each lga for each state
                rprint('Adding LGAs for {}...'.format(state['state_name'].upper()))
                for lga in lga_data['features']:
                    # push lga data if state matches with lga state name
                    if lga['properties']['NAME_1'].lower() == state['state_name']:
                        state['children'].append({
                            'name': lga['properties']['NAME_2'],
                            'type': 'MultiPolygon',
                            'coordinates': lga['geometry']['coordinates']
                        })
                        rprint('--> {}'.format(lga['properties']['NAME_2']))
                
                rprint('{} state done ✅✅✅\n\n'.format(state['state_name'].upper()))
                



        '''
        returns an object with the schema

        {
            'state_name': string,
            'pareant': {
                'type': string,
                'coordiantes': array of coordinates ([[[lat, long], ...]], ...)
            }
            'children': {
                'type': string,
                'name': string,
                'coordiantes': array of coordinates ([[[lat, long], ...]])
            }
        }[...]
        '''

        ### write each state data to file ###
        rprint('[bold underlined cyan]Writing objects to location files...')
        for state_object in track(states, description='writing files'):
            with open('generated/{file}.json'.format(file = state_object['state_name']), 'w') as file:
                # extract state data in proper schema
                file_data = {
                    'parent': state['parent'],
                    'children': state['children']
                }
                
                # write to file
                file.write(json.dumps(file_data))
                rprint('[cyan]Created file [white]{}'.format(state_object['state_name']))
                
                # close file
                file.close()
                

        rprint('[bold green]ALL PROCESSES COMPLETE. FILES CREATED!! ✅')
        
        return states
            
            


                