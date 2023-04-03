import random
import time
print('''
              _____    _____   _____   _____                _____     _____              _   _            
     /\      / ____|  / ____| |_   _| |_   _|       /\     |  __ \   / ____|     /\     | \ | |     /\    
    /  \    | (___   | |        | |     | |        /  \    | |__) | | |         /  \    |  \| |    /  \   
   / /\ \    \___ \  | |        | |     | |       / /\ \   |  _  /  | |        / /\ \   | . ` |   / /\ \  
  / ____ \   ____) | | |____   _| |_   _| |_     / ____ \  | | \ \  | |____   / ____ \  | |\  |  / ____ \ 
 /_/    \_\ |_____/   \_____| |_____| |_____|   /_/    \_\ |_|  \_\  \_____| /_/    \_\ |_| \_| /_/    \_\ 
                                                                                                          
                                                                                                          

''')
print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
print("Ascii Arcana is a singleplayer-game that requires a mage defeating its enemies. Have fun!")
print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
print("\n")


class mage:
    def __init__(self, healthpoints, magicka, karma, stamina):
        self.healthpoints = 100
        self.magickapoints = 100
        self.karma = 100
        self.staminapoints = 100

    def dagger_attack(self, enemy):
        if self.staminapoints >= 20:
            hit_chance = random.randint(1, 20)  # roll a 20-sided die for hit chance
            if hit_chance >= 10:  # attack hits if the roll is 10 or greater
                damage = random.randint(10, 15)  # roll another die for damage
                enemy.healthpoints -= damage
                self.staminapoints -= 20
                print("The enemy has been hit by the dagger attack for {damage} damage!".format(damage=damage))
            else:
                self.staminapoints -= 10  # reduce stamina cost if the attack misses
                print("The dagger attack missed!")
        else:
            print("Not enough stamina to perform the dagger attack.")
    
    def fireball(self, enemy):
        if self.magickapoints >= 50:
            hit_chance = random.randint(1, 20)
            if hit_chance >= 12:
                damage = random.randint(30,50)
                enemy.healthpoints -= damage
                self.magickapoints -= 50
                print("The enemy has been hit by the fireball attack for {damage} damage!".format(damage=damage))
            else:
                self.magickapoints -= 25
                print("The fireball misses its target!")
        else:
            print("Not enough magicka for this attack. You have {magicka} left.".format(magicka=self.magicka))

    def burn(self, enemy):
        total_damage = 0
        burn_time = 10 # set the burn time to 10 seconds
        burn_interval = 2 # set the burn interval to 2 seconds
        damage_per_second = 5 # set the damage per second to 5
        for i in range(burn_time // burn_interval):
            time.sleep(burn_interval)
            total_damage += damage_per_second
            enemy.healthpoints -= damage_per_second
            print(f"The enemy is burning and has taken {damage_per_second} damage points!")
            print(f"The enemy has taken {total_damage} damage points from the burn effect.")
    
    def __repr__(self):
        return "The mage has {hp} HP {mp} MP {Karma} Karma and {sp} staminapoints.".format(hp=self.healthpoints, mp=self.magickapoints, Karma=self.karma, sp=self.staminapoints)

class enemy:
    def __init__(self, healthpoints, magicka, karma):
        self.healthpoints = 100
        self.magickapoints = 100
        self.karma = 100

    def dagger_attack(self, mage):
        if self.staminapoints >= 20:
            hit_chance = random.randint(1, 20)  # roll a 20-sided die for hit chance
            if hit_chance >= 10:  # attack hits if the roll is 10 or greater
                damage = random.randint(10, 15)  # roll another die for damage
                mage.healthpoints -= damage
                self.staminapoints -= 20
                print("The enemy has been hit by the dagger attack for {damage} damage!".format(damage=damage))
            else:
                self.staminapoints -= 10  # reduce stamina cost if the attack misses
                print("The dagger attack missed!")
        else:
            print("Not enough stamina to perform the dagger attack.")

    def fireball(self,mage):
        if self.magickapoints >= 50:
            hit_chance = random.randint(1, 20)
            if hit_chance >= 12:
                damage = random.randint(30,50)
                mage.healthpoints -= damage
                self.magickapoints -= 50
                print("The mage has been hit by the fireball attack for {damage} damage!".format(damage=damage))
            else:
                self.magickapoints -= 25
                print("The fireball misses its target!")
        else:
            print("Not enough magicka for this attack. You have {magicka} left.".format(magicka=self.magicka))

    def burn(self, mage):
        total_damage = 0
        burn_time = 10 # set the burn time to 10 seconds
        burn_interval = 2 # set the burn interval to 2 seconds
        damage_per_second = 5 # set the damage per second to 5
        for i in range(burn_time // burn_interval):
            time.sleep(burn_interval)
            total_damage += damage_per_second
            enemy.healthpoints -= damage_per_second
            print(f"The mage is burning and has taken {damage_per_second} damage points!")
            print(f"The mage has taken {total_damage} damage points from the burn effect.")
    def __repr__(self):
        return "The enemy has {hp} HP {mp} MP {Karma} Karma and {sp} staminapoints.".format(hp=self.healthpoints, mp=self.magickapoints, Karma=self.karma, sp=self.staminapoints)


#below this line debug values

#mage = Mage(100,100,100,100)
#enemy = Enemy(100,100,10)

#print(mage.fireball(enemy))
#print(f"Enemy health: {enemy.healthpoints}")

#below this line objects and gameplay stuff

name = input("What should your name be? ")
print("\nHello, " + name + "!")
print("\nYou are a mage, born with the gift of wielding magic beyond the limits of ordinary mortals. You have spent years honing your craft, mastering the arcane arts and delving deep into the mysteries of the universe. Your power is unparalleled, and your knowledge unmatched.")
print("\nBut with great power comes great responsibility, and you know all too well the dangers that come with wielding such immense magical energies. The world is full of those who seek to use your powers for their own selfish gain, and you must remain ever-vigilant to protect yourself and those you love.")
print("\nYet despite the risks, you continue to use your magic to do good in the world. You have traveled far and wide, vanquishing dark wizards and thwarting evil plots wherever you find them.")
print("\nYour name has become known far and wide, spoken in hushed tones by those who fear your power, and whispered in reverence by those who recognize your greatness.")
print("\nBut even as you stand at the height of your power, you know that there is much left to learn. The mysteries of the universe are endless, and there are always new spells to be discovered, new incantations to be spoken.")
print("\nAnd so you continue on your journey, ever-seeking, ever-searching, ever-growing in strength and knowledge. For you are a mage, and your destiny is written in the stars.")
