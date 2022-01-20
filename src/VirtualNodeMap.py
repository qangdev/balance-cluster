import random


# Stores the vnode to node mapping
# Composed within a node so that every node has its own vnode mapping
class VirtualNodeMap:
    def __init__(self, node_names, TOTAL_VIRTUAL_NODES):
        self._vnode_map = {}
        self._node_names = node_names
        self._TOTAL_VIRTUAL_NODES = TOTAL_VIRTUAL_NODES

    @property
    def vnode_map(self):
        return self._vnode_map

    @property
    def node_names(self):
        return self._node_names

    # Populates the Virtual Node Nap, given the set of Node names.
    # Creates a mapping of Virtual Node to corresponding assigned physical Node
    def populate_map(self):
        def generate_pointer(n):
            # This helps on mapping randonly and equally
            # each time it will return a list from 0 to n - 1 and then shuffle it.
            # e.g: n = 4
            # result [0,1,2,3]; [0,3,2,1]; [1,3,2,0]
            indexes = list(range(0, n))
            random.shuffle(indexes)
            return indexes

        # Problem statement 1
        # Generate a dict of vnode ids (0 to (TOTAL_VIRTUAL_NODES - 1) mapped randomly
        # but equally (as far as maths permits) to node names
        self._vnode_map = {}
        
        pointers = []
        for i in range(self._TOTAL_VIRTUAL_NODES):
            if not pointers:
                pointers = generate_pointer(len(self.node_names))
            self._vnode_map[i] = self._node_names[pointers.pop()]

    # Return the vnode name mapped to a particular vnode
    def get_node_for_vnode(self, vnode):
        return self._vnode_map[vnode]

    # Returns the vnode name where a particular key is stored
    # It finds the vnode for the key through modulo mapping, and then looks up the physical node
    def get_assigned_node(self, key):
        vnode = key % self._TOTAL_VIRTUAL_NODES
        return self._vnode_map[vnode]

    # Assign a new node name as mapping for a particular vnode
    # This is useful when vnodes are remapped during node addition or removal
    def set_new_assigned_node(self, vnode, new_node_name):
        self._vnode_map[vnode] = new_node_name

