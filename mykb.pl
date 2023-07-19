servesAll(american_restaurants, [salad, steak, sandwiches, burgers, fried_chicken]).
servesAll(burger_place_restaurants, [burgers, fries, onion_rings]).
servesAll(chinese_restaurants, [eggrolls, rice, shrimp, soup, noodles]).
servesAll(indian_restaurants, [papadam, bagan_bharta, rice, tandoori, naan]).
servesAll(italian_restaurants, [salad, pasta, cioppino, snapper, bread, garlic_bread]).
servesAll(japanese_restaurants, [sashimi, rice, tempura, noodles]).
servesAll(mediterranean_restaurants, [gyros, hummus, pita, falafel]).
servesAll(mexican_restaurants, [tacos, beans, rice, enchiladas, fish_tacos]).
servesAll(pizza_place_restaurants, [pizza, salad, garlic_bread]).
servesAll(thai_restaurants, [rice, noodles, larb, pad_thai]).

dishesAll(vegetarian_dishes, [beans, bagan_bharta, enchiladas, falafel, hummus, pizza, salad, soup, tempura, onion_rings, naan, papadam, bread, rice, noodles, pita, garlic_bread, pasta, fries]).
dishesAll(meat_dishes, [burgers, enchiladas, gyros, pad_thai, pizza, steak, sandwiches, fried_chicken, tacos, tandoori, larb]).
dishesAll(seafood_dishes, [snapper, cioppino, sashimi, shrimp, clams, fish_tacos, tempura]).
dishesAll(starch_dishes, [naan, papadam, bread, rice, noodles, pita, garlic_bread, pasta, fries]).

locationAll(thayer_street, [yans, bajas, andreas, chinatown, kabob_n_curry, heng, mikes, east_side_pocokets, shake_shack]).
locationAll(fox_point, [pizza_marvin, bees, al_forno, dolores, tallulahs]).
locationAll(wayland, [red_stripe, pasta_beach, haruki, waterman_grille, lims]).

cuisineAll(chinese_restaurants, [yans, chinatown]).
cuisineAll(burger_place_restaurants, [shake_shack]).
cuisineAll(mexican_restaurants, [bajas, dolores, tallulahs]).
cuisineAll(mediterranean_restaurants, [andreas, east_side_pocokets]).
cuisineAll(indian_restaurants, [kabob_n_curry]).
cuisineAll(thai_restaurants, [heng, lims]).
cuisineAll(pizza_place_restaurants, [mikes, pizza_marvin]).
cuisineAll(italian_restaurants, [pasta_beach, al_forno]).
cuisineAll(japanese_restaurants, [haruki]).
cuisineAll(american_restaurants, [red_stripe, waterman_grille]).


dishes(Kind, Dish) :-
    dishesAll(Kind, Dishes) ,
    member(Dish, Dishes).

serves(Kind, Dish) :-
    servesAll(Kind, Dishes) ,
    member(Dish, Dishes).

locations(Kind, Restaurant) :-
    locationAll(Kind, Restaurants),
    member(Restaurant, Restaurants).

cuisines(Kind, Restaurant) :-
    cuisineAll(Kind, Restaurants),
    member(Restaurant, Restaurants).
    
dish_from_location(Location, Kind, Restaurant_name) :-
    locations(Location, Restaurant_name), 
    cuisines(Type_of_restaurant, Restaurant_name), 
    serves(Type_of_restaurant, Dish), 
    dishes(Kind, Dish).
    

/**Queries:

1. Which restaurants are in wayland?
    locations(wayland, X).

2. Which restaurants have italian cuisine?
    cuisines(italian_restaurants, X).

3. Which kind of restaurants serve snapper?
    serves(X, snapper).

4. Which kinds of restaurants serves rice ?
    serves(X, rice).

5. Where can you get served a vegetarian dish in fox_point?
    dish_from_location(fox_point, vegetarian_dishes).
**/


