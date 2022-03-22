class Interface():

    def hangman(self, lives: int):
        if lives == 0:
            print( """  
                = = = = =
                |       |  
                |       |
                |      ( )
                |    ___|___
                |       |
                |       |
                |      / \ 
                |     /   \ 
             = = = =          """
            )
        elif lives == 1:
            print( """  
                = = = = =
                |       |  
                |       |
                |      ( )
                |    ___|___
                |       |
                |       |
                |      /  
                |     /    
             = = = =          """
            )
        elif lives == 2:
            print( """  
                = = = = =
                |       |  
                |       |
                |      ( )
                |    ___|___
                |       |
                |       |
                |       
                |     
             = = = =          """
            )
        elif lives == 3:
            print( """  
                = = = = =
                |       |  
                |       |
                |      ( )
                |    ___|
                |       |
                |       |
                |        
                |         
             = = = =          """
            )
        elif lives == 4:
            print( """  
                = = = = =
                |       |  
                |       |
                |      ( )
                |       |
                |       |
                |       |
                |        
                |         
             = = = =          """
            )
        elif lives == 5:
            print( """  
                = = = = =
                |       |  
                |       |
                |      ( )
                |       
                |       
                |       
                |        
                |         
             = = = =          """
            )
        else:
            print( """  
                = = = = =
                |       |  
                |       |
                |      
                |       
                |       
                |       
                |        
                |         
             = = = =          """
            )