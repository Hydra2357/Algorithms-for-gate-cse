def huffman_coding(freq):
    """Huffman coding for lossless compression.
    Time Complexity: O(n log n)
    Space Complexity: O(n)
    """
    
    import heapq
    
    class Node:
        def __init__(self, char=None, freq=0, left=None, right=None):
            self.char = char
            self.freq = freq
            self.left = left
            self.right = right
        
        def __lt__(self, other):
            return self.freq < other.freq
    
    heap = [Node(char, f) for char, f in freq.items()]
    heapq.heapify(heap)
    
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        parent = Node(freq=left.freq + right.freq, left=left, right=right)
        heapq.heappush(heap, parent)
    
    root = heap[0]
    codes = {}
    
    def generate_codes(node, code):
        if node is None:
            return
        if node.char is not None:
            codes[node.char] = code or '0'
            return
        generate_codes(node.left, code + '0')
        generate_codes(node.right, code + '1')
    
    generate_codes(root, '')
    return codes

def huffman_encode(text, codes):
    """Encode text using Huffman codes."""
    return ''.join(codes[char] for char in text)

if __name__ == "__main__":
    freq = {'a': 5, 'b': 9, 'c': 12, 'd': 13, 'e': 16, 'f': 45}
    codes = huffman_coding(freq)
    print(f"Huffman codes: {codes}")
    
    text = "aabbccddee"
    encoded = huffman_encode(text, codes)
    print(f"Encoded text length: {len(encoded)} bits")
