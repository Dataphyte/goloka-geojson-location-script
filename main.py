from loaders.ghana import  GhanaLoader
from rich import print as rprint


ghana_loader = GhanaLoader()

ghana_loader.create_region_parent('source/ghana//ghana_regions.json')

ghana_loader.add_region_children('source/ghana//ghana_towns.json')

ghana_loader.generate('generated/ghana')