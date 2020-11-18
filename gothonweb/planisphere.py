import sys

class Room(object):

    def __init__(self, name, description, timer=0):
        self.name = name
        self.description = description
        self.paths = {}
        self.timer = timer
    def go(self, direction):
        return self.paths.get(direction, None)

    def add_paths(self, paths):
        self.paths.update(paths)


central_corridor = Room("Central Corridor",
"""
You wake up in a dark dusty room. You try to figure out where
you are ,as the blare before your eyes is starting wearing off you
realize that you are in a corridor. You recall that an allien attack
took place and the space ship is pretty much unusable. Before you
stands a Gothon. The Gothon looks confused, he propably thouhgt that
you were dead. He grabs his axe, ready to attack you.
""")


laser_weapon_armory = Room("Laser Weapon Armory",
f"""
You do a dive roll into the Weapon Armory, crouch and scan
the room for more Gothons that might be hiding. It's dead
quiet, too quiet. You stand up and run to the far side of
the room and find the neutron bomb in its container.
There's a keypad lock on the box and you need the code to
get the bomb out. If you get the code wrong 10 times then
the lock closes forever and you can't get the bomb. The
code is 4 digits.
""")

the_bridge = Room("The Bridge",
"""
You burst onto the Bridge with the netron destruct bomb
under your arm and surprise 5 Gothons who are trying to
take control of the ship. They haven't pull their guns out yet.
""")

escape_pod = Room("Escape Pod",
"""
You rush through the ship desperately trying to make
it to the escape pod before the whole ship explodes.
You get to the chamber with the
escape pods, and now need to pick one to take. Some of
them could be damaged but you don't have time to look.
There's 5 pods '1', '2', '3', '4', '5'.
""")

the_end_winner = Room("The End",
"""
You jump into pod 2 and hit the eject button. The pod easily slides out
into space heading to the planet below.  As it flies to the planet, you look
back and you see your ship implode then explode like a bright star, taking out
the Gothon ship at the same time. You won!
""")

the_end_loser = Room("The End",
"""
You jumo into a random pod and hi the eject button. The pod escapes out
into the void of space, then implodes as the hull ruptures, crushing your body
into jam jelly.
""")


generic_death = Room("Death",
"""
You died.
""")

escape_pod.add_paths({
        '2': the_end_winner,
        '*': the_end_loser
})

the_bridge.add_paths({
        'throw_the_bomb': generic_death,
        'slowly_place_the_bomb': escape_pod
})

laser_weapon_armory.add_paths({
        '0123': the_bridge,
        '*': generic_death
})

central_corridor.add_paths({
        'shoot!': generic_death,
        'dodge!': generic_death,
        'tell_a_joke': laser_weapon_armory
})

START = 'central_corridor'


def load_room(name):
    # The globals() function returns a dictionary containing the variables
    # defined in the global namespace. When globals() is called from a
    # function or method, it returns the dictionary representing the global
    # namespace of the module where the function or method is defined,
    # not from where it is called.
    return globals().get(name)

def name_room(room):

    for key, value in globals().items():
        if value == room:
            return key
