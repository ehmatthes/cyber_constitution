class CyberConstitution():
    """A solid set of laws, that doesn't limit speech."""
    
    def __init__(self):
        """Initialize the constitution."""
        self.state = ''
        self.author = ''
        self.preamble = ''
        self.laws = []
        
    def add_law(self, new_law):
        """Add the new law to the list of existing laws."""
        self.laws.append(new_law)
        
    def show_laws(self):
        """Show all the laws in the constitution."""
        for law in self.laws:
            print(law)
            
    def show_constitution(self):
        """Show the entire constitution."""
        print("This is the cyber constitution for the state of " +
            self.state.title() + ".\n\n")
        print("Authored by: " + self.author)
        print("\n\nOur constitution contains the following laws:\n")
        self.show_laws()
