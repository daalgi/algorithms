"""
https://leetcode.com/problems/find-all-possible-recipes-from-given-supplies/

You have information about n different recipes. You are 
given a string array recipes and a 2D string array 
ingredients. The ith recipe has the name recipes[i], and 
you can create it if you have all the needed ingredients 
from ingredients[i]. Ingredients to a recipe may need to 
be created from other recipes, i.e., ingredients[i] may 
contain a string that is in recipes.

You are also given a string array supplies containing 
all the ingredients that you initially have, and you 
have an infinite supply of all of them.

Return a list of all the recipes that you can create. 
You may return the answer in any order.

Note that two recipes may contain each other in their 
ingredients.

Example 1:
Input: recipes = ["bread"], 
ingredients = [["yeast","flour"]], 
supplies = ["yeast","flour","corn"]
Output: ["bread"]
Explanation:
We can create "bread" since we have the ingredients 
"yeast" and "flour".

Example 2:
Input: recipes = ["bread","sandwich"], 
ingredients = [["yeast","flour"],["bread","meat"]], 
supplies = ["yeast","flour","meat"]
Output: ["bread","sandwich"]
Explanation:
We can create "bread" since we have the ingredients 
"yeast" and "flour".
We can create "sandwich" since we have the ingredient 
"meat" and can create the ingredient "bread".

Example 3:
Input: recipes = ["bread","sandwich","burger"], 
ingredients = [["yeast","flour"],["bread","meat"],
["sandwich","meat","bread"]], 
supplies = ["yeast","flour","meat"]
Output: ["bread","sandwich","burger"]
Explanation:
We can create "bread" since we have the ingredients 
"yeast" and "flour".
We can create "sandwich" since we have the ingredient 
"meat" and can create the ingredient "bread".
We can create "burger" since we have the ingredient 
"meat" and can create the ingredients "bread" and "sandwich".

Constraints:
n == recipes.length == ingredients.length
1 <= n <= 100
1 <= ingredients[i].length, supplies.length <= 100
1 <= recipes[i].length, ingredients[i][j].length, supplies[k].length <= 10
recipes[i], ingredients[i][j], and supplies[k] consist 
only of lowercase English letters.
All the values of recipes and supplies combined are unique.
Each ingredients[i] does not contain any duplicate values.
"""
from copy import deepcopy
from typing import List
from collections import defaultdict, deque


def dfs_recursion(
    recipes: List[str], ingredients: List[List[str]], supplies: List[str]
) -> List[str]:
    # Time complexity: O(n)
    # Space complexity: O(n)

    def dfs(recipe: str) -> bool:
        # Depth First Search recursive function

        if recipe not in can_make:
            # If the current `recipe` is not yet in the hashmap
            # `can_make`, find out if all its ingredients can
            # be found.
            # First, initialize the current `recipe` in the
            # hashmap as can't make it (False) to avoid an
            # infinite loop due to a cycle
            can_make[recipe] = False
            # Loop over all the ingredients
            can_make[recipe] = all([dfs(ingr) for ingr in graph[recipe]])

        # The current `recipe` has already been stored in the hashmap,
        # so return it
        return can_make[recipe]

    # Convert `supplies` into a hashset for O(1) lookups
    supplies = set(supplies)

    # Hashmap to track whether a recipe or ingredient can be made
    # or found in the `supplies`, i.e.
    # { "bread": True, "meat": False }
    can_make = {}

    # Build a adjacency list `graph`
    # {"ingredient1": ["subingredient1", "subingredient1", ...], ...}
    graph = {r: [] for r in recipes}
    n = len(recipes)
    # Loop over the `recipes`
    for i in range(n):
        # Loop over the `ingredients` of the current recipe
        for ingr in ingredients[i]:
            if ingr not in supplies:
                # If the current ingredient `ingr` is not in `supplies`,
                # it may be a composed ingredient (that depends on other
                # basic ingredients), so add it to the graph
                # to check later on if it can be made
                graph[recipes[i]].append(ingr if ingr in graph else recipes[i])

    # Return a list of the recipees that can be made
    # using the recursive function `dfs`
    return [recipe for recipe in recipes if dfs(recipe)]


