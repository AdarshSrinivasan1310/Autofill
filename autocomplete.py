import tkinter as tk

# Class for Trie Node
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_leaf = False
        self.meaning = "word not found"

# Class for Trie operations
class Trie:
    def __init__(self):
        self.root = TrieNode()

    # Insert a word into the Trie
    def insert(self, word, meaning):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_leaf = True
        node.meaning = meaning

    # Search for a node that represents the word or prefix
    def search_prefix(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return None
            node = node.children[char]
        return node

    # Helper function to find all words starting from a node
    def collect_words(self, node, prefix, words):
        if node.is_leaf:
            words.append(prefix)
        for char, child_node in node.children.items():
            self.collect_words(child_node, prefix + char, words)

    # Function to find all words with a given prefix
    def find_words_with_prefix(self, prefix):
        node = self.search_prefix(prefix)
        words = []
        if node:
            self.collect_words(node, prefix, words)
        return words

# Function to update suggestions as user types
def update_suggestions(event, trie):
    typed = entry_word.get().lower()

    # Stop autocomplete if '0' is entered
    if '0' in typed:
        listbox_suggestions.delete(0, tk.END)
        return

    suggestions = trie.find_words_with_prefix(typed)
    listbox_suggestions.delete(0, tk.END)  # Clear previous suggestions

    # Display new suggestions
    for word in suggestions:
        listbox_suggestions.insert(tk.END, word)

# Function to perform search and show result
def search_word(trie):
    typed = entry_word.get().lower()
    listbox_suggestions.delete(0, tk.END)
    label_result.config(text="")  # Clear the result label

    if typed:
        node = trie.search_prefix(typed)
        if node and node.is_leaf:
            # If the word is found and is a full word, display its meaning
            label_result.config(text=f"Meaning of '{typed}': {node.meaning}")
        else:
            # If it's a prefix, show the possible words
            suggestions = trie.find_words_with_prefix(typed)
            if suggestions:
                label_result.config(text="Possible completions:")
                for word in suggestions:
                    listbox_suggestions.insert(tk.END, word)
            else:
                listbox_suggestions.insert(tk.END, "No words found with this prefix.")
    else:
        listbox_suggestions.insert(tk.END, "Please enter a prefix to search.")

# Function to insert new word and meaning
def insert_word(trie):
    word = entry_insert_word.get().lower()
    meaning = entry_meaning.get()
    if word and meaning:
        trie.insert(word, meaning)
        entry_insert_word.delete(0, tk.END)
        entry_meaning.delete(0, tk.END)

# Set up the main window
def setup_gui():
    root = tk.Tk()
    root.title("Trie Autocomplete and Word Meaning")
    root.geometry("600x400")

    trie = Trie()

    # Insert default words into the Trie
    default_words = {
    "apple": "a fruit",
    "ant": "a small insect",
    "angle": "the space between two intersecting lines",
    "apron": "a protective garment worn over the front of one's clothes",
    "arrow": "a weapon with a straight thin shaft and a pointed head",
    "actor": "a person who performs in plays or movies",
    "alarm": "a signal, typically a loud sound, warning of danger",
    "anchor": "a device used to hold a vessel in place",
    "artist": "a person who creates art",
    "animal": "a living organism that feeds on organic matter",
    "boat": "a small vessel for traveling on water",
    "bat": "a flying mammal",
    "ball": "a round object used in games",
    "bread": "a food made of flour, water, and yeast or another leavening agent",
    "bank": "a financial institution that accepts deposits",
    "bark": "the outer covering of the trunk of a tree",
    "blue": "the color of the sky or sea on a clear day",
    "bird": "a warm-blooded egg-laying vertebrate animal",
    "branch": "a part of a tree which grows out from the trunk",
    "butter": "a pale yellow edible fatty substance made from cream",
    "box": "a container with a flat base and sides",
    "cat": "a small domesticated carnivorous mammal",
    "car": "a road vehicle, typically with four wheels",
    "cup": "a small bowl-shaped container for drinking",
    "cake": "a sweet baked dessert made from flour, sugar, and other ingredients",
    "cap": "a kind of soft, flat hat without a brim",
    "card": "a piece of thick, stiff paper or thin pasteboard",
    "camera": "a device for recording visual images",
    "candle": "a cylinder or block of wax with a central wick",
    "cloud": "a visible mass of condensed water vapor in the sky",
    "coat": "an outer garment worn outdoors",
    "coin": "a flat, typically round piece of metal used as money",
    "chair": "a seat for one person with a support for the back",
    "dog": "a domesticated carnivorous mammal",
    "door": "a hinged or sliding barrier",
    "dust": "fine, dry particles of matter",
    "duck": "a waterbird with a broad blunt bill, short legs, and webbed feet",
    "doctor": "a qualified practitioner of medicine",
    "desk": "a piece of furniture with a flat top for writing or using a computer",
    "diamond": "a precious stone consisting of a clear and colorless crystalline form of pure carbon",
    "doll": "a small model of a human figure",
    "drum": "a percussion instrument sounded by being struck",
    "dress": "a one-piece garment for a woman or girl",
    "egg": "an oval or round object laid by a female bird, reptile, fish, or invertebrate",
    "earth": "the planet on which we live",
    "ear": "the organ of hearing",
    "engine": "a machine with moving parts that converts power into motion",
    "eye": "the organ of sight",
    "elbow": "the joint between the forearm and the upper arm",
    "eagle": "a large bird of prey",
    "echo": "a sound or sounds caused by the reflection of sound waves",
    "fan": "a device with rotating blades that creates a current of air",
    "fire": "combustion or burning",
    "fish": "a limbless cold-blooded vertebrate animal with gills and fins",
    "fog": "a thick cloud of tiny water droplets suspended in the atmosphere",
    "flag": "a piece of cloth with a distinctive design",
    "frog": "a tailless amphibian with a short squat body",
    "fruit": "the sweet and fleshy product of a tree or other plant",
    "finger": "each of the four slender jointed parts attached to either hand",
    "feather": "any of the flat appendages growing from a bird's skin",
    "forest": "a large area covered chiefly with trees and undergrowth",
    "friend": "a person whom one knows and with whom one has a bond of mutual affection",
    "flower": "the seed-bearing part of a plant",
    "fork": "a tool with two or more prongs used for eating or serving food",
    "fox": "a carnivorous mammal of the dog family",
    "foot": "the lower extremity of the leg below the ankle",
    "flute": "a wind instrument made from a tube with holes along it",
    "farm": "an area of land used for growing crops and raising animals",
    "fence": "a barrier intended to prevent escape or intrusion",
    "field": "an area of open land",
    "fairy": "a mythical being of folklore and romance",
    "firefly": "a nocturnal beetle that produces a bright light",
    "feast": "a large meal, typically one in celebration",
    "frame": "a rigid structure that surrounds something",
    "forest": "a large area covered chiefly with trees and undergrowth",
    "fridge": "a large container for keeping food and drinks cool",
    "flash": "a sudden brief burst of bright light",
    "feather": "one of the light, flat appendages growing from a bird's skin",
    "flame": "the visible, gaseous part of a fire",
    "family": "a group consisting of parents and children living together",
    "field": "an area of open land",
    "film": "a motion picture",
    "fan": "an apparatus with rotating blades that creates a current of air"
}


    for word, meaning in default_words.items():
        trie.insert(word, meaning)

    # Frame for inserting words
    frame_insert = tk.Frame(root)
    frame_insert.pack(pady=10)

    tk.Label(frame_insert, text="Insert a new word and meaning").grid(row=0, column=0, columnspan=2)

    tk.Label(frame_insert, text="Word:").grid(row=1, column=0, sticky=tk.W)
    global entry_insert_word
    entry_insert_word = tk.Entry(frame_insert, width=30)
    entry_insert_word.grid(row=1, column=1)

    tk.Label(frame_insert, text="Meaning:").grid(row=2, column=0, sticky=tk.W)
    global entry_meaning
    entry_meaning = tk.Entry(frame_insert, width=30)
    entry_meaning.grid(row=2, column=1)

    btn_insert = tk.Button(frame_insert, text="Insert Word", command=lambda: insert_word(trie))
    btn_insert.grid(row=3, column=0, columnspan=2, pady=10)

    # Frame for searching words
    frame_search = tk.Frame(root)
    frame_search.pack(pady=20)

    tk.Label(frame_search, text="Start typing for suggestions or search meaning").grid(row=0, column=0, columnspan=2)

    tk.Label(frame_search, text="Word Prefix:").grid(row=1, column=0, sticky=tk.W)
    global entry_word
    entry_word = tk.Entry(frame_search, width=30)
    entry_word.grid(row=1, column=1)

    # Listbox to display suggestions
    global listbox_suggestions
    listbox_suggestions = tk.Listbox(frame_search, width=40, height=10)
    listbox_suggestions.grid(row=3, column=0, columnspan=2, pady=10)

    # Label to display the meaning of the word
    global label_result
    label_result = tk.Label(frame_search, text="", fg="blue")
    label_result.grid(row=4, column=0, columnspan=2, pady=10)

    # Button to trigger search
    btn_search = tk.Button(frame_search, text="Search", command=lambda: search_word(trie))
    btn_search.grid(row=2, column=0, columnspan=2, pady=10)

    # Bind the text entry to update suggestions on every keypress
    entry_word.bind("<KeyRelease>", lambda event: update_suggestions(event, trie))

    root.mainloop()

# Run the application
if __name__ == "__main__":
    setup_gui()
