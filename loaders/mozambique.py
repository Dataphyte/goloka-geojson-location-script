import json
from rich import print as rprint 
from rich.pretty import pprint 

class MozambiqueLoader():
    def __init__(self, ) -> None:
        self.regions = []
        
    def create_regions(self, file_path: str): 
        with open(file_path, 'r') as region_file:
            file = json.load(region_file)
            
            for region in file['features']:
                self.regions.append({
                    'name': region['properties']['NAME_1'],
                    'parent': {
                        'type': region['geometry']['type'],
                        'coordinates': region['geometry']['coordinates']
                    },
                    'children': []
                })
        return self.regions
    
    def create_sub_regions(self, file_path:str):
        with open(file_path, 'r') as sub_regions:
            file = json.load(sub_regions)
            
            
            for sub_region in file['features']:
                for region in self.regions:
                    if sub_region['properties']['NAME_1'] ==  region['name']:
                        region['children'].append({
                            'name': sub_region['properties']['NAME_2'],
                            'type': sub_region['geometry']['type'],
                            'coordinates': sub_region['geometry']['coordinates']
                        })
                        
            return self.regions
        
        
    def generate(self, output_dir: str):
        for region in self.regions:
            with open('{}/{}.json'.format(output_dir, region['name']), 'w') as file:
                
                file.write(json.dumps({
                    'parent': region['parent'],
                    'children': region['children']
                }))
                
                file.close()