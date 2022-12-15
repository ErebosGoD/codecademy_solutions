class Node:
    def __init__(self,value,next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next_node(self):
        return self.next_node

    def set_next_node(self,next_node):
        self.next_node = next_node

class LinkedList:
    def __init__(self,value=None):
        self.head_node = Node(value)
    def get_head_node(self):
        return self.head_node

    def insert_beginning(self,new_value):
        new_node = Node(new_value)
        new_node.set_next_node(self.head_node)
        self.head_node = new_node

    def stringify_list(self):
        string_list = ""
        current_node = self.get_head_node()
        while current_node:
        #simply, as long as the current node has a value, add it to the string list and jump to the next node
            if current_node.get_value() != None:
                string_list += str(current_node.get_value()) + "\n"
            current_node = current_node.get_next_node()
        return string_list

    def remove_node(self,value_to_remove):
        current_node = self.head_node
        #if the value of the head node equals the value to be removed, set the head node to the current nodes next node
        if self.head_node.get_value() == value_to_remove:
            self.head_node = current_node.get_next_node()
        #as long as there is a current node, the next node is the next node of the current node
        # if the current nodes next nodes value equals the value to be removed, set the current nodes next to the next nodes next node 
        #else the current node equals the next node
        else:
            while current_node:
                next_node = current_node.get_next_node()
                if next_node.get_value() == value_to_remove:
                    current_node.set_next_node(next_node.get_next_node())
                else:
                    current_node = next_node
