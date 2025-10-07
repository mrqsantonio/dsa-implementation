from dsa import *
from attacks import *

class LeavingException(Exception):
    pass

domain_parameters = {}
session_keys = {}

def get_input(message):
    while True:
        try:
            choice = input(f"Please introduce the {message} or 'x' to exit> ").strip()
            if choice == "x":
                raise LeavingException("Leaving...")
            return int(choice)
        except ValueError:
            print("Please enter a valid number.")
            continue

def create_domain_parameters():
    global domain_parameters
    global session_keys
    while True:
        n = get_input("number of bits of q")
        print("Generating new domain parameters...")
        try:
            domain_parameters = get_DSAparameters(n)
            session_keys = {}
            print(f"New Domain Paramters generated! {str(domain_parameters)}")
            break
        except Exception as e:
            print(str(e))


def create_session():
    global session_keys
    if domain_parameters == {}:
        print("Make sure you have a valid domain.")
        return
    print("Generating new session...")
    print(f"{str(domain_parameters)}")
    p, q, g = domain_parameters
    session_keys = get_skeys(p, q, g)
    print(f"New Session Generated! {str(session_keys)}")

def sign_message():
    if domain_parameters == {} or session_keys == {}:
        print("Make sure you have a valid session/domain.")
        return
    message = get_input("message to be signed")
    print("Signing message...")
    p, q, g = domain_parameters
    x, y = session_keys
    r, s = dsa_sign(message, p, q, g, x)
    print(f"Your message: '{message}' was signed with ({r}, {s}).")

def verify_message():
    if domain_parameters == {} or session_keys == {}:
        print("Make sure you have a valid session/domain.")
        return
    p, q, g = domain_parameters
    x, y = session_keys
    print("Remember that you can only verify messages signed within this session/domain.")
    message = get_input("message to be verified")
    r = get_input("first field of the signature")
    s = get_input("second filed of the signature")
    signature = [r, s]
    is_authentic = dsa_verify(message, signature, p, q, g, y)
    if is_authentic:
        print("This signature has been verified.")
    else:
        print("This signature isn't valid.")

def brute_force_atack():
    y = get_input("y")
    g = get_input("g")
    p = get_input("p")
    print("Calculating private Key...")
    x = get_private_key(y,g,p)
    print(f"Your Private Key: '{x}' found with y= '{y}',g= '{g}', p ='{p}'")
    
def key_repeticion_atack():
    m1 = get_input("message 1")
    m2 = get_input("message 2")
    q = get_input("prime q")
    r = get_input("first field of the signature with is the same in both messages")
    s1 = get_input("second field of the signature of the first message")
    s2 = get_input("second field of the signature of the first message")
    print("Breaking private Key...")
    x = get_private_key_from_k(m1, s1, m2, s2, r, q)
    print(f"Your Private Key: '{x}' found with m1='{m1}', m2='{m2}', q='{q}', r='{r}', s1='{s1}', s2='{s2}'")

def restore_session():
    global domain_parameters
    global session_keys
    p = get_input("p")
    q = get_input("q")
    g = get_input("g")
    x = get_input("x")
    y = get_input("y")
    domain_paramters = {p, q, g}
    session_keys = {x, y}
    print("Restoring session...")

def main():
    options = {
        "1": "Create domain",
        "2": "Create session",
        "3": "Sign message",
        "4": "Verify message",
        "5": "Brute force atack",
        "6": "Key repeticion atack",
        "7": "Restore session",
        "8": "Exit"
    }

    while True:
        print("\n")
        if domain_parameters != {}:
            p, q, g = domain_parameters
            print(f"p={p} q={q} g={g} {f"x={session_keys[0]} y={session_keys[1]}" if session_keys != {} else ""}")
        print("--- Main Menu ---")
        for key, value in options.items():
            print(f"{key}. {value}")

        try:
            choice = input("Select an option> ").strip()
            if choice == "1":
                create_domain_parameters()
            elif choice == "2":
                create_session()
            elif choice == "3":
                sign_message()
            elif choice == "4":
                verify_message()
            elif choice == "5":
                brute_force_atack()
            elif choice == "6":
                key_repeticion_atack()
            elif choice == "7":
                restore_session()
            elif choice == "8":
                print("\n")
                return
            else:
                print("Invalid choice. Please try again.")
        except LeavingException:
            print("Going back to main menu...")
        except KeyboardInterrupt:
            print("\n")
            return

if __name__ == "__main__":
    main()