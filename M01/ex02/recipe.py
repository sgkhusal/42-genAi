from enum import Enum


class RecipeType(str, Enum):
    STARTER = "starter"
    LUNCH = "lunch"
    DESSERT = "dessert"


class Recipe:
    levels = range(1, 6)
    types = [RecipeType.STARTER, RecipeType.LUNCH, RecipeType.DESSERT]

    def __init__(
        self,
        name: str,
        level: int,
        time: int,
        ingredients: list[str],
        description: str,
        recipe_type: str,
    ) -> None:
        if not name:
            raise ValueError("missing name")
        self._name = name

        if level not in self.levels:
            raise ValueError(f"{level} is not a valid cooking level")
        self._cooking_lvl = level

        if time < 0:
            raise ValueError("invalid time value")
        self._cooking_time = time

        if not ingredients:
            raise ValueError("Missing recipe ingredients")
        self._ingredients = ingredients
        self._description = description

        if recipe_type not in self.types:
            raise ValueError(f"{recipe_type} is not a valid recipe type")
        self._recipe_type = recipe_type

    @property
    def name(self) -> str:
        return self._name

    @property
    def cooking_lvl(self) -> int:
        return self._cooking_lvl

    @property
    def cooking_time(self) -> int:
        return self._cooking_time

    @property
    def ingredients(self) -> list[str]:
        return self._ingredients

    @property
    def description(self) -> str:
        return self._description

    @description.setter
    def description(self, description: str):
        self._description = description

    @property
    def recipe_type(self) -> str:
        return self._recipe_type

    def __str__(self):
        description = ""
        if self.description:
            description = f"Description: {self.description}"

        ingredients = "ingredients:\n"
        for i, ingredient in enumerate(self.ingredients):
            ingredients += f"{i + 1}. {ingredient}\n"

        return (
            f"Recipe: {self.name}\n"
            f"type: {self.recipe_type}\n"
            f"level: {self.cooking_lvl}\n"
            f"duration: {self.cooking_time} min\n"
            f"{ingredients}{description}"
        )
