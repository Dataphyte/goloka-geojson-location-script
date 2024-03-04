from loaders.ghana import  GhanaLoader
from loaders.congo import CongoLoader
from loaders.mozambique import MozambiqueLoader 
from rich import print as rprint

from rich.pretty import pprint


################################
# Ghana Loader
################################


# ghana_loader = GhanaLoader()

# ghana_loader.create_region_parent('source/ghana/ghana_regions.json')

# ghana_loader.add_region_children('source/ghana/ghana_towns.json')

# ghana_loader.generate('generated/ghana')



################################
# Congo Loader
################################

# congo_loader  = CongoLoader(file_path='source/congo/congo_level_1.json')

# files = congo_loader.check_keys_from_file()

# congo_loader.create_regions(files)

# congo_loader.create_sub_regions('source/congo/congo_level_2.json')

# congo_loader.generate('generated/congo')



################################
# Mozambique Loader
################################

moz_loader = MozambiqueLoader()

moz_loader.create_regions(file_path='source/mozambique/mozambiqu_level_1.json')

moz_loader.create_sub_regions(file_path='source/mozambique/mozambique_level_2.json')

moz_loader.generate(output_dir='generated/mozambique')