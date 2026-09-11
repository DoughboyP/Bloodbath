import time
import sys

def print_slow(text, delay=0.03):
    """Prints text with a dramatic typing effect."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def intro():
    print("=" * 60)
    print("                WELCOME TO BLOODBATH: THE NEW ORDER            ")
    print("=" * 60)
    print_slow("\nThe old world order fell during the Great Revolt.")
    print_slow("The Syndicate—once dismissed as mere gangsters—took on the system.")
    print_slow("The war was brutal, but the turning point wasn't fought on the streets.")
    print_slow("It was fought in the digital ether...")
    time.sleep(1)
    
def satellite_hack():
    print("\n[SYSTEM ALERT]: INITIATING ARCHIVAL PLAYBACK: 'THE DAY HQ FELL'")
    print("-" * 60)
    print_slow("Syndicate Hacking Rig: Connected to orbital network...")
    
    input("\n[Press ENTER to bypass the Central System Firewall]")
    print_slow("Bypassing firewalls... [████████████████████] 100%")
    
    input("\n[Press ENTER to hijack orbital coordinates]")
    print_slow("Target locked: System Command Headquarters.")
    print_slow("Satellite weapon: 'Zephyr-9' Kinetic Missile Array Primed.")
    
    input("\n[Type 'LAUNCH' and press ENTER to fire]: ")
    print("\n[!] MISSILE LAUNCHED.")
    time.sleep(1)
    print_slow("Countdown: 3... 2... 1...")
    print("\n💥 DETONATION TRACE CONFIRMED. HEADQUARTERS IS ASH.")
    print("-" * 60)
    time.sleep(1)

def rule_the_world():
    print("\n" + "=" * 50)
    print("       NEW ERA: THE IRON SYNDICATE GRID")
    print("=" * 50)
    print_slow("The war is over. The Street Enforcers and Cyber-Jackers have united.")
    print_slow("Muscle and code now rule side-by-side as a single joint domain.")
    print_slow("The old government is gone, and the world waits for your first decrees.\n")
    
    print("DECISION 1: How will you handle the surviving citizens of the old system?")
    print("1. Enslave them as laborers to rebuild infrastructure.")
    print("2. Recruit them into the lower ranks of the Syndicate.")
    print("3. Leave them alone but tax them heavily in crypto and resources.")
    
    choice1 = input("\nEnter choice (1, 2, or 3): ")
    print("\n" + "-" * 40)
    if choice1 == "1":
        print_slow("[DECREE SAVED]: Labor camps established. Heavy infrastructure boom, but dissent is growing.")
    elif choice1 == "2":
        print_slow("[DECREE SAVED]: Syndicate numbers skyrocket. The new generation swears loyalty to the streets.")
    else:
        print_slow("[DECREE SAVED]: High taxes fill the Syndicate vaults. The economy thrives under a black market.")
        
    print("\nDECISION 2: What is the main priority for the satellite network now?")
    print("1. Weaponize it further—keep missiles locked on any city that dares defy you.")
    print("2. Use it for total digital surveillance—spy on every message and connection on Earth.")
    print("3. Turn it into a global pirate broadcast—stream gang propaganda and raw entertainment.")
    
    choice2 = input("\nEnter choice (1, 2, or 3): ")
    print("\n" + "-" * 40)
    if choice2 == "1":
        print_slow("[DECREE SAVED]: Absolute military dominance achieved. No one dares start a rebellion.")
    elif choice2 == "2":
        print_slow("[DECREE SAVED]: Privacy is dead. The Cyber-Jackers stop every counter-revolution before it starts.")
    else:
        print_slow("[DECREE SAVED]: The world embraces the chaos. Syndicate culture becomes the global norm.")

    print("\n" + "=" * 50)
    print_slow("The foundation of Bloodbath has been laid. Long live the Grid.")
    print("=" * 50)

def main():
    intro()
    satellite_hack()
    rule_the_world()

if __name__ == "__main__":
    main()
