from loaders.ghana import  GhanaLoader
from loaders.congo import CongoLoader
from rich import print as rprint

from rich.pretty import pprint


# ghana_loader = GhanaLoader()

# ghana_loader.create_region_parent('source/ghana/ghana_regions.json')

# ghana_loader.add_region_children('source/ghana/ghana_towns.json')

# ghana_loader.generate('generated/ghana')

congo_loader  = CongoLoader(file_path='source/congo/congo_level_1.json')

files = congo_loader.check_keys_from_file()

congo_loader.create_regions(files)

congo_loader.create_sub_regions('source/congo/congo_level_2.json')

congo_loader.generate('generated/congo')