from src.buildings.faci import BaseFaci
from src.registry.registry import Registry

facilities = Registry[BaseFaci]("vanilla")

AEROSTAT_PLATFORM = facilities.register(BaseFaci("aerostat_platform", "faci.vanilla.aerostat_platform", "faci.vanilla.aerostat_platform.description", "temperature", 2, -40, 0, 0, 0, 0, 0, 3000, 0))
ALGAE_COLONY = facilities.register(BaseFaci("algae_colony", "faci.vanilla.algae_colony", "faci.vanilla.algae_colony.description", "biomass", 1, 0, 0, 0, -4, 8, 0, 0, 0))
AQUIFER_NETWORK = facilities.register(BaseFaci("aquifer_network", "faci.vanilla.aquifer_network", "faci.vanilla.aquifer_network.description", "water", 2, 0, 10, 0, 40, 0, 0, 0, 0))
ATMOGEN_SUITE = facilities.register(BaseFaci("atmogen_suite", "faci.vanilla.atmogen_suite", "faci.vanilla.atmogen_suite.description", "pressure", 2, 0, 60, 10, 0, 0, 0, 0, 0))
BIOFIXTURE_LAB = facilities.register(BaseFaci("biofixture_lab", "faci.vanilla.biofixture_lab", "faci.vanilla.biofixture_lab.description", "pressure", 2, 0, -40, 0, 0, 10, 0, 0, 0))
BOREHOLE = facilities.register(BaseFaci("borehole", "faci.vanilla.borehole", "faci.vanilla.borehole.description", "temperature", 2, 60, 10, 0, 0, 0, 0, 0, 0))
CARBON_FIXER = facilities.register(BaseFaci("carbon_fixer", "faci.vanilla.carbon_fixer", "faci.vanilla.carbon_fixer.description", "oxygen", 2, 0, 10, -40, 0, 0, 0, 0, 0))
CHILDREN_S_CRECHE = facilities.register(BaseFaci("children_s_creche", "faci.vanilla.children_s_creche", "faci.vanilla.children_s_creche.description", "population", 1, 0, 0, 0, 0, 0, 10, 0, 0))
CLOUD_SEEDER = facilities.register(BaseFaci("cloud_seeder", "faci.vanilla.cloud_seeder", "faci.vanilla.cloud_seeder.description", "water", 1, 0, 0, 0, 4, 0, 0, 0, 0))
COMET_SLING = facilities.register(BaseFaci("comet_sling", "faci.vanilla.comet_sling", "faci.vanilla.comet_sling.description", "water", 3, 0, 0, 0, 120, -10, 0, 8000, 0))
COOLING_PLANT = facilities.register(BaseFaci("cooling_plant", "faci.vanilla.cooling_plant", "faci.vanilla.cooling_plant.description", "temperature", 1, -4, 0, 0, 0, 0, 0, 0, 0))
CORAL_REEF = facilities.register(BaseFaci("coral_reef", "faci.vanilla.coral_reef", "faci.vanilla.coral_reef.description", "biomass", 3, 0, 0, 0, 0, 120, 20, 4000, 0))
CYANOVATS = facilities.register(BaseFaci("cyanovats", "faci.vanilla.cyanovats", "faci.vanilla.cyanovats.description", "oxygen", 2, 0, 0, 60, -10, 0, 0, 0, 0))
ELECTROLYSIS_PLANT = facilities.register(BaseFaci("electrolysis_plant", "faci.vanilla.electrolysis_plant", "faci.vanilla.electrolysis_plant.description", "water", 2, 0, 0, 10, -40, 0, 0, 0, 0))
FOREST_STAND = facilities.register(BaseFaci("forest_stand", "faci.vanilla.forest_stand", "faci.vanilla.forest_stand.description", "biomass", 3, 0, 0, 20, -20, 100, 0, 0, 0))
GEOCISTERN = facilities.register(BaseFaci("geocistern", "faci.vanilla.geocistern", "faci.vanilla.geocistern.description", "water", 1, 0, 0, 0, -4, 0, 0, 0, 0))
GRASS_FARM = facilities.register(BaseFaci("grass_farm", "faci.vanilla.grass_farm", "faci.vanilla.grass_farm.description", "biomass", 2, 0, 0, 0, -10, 40, 0, 0, 0))
HABITATION_COMPLEX = facilities.register(BaseFaci("habitation_complex", "faci.vanilla.habitation_complex", "faci.vanilla.habitation_complex.description", "population", 2, 0, 0, 10, 0, 0, 0, 0, 2500))
HABITATION_DOME = facilities.register(BaseFaci("habitation_dome", "faci.vanilla.habitation_dome", "faci.vanilla.habitation_dome.description", "population", 3, 0, 0, 0, 20, 10, 0, 0, 50000))
HABITATION_UNIT = facilities.register(BaseFaci("habitation_unit", "faci.vanilla.habitation_unit", "faci.vanilla.habitation_unit.description", "population", 1, 0, 0, 0, 0, 0, 0, 0, 100))
HEATING_CLUSTER = facilities.register(BaseFaci("heating_cluster", "faci.vanilla.heating_cluster", "faci.vanilla.heating_cluster.description", "temperature", 1, 4, 0, 0, 0, 0, 0, 0, 0))
HYDROGEN_PROCESSOR = facilities.register(BaseFaci("hydrogen_processor", "faci.vanilla.hydrogen_processor", "faci.vanilla.hydrogen_processor.description", "pressure", 3, 10, -100, 0, 20, 0, 0, 0, 0))
HYDRO_GENERATOR = facilities.register(BaseFaci("hydro_generator", "faci.vanilla.hydro_generator", "faci.vanilla.hydro_generator.description", "oxygen", 3, 0, 0, -80, 20, 0, 0, 0, 0))
ICE_LAUNCHER = facilities.register(BaseFaci("ice_launcher", "faci.vanilla.ice_launcher", "faci.vanilla.ice_launcher.description", "water", 3, 0, -10, 0, -120, 0, 0, 3000, 0))
KELP_FARM = facilities.register(BaseFaci("kelp_farm", "faci.vanilla.kelp_farm", "faci.vanilla.kelp_farm.description", "oxygen", 3, 0, -10, 120, 0, 20, 0, 0, 0))
KELP_FOREST = facilities.register(BaseFaci("kelp_forest", "faci.vanilla.kelp_forest", "faci.vanilla.kelp_forest.description", "biomass", 2, 0, 0, 30, 0, 80, 0, 0, 0))
ORBITAL_MIRROR = facilities.register(BaseFaci("orbital_mirror", "faci.vanilla.orbital_mirror", "faci.vanilla.orbital_mirror.description", "temperature", 3, 120, 0, 0, -10, -20, 0, 0, 0))
OXYGEN_FILTER = facilities.register(BaseFaci("oxygen_filter", "faci.vanilla.oxygen_filter", "faci.vanilla.oxygen_filter.description", "oxygen", 1, 0, 0, -4, 0, 0, 0, 0, 0))
OXYGEN_PLANT = facilities.register(BaseFaci("oxygen_plant", "faci.vanilla.oxygen_plant", "faci.vanilla.oxygen_plant.description", "oxygen", 1, 0, 0, 4, 0, 0, 0, 0, 0))
POCKET_MINE = facilities.register(BaseFaci("pocket_mine", "faci.vanilla.pocket_mine", "faci.vanilla.pocket_mine.description", "pressure", 3, 0, 100, 20, 0, 0, 0, 2000, 0))
SEQUESTRATION_PLANT = facilities.register(BaseFaci("sequestration_plant", "faci.vanilla.sequestration_plant", "faci.vanilla.sequestration_plant.description", "pressure", 1, 0, -4, 0, 0, 0, 0, 0, 0))
SOIL_FARM = facilities.register(BaseFaci("soil_farm", "faci.vanilla.soil_farm", "faci.vanilla.soil_farm.description", "biomass", 1, 0, 0, 0, 0, 4, 0, 0, 0))
SOLAR_SHADE = facilities.register(BaseFaci("solar_shade", "faci.vanilla.solar_shade", "faci.vanilla.solar_shade.description", "temperature", 3, -100, 0, 0, 0, -20, 0, -5000, 0))
SPACEPORT = facilities.register(BaseFaci("spaceport", "faci.vanilla.spaceport", "faci.vanilla.spaceport.description", "population", 3, 0, 10, 0, 0, -10, 120, 10000, 0))
THERMAL_DUST = facilities.register(BaseFaci("thermal_dust", "faci.vanilla.thermal_dust", "faci.vanilla.thermal_dust.description", "pressure", 1, 0, 4, 0, 0, 0, 0, 0, 0))
TRANSIT_NETWORK = facilities.register(BaseFaci("transit_network", "faci.vanilla.transit_network", "faci.vanilla.transit_network.description", "population", 2, 0, 0, 0, 0, -10, 80, 0, 0))
