import random
from datetime import datetime, timedelta

from recipe import Recipe, RecipeType
from book import Book

nbr = 0


def create_recipe(recipe_type: str | None = None) -> Recipe:
    global nbr
    nbr += 1

    total_ingredients = nbr % 5 + 3
    return Recipe(
        name=f"Recipe {nbr}",
        level=random.randint(1, 5),
        time=random.randint(15, 60),
        ingredients=[f"ingredient {i}" for i in range(total_ingredients)],
        description=f"Description {nbr}" if nbr % 2 else "",
        recipe_type=recipe_type or random.choice(Recipe.types),
    )


if __name__ == "__main__":
    r1 = create_recipe()
    print(r1)

    print()
    r2 = create_recipe()
    print(r2)

    created_at = datetime.now() - timedelta(days=100)
    book = Book(
        name="Cook book",
        last_update=created_at + timedelta(days=25),
        creation_date=created_at,
        recipes_list={
            RecipeType.STARTER: [
                create_recipe(RecipeType.STARTER) for _ in range(7)
            ],
            RecipeType.LUNCH: [
                create_recipe(RecipeType.LUNCH) for _ in range(10)
            ],
            RecipeType.DESSERT: [
                create_recipe(RecipeType.DESSERT) for _ in range(3)
            ],
        },
    )

    assert book.get_recipe_by_name(r1.name) is None

    assert len(book.get_recipes_by_types(RecipeType.STARTER)) == 7
    assert len(book.get_recipes_by_types(RecipeType.LUNCH)) == 10
    assert len(book.get_recipes_by_types(RecipeType.DESSERT)) == 3

    print(book.creation_date)
    print(book.last_update)
    size = len(book.get_recipes_by_types(r1.recipe_type))
    book.add_recipe(r1)
    print()
    assert book.get_recipe_by_name(r1.name) == r1
    assert len(book.get_recipes_by_types(r1.recipe_type)) == size + 1
    print(book.last_update)
