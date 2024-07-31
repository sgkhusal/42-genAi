from datetime import datetime

from recipe import Recipe, RecipeType

# sys.path.append(os.path.dirname(os.path.abspath(__file__)))


class Book():
    def __init__(
        self,
        name: str,
        last_update: datetime,
        creation_date: datetime,
        recipes_list: dict[str, list[Recipe]]
    ) -> None:
        if not name:
            raise ValueError("missing name")
        self._name = name

        self._last_update = last_update
        self._creation_date = creation_date

        self._recipes_list = {
            RecipeType.STARTER: [],
            RecipeType.LUNCH: [],
            RecipeType.DESSERT: [],
        }
        for k in recipes_list.keys():
            if k not in Recipe.types:
                raise ValueError(f"Invalid recipe type {k} on receipes list")
        self._recipes_list.update(recipes_list)

    @property
    def name(self) -> str:
        return self._name

    @property
    def last_update(self) -> str:
        return self._last_update

    @last_update.setter
    def last_update(self, last_update: str):
        self._last_update = last_update

    @property
    def creation_date(self) -> str:
        return self._creation_date

    @property
    def recipes_list(self) -> dict:
        return self._recipes_list

    def get_recipe_by_name(self, name: str) -> Recipe | None:
        for recipes in self.recipes_list.values():
            for recipe in recipes:
                recipe: Recipe
                if recipe.name == name:
                    print(recipe)
                    return recipe

        return None

    def get_recipes_by_types(self, recipe_type: str) -> list[Recipe]:
        return self.recipes_list[recipe_type]

    def add_recipe(self, recipe: Recipe) -> None:
        if not self.recipes_list.get(recipe.recipe_type):
            self.recipes_list[recipe.recipe_type] = []
        self.recipes_list[recipe.recipe_type].append(recipe)
        self.last_update = datetime.now()
