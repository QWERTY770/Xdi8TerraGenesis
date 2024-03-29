import json

from src.registry.registry import HasID


class BaseFaci(HasID):
    def __init__(self, faci_id: str, name: str, description: str, faci_type: str, faci_tier: int,
                 temp_gen, pressure_gen, oxygen_gen, water_gen, biomass_gen, pop_gen, money_gen,
                 pop_limit: int = 0):
        super().__init__(faci_id)
        self.name = name  # translation key, not real name
        self.description = description  # translation key, not real name
        self.type = faci_type
        self.tier = faci_tier
        self.temp_gen = temp_gen
        self.pressure_gen = pressure_gen
        self.oxygen_gen = oxygen_gen
        self.water_gen = water_gen
        self.biomass_gen = biomass_gen
        self.pop_gen = pop_gen
        self.money_gen = money_gen
        self.pop_limit = pop_limit  # max population in it, set to 0 for non-residential buildings
        self.namespace = "default"  # this should be set later

    @classmethod
    def from_json(cls, src: dict):
        t1 = src["data"]
        try:
            t2 = t1["pop_limit"]
            return cls(src["id"], src["name"], src["description"], src["type"], src["tire"],
                       t1["temp_gen"], t1["pressure_gen"], t1["oxygen_gen"], t1["water_gen"],
                       t1["biomass_gen"], t1["pop_gen"], t1["money_gen"], t2)
        except KeyError:
            return cls(src["id"], src["name"], src["description"], src["type"], src["tire"],
                       t1["temp_gen"], t1["pressure_gen"], t1["oxygen_gen"], t1["water_gen"],
                       t1["biomass_gen"], t1["pop_gen"], t1["money_gen"])


class Faci:
    def __init__(self, base_faci: BaseFaci, max_level: int, level: int, cost_multiplier: int = 1):
        self.base = base_faci
        self.max_level = max_level
        self.level = level
        self.cost_multiplier = cost_multiplier

    def get_maintenance_cost(self):
        return self.base.tier * self.level * 500 * self.cost_multiplier

    @property
    def temp_gen(self):
        return self.base.temp_gen * (1 + (self.level - 1) * 0.5)

    @property
    def pressure_gen(self):
        return self.base.pressure_gen * (1 + (self.level - 1) * 0.5)

    @property
    def oxygen_gen(self):
        return self.base.oxygen_gen * (1 + (self.level - 1) * 0.5)

    @property
    def water_gen(self):
        return self.base.water_gen * (1 + (self.level - 1) * 0.5)

    @property
    def biomass_gen(self):
        return self.base.biomass_gen * (1 + (self.level - 1) * 0.5)

    @property
    def pop_gen(self):
        return self.base.pop_gen * (1 + (self.level - 1) * 0.5)

    @property
    def pop_limit(self):
        return self.base.pop_limit * (1 + (self.level - 1) * 0.5)

    @property
    def money_gen(self):
        return self.base.money_gen * (1 + (self.level - 1) * 0.5)


if __name__ == "__main__":
    a = BaseFaci.from_json(json.loads(open(
        r"../../resources/data/vanilla/facilities_deprecated/heating_cluster.json").read()))
    b = Faci(a, 2, 5)
    print(b.temp_gen)
    print(b.pressure_gen)
    print(b.get_maintenance_cost())
    print(b.base.description)
