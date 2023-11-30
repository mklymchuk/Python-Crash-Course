#Store information about pizza being ordered.
pizzas = {
    'margherita pizza':{
        'ingredients': ['Pizza dough', 'Tomato sauce', 'Fresh mozzarella cheese',
                        'Fresh basil leaves', 'Olive oil', 'Salt and pepper'],
        'description': '''Margherita pizza is a classic Italian pizza known
                        for its simplicity and fresh flavors.
                        It typically features a thin crust topped with tomato sauce,
                        slices of fresh mozzarella cheese, and whole basil leaves.
                        Drizzled with olive oil and seasoned with salt and pepper,
                        the Margherita pizza highlights the quality of its ingredients.'''
    },
    'pepperoni pizza':{
        'ingredients': ['Pizza dough', 'Tomato sauce', 'Mozzarella cheese',
                        'Pepperoni slices', 'Olive oil', 'Dried oregano (optional)'],
        'description': '''Pepperoni pizza is a popular choice known for its savory and 
                        slightly spicy flavor. It starts with a traditional pizza crust,
                        topped with a generous layer of tomato sauce, mozzarella cheese,
                        and slices of pepperoni. After baking, the pepperoni becomes crispy around the edges,
                        adding a delicious texture to each bite. Some variations may include a sprinkle of
                        dried oregano for extra flavor.'''
    }
}
#Summarize the order.

for pizza, pizza_info in pizzas.items():
    print(f"\nYour order is: {pizza.title()}")
    
    ingredients = pizza_info['ingredients']
    print(f"Ingredients: ")
    for ingredient in ingredients:
        print(f"{ingredient}")
        
    print(f"\nDescription: {pizza_info['description']}")
