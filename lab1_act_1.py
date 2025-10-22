
def num1(string):
    state = "a"
    for ch in string:
        match state:
            case "a":
                match ch:
                    case "0": state = "a"
                    case "1": state ="b"
            case "b":
                match ch:
                    case "0": state = "final"
                    case "1": state ="b"
            case "c":
                match ch:
                    case "0": state = "b"
                    case "1": state = "final"
    return state =="final"

def num2(string):
    state ="q0"
    for ch in string:
        match state:
            case "q0":
                match ch:
                    case "a": state = "q1"
                    case "b": state = "q2"
            case "q1":
                match ch:
                    case "a": state = "q0"
                    case "b": state = "q3"
            case "q2":
                match ch:
                    case "a": state ="q3"
                    case "b": state = "q0"
            case "q3":
                match ch:
                    case "a": state = "q2"
                    case "b": state = "q1"
    return state == "q3"

#Num1
# Accepted:{10},{101},{10101}
# Rejected:{0},{11},{1000}
#Num2
# Accepted: {ab},{abba},{abab}
# Rejected: {a},{b},{aa}

print("Choose DFA test:(1,2)")
choice = input("Enter Choice")

test_string = input("Enter value")

if choice =="1":
    result = num1(test_string)
    if result:
        print(f"{test_string} is accepted")
    else:
        print(f"{test_string} is rejected")

elif choice =="2":
    result = num2(test_string)
    if result:
        print(f"{test_string} is accepted")
        print(f"{test_string} is rejected")
else:
    print("Invalid Choice")
        
