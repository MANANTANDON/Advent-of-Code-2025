with open("file.txt") as f:
    lines = [l.strip() for l in f.readlines()]

sep = lines.index("")
ranges = [tuple(map(int, r.split("-"))) for r in lines[:sep]]
numbers = [int(n) for n in lines[sep+1:] if n]


def StarNine():
    rangesStr = ranges
    nums = numbers 
    freshIngredients = []
    
    for n in nums:
        for start, end in rangesStr:
            if start <= n <= end:
                freshIngredients.append(n)
    
    print(len(list(set(freshIngredients))))
    

def StarTen():
    sorted_ranges = sorted(ranges)
    
    merged = []
    for start, end in sorted_ranges:
        if merged and start <= merged[-1][1] + 1:
            merged[-1] = (merged[-1][0], max(merged[-1][1], end))
        else:
            merged.append((start, end))
    
    total = sum(end - start + 1 for start, end in merged)
    print(total)

if __name__ == "__main__":
    # StarNine()
    StarTen()
