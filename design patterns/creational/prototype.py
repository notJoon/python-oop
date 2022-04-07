""" Prototype (creational type)

    Specify the kinds of objects to create using a prototypical instance,
    and create new objects by copying this prototype.

    * use the Prototype pattern should be independent of how its products are created, composed and represented.
    * particularly useful with static languages, where classes are not objects, and little or no type information is available.

    Pros and Cons 
        * Pros 
            - Adding and removing products at run-time. client can install and remove prototypes at run-time.
            - Specifying new objects by varing values and structures. 
            - Reduced subclassing
        
        * Cons
            - Cloning complex objects that have circular references might be very tricky.
"""