def bfs_iter(
    recipes: List[str], ingredients: List[List[str]], supplies: List[str]
) -> List[str]:
    # Time complexity: O(n)
    # Space complexity: O(n)

    # Solution with a graph mapping recipe -> ingredients
    n = len(recipes)

    supplies = set(supplies)

    # Build an adjacency list:
    # ingredient: [sub_ingredient1, sub_ingredient2, ...]
    adj = defaultdict(list)
    for i in range(n):
        for ingredient in ingredients[i]:
            adj[recipes[i]].append(ingredient)

    can_make = {ing: True for ing in supplies}

    for recipe in recipes:

        if recipe in can_make:
            continue

        q = deque([recipe])
        contains_all = True
        current_ingredients = set()
        while q:

            # Current ingredient
            ingredient = q.popleft()

            # Ingredient already seen previously
            if ingredient in can_make:
                if can_make[ingredient]:
                    continue
                contains_all = False
                break

            if ingredient in current_ingredients:
                contains_all = False
                break
            current_ingredients.add(ingredient)

            # Check if `ingredient` is made of other ingredients
            # or a basic ingredient in `supplies`
            if ingredient not in adj and ingredient not in supplies:
                # If not, the current `ingredient` can't be found
                # so the current `recipe` can't be made
                can_make[ingredient] = False
                contains_all = False
                break

            for subing in adj[ingredient]:
                q.append(subing)

        can_make[recipe] = contains_all

    return [r for r in recipes if can_make[r]]


def topological_sort(
    recipes: List[str], ingredients: List[List[str]], supplies: List[str]
) -> List[str]:
    # Time complexity: O(n)
    # Space complexity: O(n)

    n = len(recipes)

    # Convert `supplies` into a hashset for O(1) lookups
    supplies = set(supplies)

    # Build a adjacency list `graph` and an `indegree` counter
    # mapping the ingredients not in `supplies`, or `subrecipes`,
    # to the corresponding `recipes`.
    # By definition, the ingredients that are
    # in `supplies` make the current recipe directly valid,
    # so we only need to build a graph with the ingredients
    # that are a composition of other ingredients and check
    # if those "intermediate" recipes `subrecipe` can be made.
    # {"subrecipe": ["recipe1", "recipe2", ...], ...}
    # {"recipe1": 2, ...}
    graph, indegree = defaultdict(list), defaultdict(int)
    for i in range(n):
        for ingredient in ingredients[i]:
            if ingredient not in supplies:
                graph[ingredient].append(recipes[i])
                indegree[recipes[i]] += 1

    # Valid recipes list
    res = []

    # BFS with a queue initialized with the `recipes`
    # with no coming-in edges (indegree = 0), that is,
    # the recipes whose ingredients are all in `supplies`
    q = deque([recipe for recipe in recipes if indegree[recipe] == 0])
    while q:
        recipe = q.pop()

        # Add the current `recipe`, with has indegree = 0,
        # which means that all its ingredients or subrecipes
        # can be found, to the result list
        res.append(recipe)

        # If the current `recipe`
        for suprarecipe in graph[recipe]:
            indegree[suprarecipe] -= 1
            # Check if all the ingredients to make the current
            # `suprarecipe` have been found, that is, indegree = 0
            if not indegree[suprarecipe]:
                # Add it to the queue, to be explored later on
                q.append(suprarecipe)

    return res


