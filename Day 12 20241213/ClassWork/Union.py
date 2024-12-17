#Python Program to demostrate Union of two sets

human={"Prawesh","Pukar","Kiran"}
werewolf={"Sagar","Shushil","Sailendra"}
vampires={"Pashupati","Prasna"}

population = human.union(vampires)
print("Union of human and vampires",population)

population = population|werewolf
print("Union of population and werewolf",population)