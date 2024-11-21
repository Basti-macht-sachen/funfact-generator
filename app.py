import random
from flask import Flask, render_template, jsonify

app = Flask(__name__)

# List of fun facts
fun_facts = [
    "Honey never spoils; archaeologists have found pots of honey in ancient tombs that are over 3,000 years old and still perfectly edible.",
    "A group of flamingos is called a 'flamboyance.'",
    "The Eiffel Tower can be 15 cm taller during the summer due to the expansion of metal in the heat.",
    "Sloths can hold their breath for up to 40 minutes underwater.",
    "Sharks existed before trees, dating back over 400 million years.",
    "A jiffy is an actual unit of time, equivalent to 1/100th of a second.",
    "Bananas are berries, but strawberries are not.",
    "The shortest war in history was between Britain and Zanzibar on August 27, 1896; it lasted only 38 minutes.",
    "Octopuses have three hearts and blue blood.",
    "Cleopatra lived closer in time to the first Moon landing than to the construction of the Great Pyramid.",
    "It’s illegal to own just one guinea pig in Switzerland because they’re considered social animals.",
    "Cows have best friends and can become stressed when they are separated.",
    "Wombat poop is cube-shaped to prevent it from rolling away.",
    "A day on Venus is longer than a year on Venus.",
    "The moon has moonquakes, similar to earthquakes on Earth.",
    "The longest hiccuping spree lasted 68 years.",
    "The unicorn is Scotland’s national animal.",
    "A shrimp’s heart is in its head.",
    "More people are allergic to cow’s milk than any other food.",
    "Pineapples were once so rare and expensive that they were rented out as centerpieces at parties.",
    "The first computer virus was created in 1983.",
    "Lobsters communicate with each other by peeing on one another.",
    "The longest word in the English language is 189,819 letters long and is the chemical name for the protein known as Titin.",
    "Giraffes have the same number of neck vertebrae as humans: seven.",
    "An octopus can change both the color and texture of its skin to blend into its surroundings.",
    "The largest snowflake on record was 15 inches wide and 8 inches thick.",
    "There’s a species of jellyfish known as Turritopsis dohrnii that is considered biologically immortal.",
    "The average person walks the equivalent of three times around the world in a lifetime.",
    "A bolt of lightning contains enough energy to cook 100,000 slices of toast.",
    "You can’t hum while holding your nose.",
    "In Japan, there is a museum dedicated to rocks that look like faces.",
    "A crocodile can’t stick its tongue out.",
    "The human nose can detect over 1 trillion different scents.",
    "You can’t snore and dream at the same time.",
    "Some turtles can breathe through their butts.",
    "Elephants are the only animals that can’t jump.",
    "A single cloud can weigh more than a million pounds.",
    "Pineapples were named after pinecones by early European explorers.",
    "There are more stars in the universe than grains of sand on all of Earth’s beaches.",
    "A cow can produce up to 6 gallons of milk per day.",
    "Bamboo can grow up to 35 inches in a single day.",
    "A snail can sleep for three years without eating.",
    "Your body has more bacteria cells than human cells.",
    "The world's smallest mammal is the bumblebee bat, which weighs less than a penny.",
    "Penguins propose to their mates with a pebble.",
    "A single teaspoon of honey represents the life work of 12 bees.",
    "The average person spends about two weeks of their life waiting for red lights to turn green.",
    "A blue whale’s tongue alone can weigh as much as an elephant.",
    "Shakespeare invented over 1,700 words.",
    "In South Korea, there is a special day in the year dedicated to celebrating love for potatoes.",
    '"A giraffe’s neck is too short to reach the ground, so it has to spread its legs apart to drink water."',
    '"A cloud can weigh more than 1 million pounds."',
    '"The longest hiccuping spree lasted 68 years."',
    '"A baby octopus is the size of a pencil eraser when born."',
    '"An ostrich\'s eye is bigger than its brain."',
    '"The shortest commercial flight in the world is in Scotland, lasting just 57 seconds."',
    '"A shrimp’s heart is located in its head."',
    '"The first alarm clock could only ring at 4 a.m."',
    '"The inventor of the Pringles can is buried in one."',
    '"A jiffy is an actual unit of time—1/100th of a second."',
    '"The longest time between two twins being born is 87 days."',
    '"Some cats are allergic to humans."',
    '"There are more plastic flamingos in the U.S. than real ones."',
    '"The Earth’s inner core is as hot as the sun’s surface."',
    '"Humans share 60% of their DNA with bananas."',
    '"You can’t hum while holding your nose."',
    '"The only letter that doesn’t appear in any U.S. state name is Q."',
    '"A narwhal’s tusk reveals its age."',
    '"The Eiffel Tower can be 15 cm taller during the summer."',
    '"A small child could swim through the veins of a blue whale."',
    '"The tallest snowman ever built was over 122 feet tall."',
    '"Sloths can hold their breath for up to 40 minutes underwater."',
    '"Sea otters hold hands while they sleep to avoid drifting apart."',
    '"Koalas sleep for up to 22 hours a day."',
    '"In ancient Rome, it was considered a sign of wealth to have a pet flamingo."',
    '"The world’s largest snowflake was 15 inches wide."',
    '"A mole can dig a tunnel 300 feet long in a single night."',
    '"Cows have best friends and can become stressed when separated from them."',
    '"Polar bear skin is black, but their fur is white."',
    '"Apples float because 25% of their volume is air."',
    '"A sneeze can travel at up to 100 miles per hour."',
    '"A blue whale’s tongue weighs as much as an elephant."',
    '"The average person spends two weeks of their life waiting for red lights."',
    '"A dog’s sense of smell is 40 times better than a human’s."',
    '"There’s enough DNA in the human body to stretch from the sun to Pluto and back—17 times."',
    '"Sharks existed before trees, over 400 million years ago."',
    '"A baby kangaroo is the size of a lima bean when born."',
    '"The largest living organism on Earth is a fungus in Oregon, covering over 2,385 acres."',
    '"Bananas are berries, but strawberries are not."',
    '"The longest word in the dictionary is "pneumonoultramicroscopicsilicovolcanoconiosis."',
    '"A crocodile can’t stick its tongue out."',
    '"The moon has quakes, similar to earthquakes on Earth."',
    '"Some turtles can breathe through their butts."',
    '"The word "nerd" was first coined by Dr. Seuss in 1950."',
    '"The inventor of the lightbulb, Thomas Edison, was afraid of the dark."',
    '"A sneeze can release up to 40,000 droplets."',
    '"Penguins mate for life and propose with pebbles."',
    '"The first computer virus was created in 1983."',
    '"You can’t cry in space because your tears won’t fall."',
    '"A day on Venus is longer than a year on Venus."'
]

@app.route('/')
def index():
    # Select a random fun fact
    fact = random.choice(fun_facts)
    return render_template('index.html', fact=fact)

@app.route('/api/fact')
def api_fact():
    # Select a random fun fact and return as JSON
    fact = random.choice(fun_facts)
    return jsonify({'fact': fact})

if __name__ == '__main__':
    app.run(debug=True)