if __name__ == "__main__":
    print("-" * 60)
    print("Find all possible recipes from given supplies")
    print("-" * 60)

    test_cases = [
        # ( recipes, ingredients, supplies, solution )
        (
            ["bread"],
            [["yeast", "flour"]],
            ["yeast", "flour", "corn"],
            ["bread"],
        ),
        (
            ["bread", "sandwich"],
            [["yeast", "flour"], ["bread", "meat"]],
            ["yeast", "flour", "meat"],
            ["bread", "sandwich"],
        ),
        (
            ["bread", "sandwich", "burger"],
            [["yeast", "flour"], ["bread", "meat"], ["sandwich", "meat", "bread"]],
            ["yeast", "flour", "meat"],
            ["bread", "sandwich", "burger"],
        ),
        (
            ["bread", "sandwich", "burger"],
            [["yeast", "flour"], ["bread", "meat"], ["sandwich", "meat", "bread"]],
            ["yeast", "flour", "garlic"],
            ["bread"],
        ),
        (
            ["r1", "r2"],
            [["i1", "i2", "i3"], ["i2", "i3", "i12"]],
            ["i10", "i3", "i11"],
            [],
        ),
        (
            ["ju", "fzjnm", "x", "e", "zpmcz", "h", "q"],
            [
                ["d"],
                ["hveml", "f", "cpivl"],
                ["cpivl", "zpmcz", "h", "e", "fzjnm", "ju"],
                ["cpivl", "hveml", "zpmcz", "ju", "h"],
                ["h", "fzjnm", "e", "q", "x"],
                ["d", "hveml", "cpivl", "q", "zpmcz", "ju", "e", "x"],
                ["f", "hveml", "cpivl"],
            ],
            ["f", "hveml", "cpivl", "d"],
            ["ju", "fzjnm", "q"],
        ),
        (
            [
                "xevvq",
                "izcad",
                "p",
                "we",
                "bxgnm",
                "vpio",
                "i",
                "hjvu",
                "igi",
                "anp",
                "tokfq",
                "z",
                "kwdmb",
                "g",
                "qb",
                "q",
                "b",
                "hthy",
            ],
            [
                ["wbjr"],
                ["otr", "fzr", "g"],
                ["fzr", "wi", "otr", "xgp", "wbjr", "igi", "b"],
                [
                    "fzr",
                    "xgp",
                    "wi",
                    "otr",
                    "tokfq",
                    "izcad",
                    "igi",
                    "xevvq",
                    "i",
                    "anp",
                ],
                ["wi", "xgp", "wbjr"],
                ["wbjr", "bxgnm", "i", "b", "hjvu", "izcad", "igi", "z", "g"],
                ["xgp", "otr", "wbjr"],
                ["wbjr", "otr"],
                ["wbjr", "otr", "fzr", "wi", "xgp", "hjvu", "tokfq", "z", "kwdmb"],
                ["xgp", "wi", "wbjr", "bxgnm", "izcad", "p", "xevvq"],
                ["bxgnm"],
                ["wi", "fzr", "otr", "wbjr"],
                ["wbjr", "wi", "fzr", "xgp", "otr", "g", "b", "p"],
                ["otr", "fzr", "xgp", "wbjr"],
                ["xgp", "wbjr", "q", "vpio", "tokfq", "we"],
                ["wbjr", "wi", "xgp", "we"],
                ["wbjr"],
                ["wi"],
            ],
            ["wi", "otr", "wbjr", "fzr", "xgp"],
            ["xevvq", "izcad", "bxgnm", "i", "hjvu", "tokfq", "z", "g", "b", "hthy"],
        ),
    ]

    def print_list(name: str, l: List[str]):
        output = str(l)
        if len(output) > 55:
            output = output[:50] + " ...]"
        print(f"{name}:", output)

    for recipes, ingredients, supplies, solution in test_cases:

        print_list(name="Recipes", l=recipes)
        print_list(name="Ingredients", l=ingredients)
        print_list(name="Supplies", l=supplies)

        result = dfs_recursion(
            deepcopy(recipes),
            deepcopy(ingredients),
            deepcopy(supplies),
        )
        output = f"      dfs_recursion = "
        result_str = str(result)
        if len(result_str) > 35:
            result_str = result_str[:30] + "...]"
        output += result_str
        output += " " * (60 - len(output))
        test_ok = sorted(solution) == sorted(result)
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        result = bfs_iter(
            deepcopy(recipes),
            deepcopy(ingredients),
            deepcopy(supplies),
        )
        output = f"           bfs_iter = "
        result_str = str(result)
        if len(result_str) > 35:
            result_str = result_str[:30] + "...]"
        output += result_str
        output += " " * (60 - len(output))
        test_ok = sorted(solution) == sorted(result)
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        result = topological_sort(
            deepcopy(recipes),
            deepcopy(ingredients),
            deepcopy(supplies),
        )
        output = f"   topological_sort = "
        result_str = str(result)
        if len(result_str) > 35:
            result_str = result_str[:30] + "...]"
        output += result_str
        output += " " * (60 - len(output))
        test_ok = sorted(solution) == sorted(result)
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        print("\n")
