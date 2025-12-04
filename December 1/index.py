INPUT_FILE_PATH = "file.txt" 

def StarOne():
    with open(INPUT_FILE_PATH, "r") as f:
        content = [line.strip() for line in f]
    
    currentPosition = 50
    count = 0
    document = content # ["L68","L30","R48","L5","R60","L55","L1","L99","R14","L82"]

    for n in document:
        checkForLorR = list(n) 
        if (checkForLorR[0] == "L"):
            distance = int(n.split("L")[1])
            new_position = (currentPosition - distance) % 100
            if(new_position == 0 or new_position == 100): 
                count += 1
            currentPosition = new_position    
        else:
            distance = int(n.split("R")[1])
            new_position = (currentPosition + distance) % 100
            if(new_position == 0 or new_position == 100): 
                count += 1
            currentPosition = new_position
    print(f"count: {count}")

def StarTwo():
    with open(INPUT_FILE_PATH, "r") as f:
        content = [line.strip() for line in f]
    
    currentPosition = 50
    totalCrossing = 0
    document = content # ["L68","L30","R48","L5","R60","L55","L1","L99","R14","L82"]

    for n in document:
        checkForLorR = list(n) 
        if (checkForLorR[0] == "L"):
            distance = int(n.split("L")[1])
            
            # Count crossings DURING rotation (not landing)
            totalCrossing += (distance // 100)
            remaining = distance % 100
            if remaining > 0:
                next_pos = currentPosition - remaining
                if next_pos < 0 and currentPosition > 0:
                    totalCrossing += 1
            
            new_position = (currentPosition - distance) % 100
            
            # Count if we LAND on 0
            if new_position == 0:
                totalCrossing += 1
                
            currentPosition = new_position    
        else:
            distance = int(n.split("R")[1])
            
            # Count crossings DURING rotation (not landing)
            totalCrossing += (distance // 100)
            remaining = distance % 100
            if remaining > 0:
                next_pos = currentPosition + remaining
                if next_pos > 100:
                    totalCrossing += 1
            
            new_position = (currentPosition + distance) % 100
            
            # Count if we LAND on 0
            if new_position == 0:
                totalCrossing += 1
                
            currentPosition = new_position

    print(f"All over Crossing: {totalCrossing}")

    
if __name__ == "__main__":
   StarOne()
   StarTwo()