import json 
from rich import print as rprint 
from rich.progress import track 
from rich.pretty import pprint

class CongoLoader(): 
    def __init__(self, file_path: str) -> None:
        self.regions = []
        self.file_path = file_path
        
    def check_keys_from_file(self):
        with open(self.file_path, 'r') as file :
            # read
            file = json.load(file)
            return file['features']
        
                
    def create_regions(self, file):
        
        for entry in file:
            self.regions.append({
                'name': entry['properties']['NAME_1'],
                'parent': {
                    'type': entry['geometry']['type'],
                    'coordinates': entry['geometry']['coordinates']
                },
                'children': []
            })
            
        return self.regions
    
    
    def create_sub_regions(self, file_path: str):
        with open(file_path, 'r') as file:
            file = json.load(file)
            
            for sub_region in file['features']:
                for region in self.regions:
                    if region['name'] == sub_region['properties']['NAME_1']:
                        region['children'].append({
                            'name': sub_region['properties']['NAME_2'],
                            'type': sub_region['geometry']['type'],
                            'coordinates': sub_region['geometry']['coordinates']
                        })
                        
        return self.regions
                
                
            
    def generate(self, output_dir):
        for region in self.regions:
            with open('{}/{}.json'.format(output_dir, region['name']), 'w') as file:
                
                file.write(json.dumps({
                    'parent': region['parent'], 
                    'children': region['children']
                }))
                
                file.close()
            
        
        