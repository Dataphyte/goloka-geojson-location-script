import json
from rich import print as rprint
from rich.progress import track


class GhanaLoader():
    def __init__(self) -> None:
        self.regions = []
        
    def create_region_parent(self, region_file_path):
        
        with open(region_file_path, 'r' ) as file:
            file = json.load(file)
            # rprint(file['features'][0])
            for feature in file['features']:
               rprint(feature['properties'])
               self.regions.append({
                   'region_name': feature['properties']['region'], 
                   'data': {
                       'parent':  feature['geometry'],
                        
                       'children': []
                   }
               })
               
               
    
    def add_region_children(self, town_file_path):
        with open(town_file_path, 'r') as file:
            file = json.load(file)
            
            # rprint(file['features'][0])
            
            for region in self.regions:
                for feature in file['features']:
                    if feature['properties']['NAME_1'] == region['region_name']:
                        region['data']['children'].append({
                            'name': feature['properties']['NAME_2'],
                            'type': feature['geometry']['type'],
                            'coordinates': feature['geometry']['coordinates'],
                        })
                        
    def generate(self,export_path):
        for region in self.regions:
            with open('{}/{}.json'.format(export_path, region['region_name']), 'w') as file:
                
                 file.write(json.dumps(region['data']))
                 file.close