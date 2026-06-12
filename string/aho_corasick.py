from collections import defaultdict, deque

def aho_corasick(patterns):
    """Aho-Corasick algorithm for multi-pattern matching.
    Time Complexity: O(n + z) where z is number of pattern occurrences
    Space Complexity: O(m * k) where m is total pattern length, k is alphabet size
    """
    
    class TrieNode:
        def __init__(self):
            self.goto = {}
            self.fail = None
            self.output = []
    
    root = TrieNode()
    
    # Build trie
    for pattern in patterns:
        node = root
        for char in pattern:
            if char not in node.goto:
                node.goto[char] = TrieNode()
            node = node.goto[char]
        node.output.append(pattern)
    
    # Build failure function
    queue = deque()
    root.fail = root
    
    for child in root.goto.values():
        child.fail = root
        queue.append(child)
    
    while queue:
        node = queue.popleft()
        
        for char, child in node.goto.items():
            queue.append(child)
            fail = node.fail
            
            while fail != root and char not in fail.goto:
                fail = fail.fail
            
            child.fail = fail.goto.get(char, root)
            child.output.extend(child.fail.output)
    
    return root

def aho_corasick_search(text, patterns):
    """Search for multiple patterns in text using Aho-Corasick."""
    
    root = aho_corasick(patterns)
    node = root
    matches = []
    
    for i, char in enumerate(text):
        while node != root and char not in node.goto:
            node = node.fail
        
        if char in node.goto:
            node = node.goto[char]
        else:
            node = root
        
        for pattern in node.output:
            matches.append((i - len(pattern) + 1, pattern))
    
    return matches

if __name__ == "__main__":
    text = "ushers"
    patterns = ["she", "he", "her", "hers"]
    matches = aho_corasick_search(text, patterns)
    print(f"Matches found: {matches}")
